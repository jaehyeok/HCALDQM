//	cmssw includes
#include "DQM/HcalTasks/interface/HcalRawTask.h"

//	system includes
#include <iostream>
#include <string>

HcalRawTask::HcalRawTask(edm::ParameterSet const&ps):
	hcaldqm::HcalDQSource(ps)
{}

/* virtual */ HcalRawTask::~HcalRawTask()
{
}

/* virtual */ void HcalRawTask::beginLuminosityBlock(
		edm::LuminosityBlock const& lb, edm::EventSetup const& es)
{
	HcalDQSource::beginLuminosityBlock(lb, es);
}

/* virtual */ void HcalRawTask::endLuminosityBlock(
		edm::LuminosityBlock const& lb, edm::EventSetup const& es)
{
	HcalDQSource::endLuminosityBlock(lb, es);
}

/* virtual */ void HcalRawTask::doWork(edm::Event const& e,
		edm::EventSetup const& es)
{
	//	We need this module only for the Normal Calibration Mode
	if (_mi.currentCalibType>0)
		return;

	edm::Handle<FEDRawDataCollection> craw;
	INITCOLL(_labels["RAW"], craw);
	this->process(*craw);
}

/* virtyal */ void HcalRawTask::reset(int const periodflag)
{
	HcalDQSource::reset(periodflag);
	if (periodflag==0)
	{
		//	per event
	}
	else if (periodflag==1)
	{
		//	per LS
	}
}

void HcalRawTask::specialize(FEDRawData const& raw, int ifed)
{

}

DEFINE_FWK_MODULE(HcalRawTask);



