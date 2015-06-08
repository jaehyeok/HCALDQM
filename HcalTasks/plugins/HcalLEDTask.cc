//	cmssw includes
#include "DQM/HcalTasks/interface/HcalLEDTask.h"

//	system includes
#include <iostream>
#include <string>

HcalLEDTask::HcalLEDTask(edm::ParameterSet const&ps):
	hcaldqm::HcalDQSource(ps)
{
	_packager[0] = hcaldqm::packaging::Packager(
		hcaldqm::constants::STD_HB_MINIPHI,
		hcaldqm::constants::STD_HB_MAXIPHI,
		hcaldqm::constants::STD_HB_STEPIPHI,
		hcaldqm::constants::STD_HB_MINIETA,
		hcaldqm::constants::STD_HB_MAXIETA,
		hcaldqm::constants::STD_HB_MINDEPTH,
		hcaldqm::constants::STD_HB_MAXDEPTH
	);
	_packager[1] = hcaldqm::packaging::Packager(
		hcaldqm::constants::STD_HE_MINIPHI,
		hcaldqm::constants::STD_HE_MAXIPHI,
		hcaldqm::constants::STD_HE_STEPIPHI,
		hcaldqm::constants::STD_HE_MINIETA,
		hcaldqm::constants::STD_HE_MAXIETA,
		hcaldqm::constants::STD_HE_MINDEPTH,
		hcaldqm::constants::STD_HE_MAXDEPTH
	);
	_packager[2] = hcaldqm::packaging::Packager(
		hcaldqm::constants::STD_HO_MINIPHI,
		hcaldqm::constants::STD_HO_MAXIPHI,
		hcaldqm::constants::STD_HO_STEPIPHI,
		hcaldqm::constants::STD_HO_MINIETA,
		hcaldqm::constants::STD_HO_MAXIETA,
		hcaldqm::constants::STD_HO_MINDEPTH,
		hcaldqm::constants::STD_HO_MAXDEPTH
	);
	_packager[3] = hcaldqm::packaging::Packager(
		hcaldqm::constants::STD_HF_MINIPHI,
		hcaldqm::constants::STD_HF_MAXIPHI,
		hcaldqm::constants::STD_HF_STEPIPHI,
		hcaldqm::constants::STD_HF_MINIETA,
		hcaldqm::constants::STD_HF_MAXIETA,
		hcaldqm::constants::STD_HF_MINDEPTH,
		hcaldqm::constants::STD_HF_MAXDEPTH
	);
}

/* virtual */ HcalLEDTask::~HcalLEDTask()
{
}

/* virtual */ void HcalLEDTask::beginLuminosityBlock(
		edm::LuminosityBlock const& lb, edm::EventSetup const& es)
{
	HcalDQSource::beginLuminosityBlock(lb, es);
}

/* virtual */ void HcalLEDTask::endLuminosityBlock(
		edm::LuminosityBlock const& lb, edm::EventSetup const& es)
{
	HcalDQSource::endLuminosityBlock(lb, es);
}

/* virtual */ void HcalLEDTask::reset(int const periodflag)
{
	HcalDQSource::reset(periodflag);
	if (periodflag==0)
	{
		//	for Event
	}
	else if (periodflag==1)
	{
		//	for LS
	}
}

/* virtual */ void HcalLEDTask::doWork(edm::Event const& e,
		edm::EventSetup const& es)
{
	edm::Handle<HBHEDigiCollection>		chbhe;
	edm::Handle<HODigiCollection>		cho;
	edm::Handle<HFDigiCollection>		chf;

	INITCOLL(_labels["HBHEDigi"], chbhe);
	INITCOLL(_labels["HODigi"], cho);
	INITCOLL(_labels["HFDigi"], chf);

	this->process(*chbhe, std::string("HB"));
	this->process(*chbhe, std::string("HE"));
	this->process(*cho, std::string("HO"));
	this->process(*chf, std::string("HF"));
}

template<typename Hit>
void HcalLEDTask::specialize(Hit const& hit, std::string const& nameRes,
		int const wtw)
{/*
	int iphi = hit.id().iphi();
	int ieta = hit.id().ieta();
	int depth = hit.id().depth();
	int subdet = hit.id().subdet()-1;
	int digisize = hit.size();

	//	Fills up Prioprietary Class for LED Monitoring
	for (int i=0; i<digisize; i++)
	{
		_ledData[subdet][_packager[subdet].iieta(ieta)]
			[_packager[subdet].iiphi(iphi)]
			[_packager[subdet].idepth(depth)]
			[hit.sample(i).capid()].push(hit.sample(i).adc());
	}
	*/
}

DEFINE_FWK_MODULE(HcalLEDTask);



