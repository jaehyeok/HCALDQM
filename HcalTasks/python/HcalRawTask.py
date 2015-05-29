import FWCore.ParameterSet.Config as cms 

import DQM.HcalCommon.HcalDQStandard as standard
StandardSet = standard.StandardSet.clone()

#	List of FEDs
lFEDs = [x+700 for x in range(32)] + [929, 1118, 1120, 1122]

moduleName = "HcalRawTask"
#	Modify whatever is in StandardSet importing
StandardSet.moduleParameters.name		= cms.untracked.string(moduleName)
StandardSet.EventsProcessed.path		= cms.untracked.string(
	"Hcal/%s/" % moduleName)
StandardSet.EventsProcessedPerLS.path	= cms.untracked.string(
	"Hcal/%s/" % moduleName)
StandardSet.Standard2DMap.path			= cms.untracked.string(
	"Hcal/%s/" % moduleName)
StandardSet.Standard2DMap.desc			= cms.untracked.string(
	"Some Raw Task 2D Map")

HcalProblems = StandardSet.Standard2DMap.clone()
HcalProblems.path = cms.untracked.string("Hcal/%s" % moduleName)
HcalProblems.desc = cms.untracked.string(
		"Hcal Problems Rate per LS for RecHits")

#	Define some useful strings and doubles
cutstr_eg2		= " DQM Energy Cut (E > 2GeV) "
nocutstr		= " No Cuts Applied "

#	Main Task Description
hcalRawTask = cms.EDAnalyzer(
	moduleName,
	moduleParameters	= StandardSet.moduleParameters,
	MEs					= cms.untracked.PSet(
		EventsProcessed			= StandardSet.EventsProcessed,
		EventsProcessedPerLS	= StandardSet.EventsProcessedPerLS,
	
	)
)
