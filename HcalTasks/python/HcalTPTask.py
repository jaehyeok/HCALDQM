import FWCore.ParameterSet.Config as cms 

import DQM.HcalCommon.HcalDQStandard as standard
StandardSet = standard.StandardSet.clone()

#	List of FEDs
lFEDs = [x+700 for x in range(32)] + [929, 1118, 1120, 1122]

moduleName = "HcalTPTask"
#	Modify whatever is in StandardSet importing
StandardSet.moduleParameters.name		= cms.untracked.string(moduleName)
StandardSet.EventsProcessed.path		= cms.untracked.string(
	"Hcal/%s/" % moduleName)
StandardSet.EventsProcessedPerLS.path	= cms.untracked.string(
	"Hcal/%s/" % moduleName)
StandardSet.Standard2DMap.path			= cms.untracked.string(
	"Hcal/%s/" % moduleName)
StandardSet.Standard2DMap.desc			= cms.untracked.string(
	"TP Digi Size")

#	Main Task Description
hcalTPTask = cms.EDAnalyzer(
	moduleName,
	moduleParameters	= StandardSet.moduleParameters,
	MEs					= cms.untracked.PSet(
		EventsProcessed			= StandardSet.EventsProcessed,
		EventsProcessedPerLS	= StandardSet.EventsProcessedPerLS,
		
		#	???????????????????????????????????????????//
		#	Do we need these 2 histos???
		#	???????????????????????????????????????????//
		HBHE_EtShape_Data				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHE Compressed Et Shape Data"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("TS")
			)
		),
		HBHE_EtShape_Emul				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHE Compressed Et Shape Emulator"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("TS")
			)
		),
		HF_EtShape_Data				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Compressed Et Shape Data"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("TS")
			)
		),
		HF_EtShape_Emul				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Compressed Et Shape Emulator"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("TS")
			)
		),

		#------------------------------------------------------
		#	SOI Et and FG
		#------------------------------------------------------
		HBHE_SOI_Et_Data				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHE Compressed Et Distribution Data"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(256),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(256.),
				title	= cms.untracked.string("SOI Compressed Et")
			)
		),
		HBHE_SOI_Et_Emul				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string(
				"HBHE Compressed Et Distribution Emulator"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(256),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(256.),
				title	= cms.untracked.string("SOI Compressed Et")
			)
		),
		HF_SOI_Et_Data				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Compressed Et Distribution Data"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(256),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(256.),
				title	= cms.untracked.string("SOI Compressed Et")
			)
		),
		HF_SOI_Et_Emul				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string(
				"HF Compressed Et Distribution Emulator"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(256),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(256.),
				title	= cms.untracked.string("SOI Compressed Et")
			)
		),

		#------------------------------------------------------
		#	Number of Presamples
		#------------------------------------------------------
		HF_Presamples_Data				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Number of Presamples Data"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("# Presamples")
			)
		),
		HBHE_Presamples_Data				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHE Number of Presamples Data"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("# Presamples")
			)
		),
		HF_Presamples_Emul				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF Number of Presamples Emul"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("# Presamples")
			)
		),
		HBHE_Presamples_Emul				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHE Number of Presamples Emul"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(10),
				min		= cms.untracked.double(0.),
				max		= cms.untracked.double(10.),
				title	= cms.untracked.string("# Presamples")
			)
		),


		#------------------------------------------------------
		#	TP Digi Size
		#------------------------------------------------------
		HBHEHF_TPSize			= StandardSet.Standard2DMap 

		#------------------------------------------------------
		#	Occupancy Maps
		#------------------------------------------------------
		HBHEHF_TPOccupancyVSieta				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHEHF TP Occupancy vs ieta"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(83),
				min		= cms.untracked.double(-41.5),
				max		= cms.untracked.double(41.5),
				title	= cms.untracked.string("ieta")
			)
		), 
		HBHEHF_TPOccupancyVSiphi				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHEHF TP Occupancy vs iphi"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(72),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(72.5),
				title	= cms.untracked.string("iphi")
			)
		), 
		HF_TPOccupancyVSiphi				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HF" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HF TP Occupancy vs iphi"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(72),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(72.5),
				title	= cms.untracked.string("iphi")
			)
		), 
		HBHE_TPOccupancyVSiphi				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s/HBHE" % moduleName),
			kind	= cms.untracked.string("TH1D"),
			desc	= cms.untracked.string("HBHE TP Occupancy vs iphi"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(72),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(72.5),
				title	= cms.untracked.string("iphi")
			)
		), 
		
		HBHEHF_TPOccupancy				= cms.untracked.PSet(
			path	= cms.untracked.string("Hcal/%s" % moduleName),
			kind	= cms.untracked.string("TH2D"),
			desc	= cms.untracked.string("HBHEHF TP Occupancy"),
			xaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(83),
				min		= cms.untracked.double(-41.5),
				max		= cms.untracked.double(41.5),
				title	= cms.untracked.string("ieta")
			),
			yaxis	= cms.untracked.PSet(
				edges	= cms.untracked.bool(False),
				nbins	= cms.untracked.int32(72),
				min		= cms.untracked.double(0.5),
				max		= cms.untracked.double(72.5),
				title	= cms.untracked.string("iphi")
			)
		), 
	)
)
