import FWCore.ParameterSet.Config as cms 

#	import standard cfg and clone the parameters
import DQM.HcalCommon.HcalDQStandard as standard
StandardSet = standard.StandardSet.clone()
subsystem = standard.subsystem

#	List of FEDs
lFEDs = [x+700 for x in range(32)] + [929, 1118, 1120, 1122]

moduleName = "HcalDigiTask"
#	Modify whatever is in standard importing
StandardSet.moduleParameters.name		= cms.untracked.string(moduleName)
StandardSet.EventsProcessed.path		= cms.untracked.string(
	"%s/%s/" % (subsystem, moduleName))
StandardSet.EventsProcessedPerLS.path	= cms.untracked.string(
	"%s/%s/" % (subsystem, moduleName))

HcalDigiSizeCheck	= StandardSet.Standard2DSubSystem.clone()
HcalDigiSizeCheck.desc = cms.untracked.string("Digi Size Check")
HcalDigiSizeCheck.yaxis.title = cms.untracked.string("Digi Size")
HcalDigiSizeCheck.path = cms.untracked.string("%s/%s" % (subsystem, moduleName))

HcalDigiSizeExp		= StandardSet.Standard2DSubSystem.clone()
HcalDigiSizeExp.desc =	cms.untracked.string("Digi Size Expected(from RAW)")
HcalDigiSizeExp.yaxis.title	= cms.untracked.string("Digi Size")
HcalDigiSizeExp.path = cms.untracked.string("%s/%s" % (subsystem, moduleName))

HcalMap = [StandardSet.Standard2DMap.clone() for x in range(3)]
for i in range(3):
	HcalMap[i].path						= cms.untracked.string("%s/%s/" % (
			subsystem, moduleName))
	HcalMap[i].desc						= cms.untracked.string(
	"HB HE HF Depth%d Occupancy" % (i+1))

HcalProblemsMap = StandardSet.Standard2DMap.clone()
HcalProblemsMap.path = cms.untracked.string("%s/%s/" % (subsystem, moduleName))
HcalProblemsMap.desc = cms.untracked.string(
		"Hcal Problems Rate per LS for Digis")

#	Define some useful strings	
noCutsStr			= " No Cuts Applied "
ZSCutStr			= " DQM ZS Cut (3TS Sum of Nom fC > 20)"

