#ifndef HCALLEDTASK_H
#define HCALLEDTASK_H

/*
 *	file:			HcalLEDTask.h
 *	Author:			Viktor Khristenko
 *	Start Date:		03/04/2015
 */

#include "DQM/HcalCommon/interface/HcalMECollection.h"
#include "DQM/HcalCommon/interface/HcalDQSource.h"

class HcalLEDTask : public hcaldqm::HcalDQSource
{
	public:
		HcalLEDTask(edm::ParameterSet const&);
		virtual ~HcalLEDTask();

		virtual void doWork(edm::Event const&e,
				edm::EventSetup const& es);
		virtual void beginLuminosityBlock(edm::LuminosityBlock const&,
				edm::EventSetup const&);
		virtual void endLuminosityBlock(edm::LuminosityBlock const&,
				edm::EventSetup const&);

		virtual void reset(int const);

	private:
		//	MEs Collection come from the base class
		//	Here, we only need module specific parameters
		template<typename Hit>
		void specialize(Hit const& hit, std::string const&,
				int const wtw=1);

		DEFPROCESSOR(HBHEDigiCollection, HBHEDataFrame);
		DEFPROCESSOR(HODigiCollection, HODataFrame);
		DEFPROCESSOR(HFDigiCollection, HFDataFrame);

		hcaldqm::HcalDQLedData _ledData[hcaldqm::constants::STD_NUMSUBS]
			[hcaldqm::constants::STD_NUMIETAS][hcaldqm::constants::STD_NUMIPHIS]
			[hcaldqm::constants::STD_NUMDEPTHS][hcaldqm::constants::STD_NUMCAPS];
		hcaldqm::packaging::Packager _packager[hcaldqm::constants::STD_NUMSUBS];
};

#endif
