//	cmssw includes
#include "DQM/HcalTasks/interface/HcalTPTask.h"

//	system includes
#include <iostream>
#include <string>

HcalTPTask::HcalTPTask(edm::ParameterSet const&ps):
	hcaldqm::HcalDQSource(ps)
{}

/* virtual */ HcalTPTask::~HcalTPTask()
{
}

/* virtual */ void HcalTPTask::beginLuminosityBlock(
		edm::LuminosityBlock const& lb, edm::EventSetup const& es)
{
	HcalDQSource::beginLuminosityBlock(lb, es);
}

/* virtual */ void HcalTPTask::endLuminosityBlock(
		edm::LuminosityBlock const& lb, edm::EventSetup const& es)
{
	HcalDQSource::endLuminosityBlock(lb, es);
}

/* virtual */ void HcalTPTask::reset(int const periodflag)
{
	HcalDQSource::reset(periodflag);
	if (periodflag==0)
	{
		// Event
	}
	else if (periodflag==1)
	{
		// LS
	}
}

/* virtual */ void HcalTPTask::doWork(edm::Event const& e,
		edm::EventSetup const& es)
{
	edm::Handle<HcalTrigPrimDigiCollection>		ctpd;
	edm::Handle<HcalTrigPrimDigiCollection>		ctpe;

	INITCOLL(_lables["HCALTPD"], ctpd);
	INITCOLL(_lables["HCALTPE"], ctpe);
	this->process(*ctpd, *ctpe, std::string("HBHE"), 1);
	this->process(*ctpe, *ctpd, std::string("HBHE"), 2);
	this->process(*ctpd, *ctpe, std::string("HF"), 1);
	this->process(*ctpe, *ctpd, std::string("HF"), 2);
}

template<typename Hit>
void HcalTPTask::specialize(Hit const& hit1, Hit const& hit2, 
		std::string const& nameRes, int const wtw)
{
	//	 wtw=2 is comparing Data to Emulator, upon matching should be skipped
	//	 as this has been processed already when comparing emulator to data
	if (wtw==2)
		return;

	//	get all the info we need
	int iphi = hit1.id().iphi();
	int ieta = hit1.id().ieta();
	int subdet = hit1.id().subdet();
	int soi_cEt_1 = hit1.SOI_compressedEt();
	int soi_cEt_2 = hit2.SOI_compressedEt();
//	bool soi_fineGrain_1 = hit1.SOI_fineGrain();
//	bool soi_fineGrain_2 = hit2.SOI_fineGrain();
	int ps_1 = hit1.presamples();
	int ps_2 = hit2.presamples();

	//	SOI plots + presamples
	_mes[nameRes + "_SOI_Et_Data"].Fill(soi_cEt_1);
	_mes[nameRes + "_SOI_Et_Emul"].Fill(soi_cEt_2);
	_mes[nameRes + "_Presamples_Data"].Fill(ps_1);
	_mes[nameRes + "_Presamples_Emul"].Fill(ps_2);

	for (int i=0; i<hit1.size(); i++)
	{
		int cEt_1 = hit1.sample(i).compressedEt();
		int cEt_2 = hit2.sample(i).compressedEt();
//		bool fg_1 = hit1.sample(i).fineGrain();
//		bool fg_2 = hit2.sample(i).fineGrain();
//		int diff = abs(cEt_1-cEt_2);

		_mes[nameRes + "_EtShape_Data"].Fill(i, cEt_1);
		_mes[nameRes + "_EtShape_Emul"].Fill(i, cEt_2);
		
		/*
		//	if cEts are the same for this TS
		if (diff==0)
		{
			//	if Fine Grain bits aren't the same
			if (fg_1!=fg_2)
			{
				//	have mismatch in FG bitOB
			}
		}
		else 
		{

		}
		*/
	}

	//	Occupancy Maps
	_mes[nameRes + "_TPOccupancyVSiphi"].Fill(iphi);
	_mes["HBHEHF_TPOccupancyVSiphi"].Fill(iphi);
	_mes["HBHEHF_TPOccupancyVSieta"].Fill(ieta);
}

//	Performed if hit2(hit1.id()) isn't found in the collection.
template<typename>
void HcalTPTask::check(Hit const& hit1, int const wtw)
{

}

DEFINE_FWK_MODULE(HcalTPTask);



