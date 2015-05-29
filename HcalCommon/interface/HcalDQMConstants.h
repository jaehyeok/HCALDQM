#ifndef HCALDQMCONSTANTS_H
#define HCALDQMCONSTANTS_H

namespace hcaldqm
{
	namespace constants
	{
		//	Generic Constants
		int const RAWDATASIZE_CALIB					=24;
		int const RAWDATASIZE_HEADERTRAILER			= 12;
		int const MAXCALIBTYPE						=7;
		int const MIN_FIBER_IDLEOFFSET				=-7;
		int const MAX_FIBER_IDLEOFFSET				=	7;
		int const INVALID_FIBER_IDLEOFFSET			=	-1000;
	
		//	Hcal Specific Constants (not SubSystem specific)
		int const STD_NUMSUBS						=		4;
	
		//	HF Specific Constants
		int const STD_SUBDET_HF						=	3;
		double const STD_HF_PED						=		2.5;
		int const STD_HF_DIGISIZE_GLOBAL			=		4;
		int const STD_HF_DIGISIZE_LOCAL				=	10;
		double const STD_HF_DIGI_CUT_3TSQg20		=		20.;
		double const STD_HF_DIGI_ZSCUT				= 
			STD_HF_DIGI_CUT_3TSQg20;
		double const STD_HF_RECHIT_CUT_eg2			= 2.;
		double const STD_HF_RECHIT_ZSCUT			= 
			STD_HF_RECHIT_CUT_eg2;
	
		//	HB Specific
		int const STD_SUBDET_HB						=	0;
		int const STD_HB_DIGISIZE_GLOBAL			=		10;
		double const STD_HB_PED						=		0;
		double const STD_HB_DIGI_CUT_3TSQg20		=		20.;
		double const STD_HB_DIGI_ZSCUT				=
			STD_HB_DIGI_CUT_3TSQg20;
		double const STD_HB_RECHIT_CUT_eg2			= 2.;
		double const STD_HB_RECHIT_ZSCUT			= 
			STD_HB_RECHIT_CUT_eg2;
	
		//	HE Specific
		int const STD_SUBDET_HE						=	1;
		int const STD_HE_DIGISIZE_GLOBAL			=		10;
		double const STD_HE_PED						=		0;
		double const STD_HE_DIGI_CUT_3TSQg20		=		20.;
		double const STD_HE_DIGI_ZSCUT				=
			STD_HE_DIGI_CUT_3TSQg20;
		double const STD_HE_RECHIT_CUT_eg2			= 2.;
		double const STD_HE_RECHIT_ZSCUT			= 
			STD_HE_RECHIT_CUT_eg2;
	
		//	HO Specific Constants
		int const STD_SUBDET_HO						=	2;
		int const STD_HO_DIGISIZE_GLOBAL			=		10;
		double const STD_HO_PED						=		8.5;
		double const STD_HO_DIGI_CUT_3TSQg30		=		30.;
		double const STD_HO_DIGI_ZSCUT				=
			STD_HO_DIGI_CUT_3TSQg30;
		double const STD_HO_RECHIT_CUT_eg0			= 0;
		double const STD_HO_RECHIT_ZSCUT			= 
			STD_HO_RECHIT_CUT_eg0;

		//	Other 
		int const STD_SUBDET_OTHER					=	4;
	
		//	More Hcal Specific
		double const PEDESTALS[STD_NUMSUBS] = {
			STD_HB_PED, STD_HE_PED, STD_HO_PED, STD_HF_PED
		};

		double const DIGISIZE_GLOBAL[STD_NUMSUBS] = {
			STD_HB_DIGISIZE_GLOBAL, STD_HE_DIGISIZE_GLOBAL,
			STD_HO_DIGISIZE_GLOBAL, STD_HF_DIGISIZE_GLOBAL
		};

		double const DIGI_ZSCUT[STD_NUMSUBS] = {
			STD_HB_DIGI_ZSCUT, STD_HE_DIGI_ZSCUT, 
			STD_HO_DIGI_ZSCUT, STD_HF_DIGI_ZSCUT
		};

		double const RECHIT_ZSCUT[STD_NUMSUBS] = {
			STD_HB_RECHIT_ZSCUT, STD_HE_RECHIT_ZSCUT,
			STD_HO_RECHIT_ZSCUT, STD_HF_RECHIT_ZSCUT
		};
	}
}

#endif














