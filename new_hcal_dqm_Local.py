#-------------------------------------
#	Hcal DQM Application using New DQM Sources/Clients
#	Description: For Local Use(a la DetDiag)
#-------------------------------------

#-------------------------------------
#	Standard Python Imports
#-------------------------------------
import os, sys, socket, string

#-------------------------------------
#	Input Options
#-------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing()

options.register(
	'inputFiles',
	"file:inputFile.root", #default
	VarParsing.VarParsing.multiplicity.list,
	VarParsing.VarParsing.varType.string,
	"Input Files"
)

options.register(
	'processEvents',
	-1,
	VarParsing.VarParsing.multiplicity.singleton,
	VarParsing.VarParsing.varType.int,
	"Number of Events to process"
)

options.parseArguments()

#-------------------------------------
#	Standard CMSSW Imports/Definitions
#-------------------------------------
import FWCore.ParameterSet.Config as cms
process			= cms.Process('HCALDQM')
subsystem		= 'Hcal'
cmssw			= os.getenv("CMSSW_VERSION").split("_")
debugstr		= "### HcalDQM::cfg::DEBUG: "
warnstr			= "### HcalDQM::cfg::WARN: "
errorstr		= "### HcalDQM::cfg::ERROR:"
useOfflineGT	= True
local			= True
useMap			= True

print debugstr, "Input Files= ", options.inputFiles
print debugstr, "Run over #events=", options.processEvents


#-------------------------------------
#	Central DQM Stuff imports
#-------------------------------------
if local:
	process.source = cms.Source("HcalTBSource",
		fileNames = cms.untracked.vstring(options.inputFiles)
	)
	process.maxEvents = cms.untracked.PSet(
			input = cms.untracked.int32(options.processEvents)
	)
else:
	print errorstr + "There is an error with the Source. Exiting..."
	sys.exit(1)
process.load('DQMServices.Components.DQMEnvironment_cfi')
process.load('DQMServices.Core.DQMStore_cfi')

#-------------------------------------
#	DQM Customization
#-------------------------------------
process.DQM = cms.Service(
	"DQM",
	debug = cms.untracked.bool(False),
	publishFrequency = cms.untracked.double(1.0),
	collectorPort = cms.untracked.int32(8061),
	collectorHost = cms.untracked.string('hcaldqm03.cms'),
	filter = cms.untracked.string('')
)
process.dqmSaver.convention = 'Online'
process.dqmSaver.referenceHandling = 'all'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
process.dqmSaver.saveByLumiSection = 10
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = False
process.DQMStore.verbose = 10
process.dqmEnv.subSystemFolder = 'Hcal'

#-------------------------------------
#	CMSSW/Hcal non-DQM Related Module import
#-------------------------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")
process.load("RecoLocalCalo.Configuration.hcalLocalReco_cff")
process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("L1Trigger.Configuration.L1DummyConfig_cff")
process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi")
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

#-------------------------------------
#	CMSSW/Hcal non-DQM Related Module Settings
#	-> GlobalTag
#	-> Generic Input tag for the Raw Collection
#	-> cmssw version
#	-> Turn off default blocking of dead channels from rechit collection
#	-> Drop Channel Status Bits (had benn 'HcalCellOff', "HcalCellDead")
#	-> For Trigger Primitives
#	-> L1 GT setting
#	-> Rename the hbheprereco to hbhereco
#-------------------------------------
process.GlobalTag.globaltag = 'GR_E_V42::All'
cmssw			= os.getenv("CMSSW_VERSION").split("_")
rawTag			= cms.InputTag("rawDataCollector")
process.essourceSev = cms.ESSource(
		"EmptyESSource",
		recordName		= cms.string("HcalSeverityLevelComputerRcd"),
		firstValid		= cms.vuint32(1),
		iovIsRunNotTime	= cms.bool(True)
)
process.hcalRecAlgos.DropChannelStatusBits = cms.vstring('')
process.valHcalTriggerPrimitiveDigis = \
		process.simHcalTriggerPrimitiveDigis.clone()
process.valHcalTriggerPrimitiveDigis.inputLabel = \
		cms.VInputTag("hcalDigis", 'hcalDigis')
process.valHcalTriggerPrimitiveDigis.FrontEndFormatError = \
		cms.bool(True)
process.HcalTPGCoderULUT.LUTGenerationMode = cms.bool(False)
process.valHcalTriggerPrimitiveDigis.FG_threshold = cms.uint32(2)
process.valHcalTriggerPrimitiveDigis.InputTagFEDRaw = rawTag
process.l1GtUnpack.DaqGtInputTag = rawTag
process.hbhereco = process.hbheprereco.clone()

#-------------------------------------
#	Hcal DQM Tasks and Clients import
#-------------------------------------
process.load("DQM.HcalTasks.HcalDigiTask")
process.load("DQM.HcalTasks.HcalDeadCellTask")
process.load("DQM.HcalTasks.HcalHotCellTask")
process.load("DQM.HcalTasks.HcalLEDTask")
process.load("DQM.HcalTasks.HcalLaserTask")
process.load("DQM.HcalTasks.HcalNoiseTask")
process.load("DQM.HcalTasks.HcalPedestalTask")
process.load("DQM.HcalTasks.HcalRawTask")
process.load("DQM.HcalTasks.HcalRecHitTask")
process.load("DQM.HcalTasks.HcalTPTask")
process.load("DQM.HcalTasks.HcalTimingTask")
process.load("DQM.HcalTasks.HcaluTCATask")
process.load("DQM.HcalTasks.HcalPhaseScanTask")

#-------------------------------------
#	To force using uTCA
#	Will not be here for Online DQM
#-------------------------------------
if useMap:
	process.es_pool = cms.ESSource("PoolDBESSource",
			process.CondDBSetup,
			timetype = cms.string('runnumber'),
			toGet = cms.VPSet(
				cms.PSet(
					record = cms.string(
						"HcalElectronicsMapRcd"
					),
					tag = cms.string(
						"HcalElectronicsMap_v7.00_offline"					  )
				)
			),
			connect = cms.string(
				'frontier://FrontierProd/CMS_CONDITIONS'),
			authenticationMethod = cms.untracked.uint32(0)
	)	
	process.es_prefer_es_pool = cms.ESPrefer('PoolDBESSource', 'es_pool')

#-------------------------------------
#	To have vme Digis as a separate collection
#-------------------------------------
process.vmeDigis = process.hcalDigis.clone()
process.vmeDigis.FEDs = cms.untracked.vint32(719, 720)

#-------------------------------------
#	Hcal DQM Tasks Sequence Definition
#-------------------------------------
process.tasksSequence = cms.Sequence(
		process.hcalDigiTask
		*process.hcalDeadCellTask
		*process.hcalHotCellTask
		*process.hcalLEDTask
		*process.hcalLaserTask
		*process.hcalNoiseTask
		*process.hcalPedestalTask
)

#-------------------------------------
#	Some Settings for Local(a la DetDiag)
#-------------------------------------
process.hcalDigis.InputLabel = cms.InputTag("source")

#-------------------------------------
#	Execution Sequence Definition
#-------------------------------------
process.p = cms.Path(
					process.hcalDigis
					*process.tasksSequence
                    #*process.qTester
                    *process.dqmEnv
                    *process.dqmSaver)

#-------------------------------------
#	Scheduling
#-------------------------------------
process.options = cms.untracked.PSet(
		Rethrow = cms.untracked.vstring(
			"ProductNotFound",
			"TooManyProducts",
			"TooFewProducts"
		)
)