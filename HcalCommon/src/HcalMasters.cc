#include "DQM/HcalCommon/interface/HcalMasters.h"

namespace hcaldqm
{
	void HcalDcsMaster::initDcs(DcsStatusCollection const& cdcs)
	{
		//	HBHE go together
		if (cdcs[0].ready(DcsStatus::HBHEa) &&
			cdcs[0].ready(DcsStatus::HBHEb) &&
			cdcs[0].ready(DcsStatus::HBHEc))
		{
			_dcs[hcaldqm::constants::STD_SUBDET_HB] = true;
			_dcs[hcaldqm::constants::STD_SUBDET_HE] = true;
		}
		else
		{
			_dcs[hcaldqm::constants::STD_SUBDET_HB] = false;
			_dcs[hcaldqm::constants::STD_SUBDET_HE] = false;
		}

		//	HO
		if (cdcs[0].ready(DcsStatus::HO))
			_dcs[hcaldqm::constants::STD_SUBDET_HO] = true;
		else 
			_dcs[hcaldqm::constants::STD_SUBDET_HO] = false;

		//	HF
		if (cdcs[0].ready(DcsStatus::HF))
			_dcs[hcaldqm::constants::STD_SUBDET_HF] = true;
		else 
			_dcs[hcaldqm::constants::STD_SUBDET_HF] = false;
	}
/*
	void HcalTriggerMaster::initL1GT(L1GlobalTriggerReadoutRecord const& l1gtrr)
	{
		const TechnicalTriggerWord tw = l1gtrr.technicalTriggerWord();
		const DecisionWord dw = l1gtrr.decisionWord();
		bool host; 
		if (!tw.empty())
			host = tw.at(hcaldqm::constants::STD_HO_SELFTRIGGER_TECHPOS);


		return;
	}
	*/
}






