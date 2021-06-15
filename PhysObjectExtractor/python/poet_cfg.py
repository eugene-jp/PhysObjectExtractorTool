import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

process = cms.Process("POET")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "WARNING"
process.MessageLogger.categories.append("POET")
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit=cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True))


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/SingleElectron/AOD/12Oct2013-v1/10000/1045436C-1240-E311-851B-003048D2BF1C.root'
#	'file:/playground/002F62E1-B53D-E311-A49F-003048F1B950.root'
    )
)

#needed to get the actual prescale values used from the global tag
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db')
#process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'

#Here, you can enter the desired input tag, corresponding to each container, In addition, you can add more containers.
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideRecoDataTable
process.myevents = cms.EDAnalyzer('EventAnalyzer')	                             
process.myelectrons = cms.EDAnalyzer('ElectronAnalyzer',
				     InputCollection = cms.InputTag("gsfElectrons")
				    )
process.mymuons = cms.EDAnalyzer('MuonAnalyzer',
				InputCollection = cms.InputTag("muons")
				)

process.TFileService = cms.Service(
    "TFileService", fileName=cms.string("myoutput.root"))


process.p = cms.Path(process.myevents+process.myelectrons+process.mymuons)