#	Main Task Description
hcalDigiTask = cms.EDAnalyzer(
	moduleName,
	moduleParameters	= StandardSet.moduleParameters,
	MEs					= cms.untracked.PSet(
		EventsProcessed			= StandardSet.EventsProcessed,
		EventsProcessedPerLS	= StandardSet.EventsProcessedPerLS,	

		#	Digi Shape Histograms
		HB_DigiShape			= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB Digi Shape." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)
		),
		HB_DigiShape_ZSCut			= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB Digi Shape." + 
				ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)
		),
		HE_DigiShape			= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE Digi Shape." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)
		),
		HE_DigiShape_ZSCut			= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE Digi Shape." + 
				ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)
		),
		HF_DigiShape				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HF" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Digi Shape." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)
		),
		HF_DigiShape_ZSCut				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HF" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Digi Shape." + ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)
		),
		HO_DigiShape				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO Digi Shape." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)	
		),
		HO_DigiShape_ZSCut				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO Digi Shape." + ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(9.5),
				title	= cms.untracked.string("TS")
			)	
		),

		#	Timing Plots
		HB_Timing				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string(
				"HB Timing (Nominal fC-weighted average)." + ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(500),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10),
				title	= cms.untracked.string("TS(ns-like)")
			)	
		),
		HE_Timing				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string(
				"HE Timing (Nominal fC-weighted average)." + ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(500),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10),
				title	= cms.untracked.string("TS(ns-like)")
			)	
		),
		HF_Timing				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HF" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string(
				"HF Timing (Nominal fC-weighted average)." + ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(200),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(3.5),
				title	= cms.untracked.string("TS(ns-like)")
			)	
		),
		HO_Timing				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string(
				"HO Timing (Nominal fC-weighted average)." + ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(500),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10),
				title	= cms.untracked.string("TS(ns-like)")
			)	
		),
		HB_TimingVSieta				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("PROF"),
			desc	= cms.untracked.string(
				"HB Timing (Nominal fC-weighted average). vs ieta" + 
				ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(83),
				min		= cms.untracked.double(-41.5),
				max		= cms.untracked.double(41.5),
				title	= cms.untracked.string("ieta")
			),
			yaxis	= cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
				nbins	= cms.untracked.int32(500),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10),
				title	= cms.untracked.string("TS(ns-like)")
			)
		),
		HE_TimingVSieta				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("PROF"),
			desc	= cms.untracked.string(
				"HE Timing (Nominal fC-weighted average). vs ieta" + 
				ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(83),
				min		= cms.untracked.double(-41.5),
				max		= cms.untracked.double(41.5),
				title	= cms.untracked.string("ieta")
			),
			yaxis	= cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
				nbins	= cms.untracked.int32(500),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10),
				title	= cms.untracked.string("TS(ns-like)")
			)
		),
		HF_TimingVSieta				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HF" % (subsystem, moduleName)),
			kind	= cms.untracked.string("PROF"),
			desc	= cms.untracked.string(
				"HF Timing (Nominal fC-weighted average). vs ieta" + 
				ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(83),
				min		= cms.untracked.double(-41.5),
				max		= cms.untracked.double(41.5),
				title	= cms.untracked.string("ieta")
			),
			yaxis	= cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
				nbins	= cms.untracked.int32(200),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(5),
				title	= cms.untracked.string("TS(ns-like)")
			)
		),
		HO_TimingVSieta				= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("PROF"),
			desc	= cms.untracked.string(
				"HO Timing (Nominal fC-weighted average). vs ieta" + 
				ZSCutStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(83),
				min		= cms.untracked.double(-41.5),
				max		= cms.untracked.double(41.5),
				title	= cms.untracked.string("ieta")
			),
			yaxis	= cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
				nbins	= cms.untracked.int32(500),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10),
				title	= cms.untracked.string("TS(ns-like)")
			)
		),

		#	ADC Counts Per TS Histos
		HB_ADCCountPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB ADC Counts per 1TS." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(130),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(129.5),
				title	= cms.untracked.string("Unlin. ADC ")
			)	
		),
		HE_ADCCountPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE ADC Counts per 1TS" + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(130),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(129.5),
				title	= cms.untracked.string("Unlin. ADC")
			)	
		),
		HO_ADCCountPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO ADC Counts per 1TS" + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(130),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(129.5),
				title	= cms.untracked.string("Unlin. ADC")
			)	
		),
		HF_ADCCountPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HF" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF ADC Counts per 1TS" + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(130),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(129.5),
				title	= cms.untracked.string("Unlin. ADC")
			)	
		),
		HB_fCPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB fC per 1TS." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(100),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10000),
				title	= cms.untracked.string("Nominal fC")
			)	
		),
		HE_fCPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE fC per 1TS." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(100),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10000),
				title	= cms.untracked.string("Nominal fC")
			)	
		),
		HO_fCPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO fC per 1TS." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(100),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10000),
				title	= cms.untracked.string("Nominal fC")
			)	
		),
		HF_fCPerTS		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HF" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF fC per 1TS." + noCutsStr),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(100),
				min		= cms.untracked.double(0),
				max		= cms.untracked.double(10000),
				title	= cms.untracked.string("Nominal fC")
			)	
		),

		#	Diagnostic Plots
		HB_Presamples		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HB" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB Number of Presamples"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(20),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(20.5),
				title	= cms.untracked.string("# Presamples")
			)	
		),
		HE_Presamples		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HE" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE Number of Presamples"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(20),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(20.5),
				title	= cms.untracked.string("# Presamples")
			)	
		),
		HO_Presamples		= cms.untracked.PSet(
			path	= cms.untracked.string("%s/%s/HO" % (subsystem, moduleName)),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO Number of Presamples"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(20),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(20.5),
				title	= cms.untracked.string("# Presamples")
			)	
		),
		HF_Presamples		= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Number of Presamples"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(20),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(20.5),
				title	= cms.untracked.string("# Presamples")
			)	
		),
		HB_CapId		= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HB" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB Cap ID"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(5),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(4.5),
				title	= cms.untracked.string("Cap ID")
			)	
		),
		HE_CapId		= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE Cap ID"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(5),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(4.5),
				title	= cms.untracked.string("Cap ID")
			)	
		),
		HO_CapId		= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HO" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO Cap ID"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(5),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(4.5),
				title	= cms.untracked.string("Cap ID")
			)	
		),
		HF_CapId		= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Cap ID"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(5),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(4.5),
				title	= cms.untracked.string("Cap ID")
			)	
		),
		HB_bcnOffset	= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HB" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HB Fiber Idle BCN Offset"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(16),
				min		= cms.untracked.double(-8),
				max		= cms.untracked.double(8),
				title	= cms.untracked.string("BCN Offset")
			)	
		),
		HE_bcnOffset	= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HE Fiber Idle BCN Offset"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(16),
				min		= cms.untracked.double(-8),
				max		= cms.untracked.double(8),
				title	= cms.untracked.string("BCN Offset")
			)	
		),
		HO_bcnOffset	= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HO" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HO Fiber Idle BCN Offset"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(16),
				min		= cms.untracked.double(-8),
				max		= cms.untracked.double(8),
				title	= cms.untracked.string("BCN Offset")
			)	
		),
		HF_bcnOffset	= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Fiber Idle BCN Offset"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(16),
				min		= cms.untracked.double(-8),
				max		= cms.untracked.double(8),
				title	= cms.untracked.string("BCN Offset")
			)	
		),
		DigiSize				= HcalDigiSizeCheck,
		DigiSizeExp				= HcalDigiSizeExp,

		#	Timing 2D Profiles
		HBHEHFD1_TimingMap          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("PROF2D"),
            desc    = cms.untracked.string( "HBHEHF D1 Average Timing Map" + 
				ZSCutStr),
            xaxis   = StandardSet.ietaAxis.clone(),
            yaxis   = StandardSet.iphiAxis.clone(),
			zaxis	= cms.untracked.PSet(
				wnbins		= cms.untracked.bool(False),
				min			= cms.untracked.double(-100),
				max			= cms.untracked.double(100),
			)
        ),
		HBHEHFD2_TimingMap          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("PROF2D"),
            desc    = cms.untracked.string( "HBHEHF D2 Average Timing Map" + 
				ZSCutStr),
            xaxis   = StandardSet.ietaAxis.clone(),
            yaxis   = StandardSet.iphiAxis.clone(),
			zaxis	= cms.untracked.PSet(
				wnbins		= cms.untracked.bool(False),
				min			= cms.untracked.double(-100),
				max			= cms.untracked.double(100),
			)
        ),
		HBHEHFD3_TimingMap          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("PROF2D"),
            desc    = cms.untracked.string( "HBHEHF D3 Average Timing Map" + 
				ZSCutStr),
            xaxis   = StandardSet.ietaAxis.clone(),
            yaxis   = StandardSet.iphiAxis.clone(),
			zaxis	= cms.untracked.PSet(
				wnbins		= cms.untracked.bool(False),
				min			= cms.untracked.double(-100),
				max			= cms.untracked.double(100),
			)
        ),
		HOD4_TimingMap          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("PROF2D"),
            desc    = cms.untracked.string( "HO D4 Average Timing Map" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(33),
				min		= cms.untracked.double(-16.5),
				max		= cms.untracked.double(16.5),
				title	= cms.untracked.string("ieta")
			),
            yaxis   = StandardSet.iphiAxis.clone(),
			zaxis	= cms.untracked.PSet(
				wnbins		= cms.untracked.bool(False),
				min			= cms.untracked.double(-100),
				max			= cms.untracked.double(100),
			)
        ),

		#	Occupancy Plots
		HBHEHF_OccupancyMapD1          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("TH2D"),
            desc    = cms.untracked.string( "HBHEHF Occupancy D1" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
				edges   = cms.untracked.bool(False),
				nbins   = cms.untracked.int32(83),
				min             = cms.untracked.double(-41.5),
                max             = cms.untracked.double(41.5),
                title   = cms.untracked.string("ieta")
			),
            yaxis   = cms.untracked.PSet(
				edges   = cms.untracked.bool(False),
                nbins   = cms.untracked.int32(72),
                min     = cms.untracked.double(0.5),
                max      = cms.untracked.double(72.5),
                title   = cms.untracked.string("iphi")
            )
        ),
		HBHEHF_OccupancyMapD2          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("TH2D"),
            desc    = cms.untracked.string( "HBHEHF Occupancy D2" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(83),
				min             = cms.untracked.double(-41.5),
                max             = cms.untracked.double(41.5),
                title   = cms.untracked.string("ieta")
			),
            yaxis   = cms.untracked.PSet(
				edges   = cms.untracked.bool(False),
                nbins   = cms.untracked.int32(72),
                min     = cms.untracked.double(0.5),
                max      = cms.untracked.double(72.5),
                title   = cms.untracked.string("iphi")
            )
        ),
		HBHEHF_OccupancyMapD3          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("TH2D"),
            desc    = cms.untracked.string( "HBHEHF Occupancy D3" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(83),
				min             = cms.untracked.double(-41.5),
                max             = cms.untracked.double(41.5),
                title   = cms.untracked.string("ieta")
			),
            yaxis   = cms.untracked.PSet(
				edges   = cms.untracked.bool(False),
                nbins   = cms.untracked.int32(72),
                min     = cms.untracked.double(0.5),
                max      = cms.untracked.double(72.5),
                title   = cms.untracked.string("iphi")
            )
        ),
		HO_OccupancyMapD4          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s" % moduleName),
            kind    = cms.untracked.string("TH2D"),
            desc    = cms.untracked.string( "HO Occupancy D4" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(33),
				min             = cms.untracked.double(-16.5),
                max             = cms.untracked.double(16.5),
                title   = cms.untracked.string("ieta")
			),
            yaxis   = cms.untracked.PSet(
				edges   = cms.untracked.bool(False),
                nbins   = cms.untracked.int32(72),
                min     = cms.untracked.double(0.5),
                max      = cms.untracked.double(72.5),
                title   = cms.untracked.string("iphi")
            )
        ),
		HB_OccupancyVSls_wZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HB" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HB Occupancy vs LS" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
        ),
		HE_OccupancyVSls_wZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HE" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HE Occupancy vs LS" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
        ),
		HF_OccupancyVSls_wZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HF" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HF Occupancy vs LS" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
        ),
		HO_OccupancyVSls_wZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HO" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HO Occupancy vs LS" + 
				ZSCutStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
        ),
		HB_OccupancyVSls_NoZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HB" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HB Occupancy vs LS" + 
				noCutsStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
		),
		HE_OccupancyVSls_NoZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HE" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HE Occupancy vs LS" + 
				noCutsStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
		),
		HO_OccupancyVSls_NoZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HO" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HO Occupancy vs LS" + 
				noCutsStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
		),
		HF_OccupancyVSls_NoZSCut          = cms.untracked.PSet(
			path    = cms.untracked.string("Hcal/%s/HF" % moduleName),
            kind    = cms.untracked.string("PROF"),
            desc    = cms.untracked.string( "HF Occupancy vs LS" + 
				noCutsStr),
            xaxis   = cms.untracked.PSet(
            edges   = cms.untracked.bool(False),
            nbins   = cms.untracked.int32(1000),
				min     = cms.untracked.double(0),
                max     = cms.untracked.double(1000),
                title   = cms.untracked.string("LS")
			),
            yaxis   = cms.untracked.PSet(
				wnbins	= cms.untracked.bool(True),
                nbins   = cms.untracked.int32(2000),
                min     = cms.untracked.double(0),
                max      = cms.untracked.double(5000),
                title   = cms.untracked.string("# Channels")
            )
		),

		#	Problem Maps and Valid/Invalid 
		ValidInvalid			= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("Valid (0) or Invalid Events(1)"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(2),
				min		= cms.untracked.double(-0.5),
				max		= cms.untracked.double(1.5),
				title	= cms.untracked.string("Criteria")
			)
		),
		ProblemsMap				= HcalProblemsMap,
		ProblemsVsLS = cms.untracked.PSet(
				path	= cms.untracked.string("Hcal/%s" % moduleName),
				kind	= cms.untracked.string("TH1D"),
				desc	= cms.untracked.string("Hcal Problems vs LS"),
				xaxis	= cms.untracked.PSet(
					edges	= cms.untracked.bool(False),
					nbins	= cms.untracked.int32(400),
					min		= cms.untracked.double(0),
					max		= cms.untracked.double(400),
					title	= cms.untracked.string("LS")
				)
		)
	)
)
