
#include "DQM/HcalCommon/interface/HcalMECollection.h"

namespace hcaldqm
{
	MEInfo::MEInfo(edm::ParameterSet const&ps) :
		meps(ps)
	{}

	HcalMECollection::HcalMECollection(edm::ParameterSet const& ps, int debug)
		: _ps(ps), _debug(debug), _wasRetr(false), _wasBooked(false)
	{}

	HcalMECollection::~HcalMECollection()
	{
		forceEmpty();
	}

	//	Force the release of the contents of the MECollection
	void HcalMECollection::forceEmpty()
	{
		//	Cannot delete the MEMap, have to release all the MEs
		for (MEMap::iterator it=_meMap.begin();
				it!=_meMap.end(); ++it)
		{
			MEMap::auto_type ptr = _meMap.release(it);
			ptr.release();
		}
	}

	//	for booking Monitor Elements based on PSet
	void HcalMECollection::book(DQMStore::IBooker &ib)
	{
		if (_wasBooked==true)
		{
			this->debug("Trying to Do Double Booking!!!");
			return;
		}

		std::vector<std::string> const& meNames(_ps.getParameterNames());
		for (std::vector<std::string>::const_iterator it=meNames.begin();
				it!=meNames.end(); ++it)
		{
	 		std::string meName = *it;

			//	parse VPSet differently
			if (this->isVPSet(meName))
			{
				edm::VParameterSet const& psv = _ps.getUntrackedParameterSetVector(*it);
				for (edm::VParameterSet::const_iterator jt=psv.begin();
						jt!=psv.end(); ++jt)
				{
					MEInfo meinfo(*jt);
					std::string name = jt->getUntrackedParameter<std::string>("name");
					meinfo.setName(name);
					doBook(ib, meinfo);
				}
			}
			else
			{
				MEInfo meinfo(_ps.getUntrackedParameterSet(*it)); 
				meinfo.setName(meName);
				doBook(ib, meinfo);
			}
		}

		_wasBooked = true;
	}

	void HcalMECollection::doBook(DQMStore::IBooker &ib,
			MEInfo const& info)
	{
		std::string path = info.getPS().getUntrackedParameter<std::string>(
				"path");
		std::string kind = info.getPS().getUntrackedParameter<std::string>(
				"kind");
		bool toUpdate = false;
		if (info.getPS().exists("toUpdate"))
			toUpdate = info.getPS().getUntrackedParameter<bool>("toUpdate");
		if (toUpdate)
			_namesToUpdate.push_back(info.getName());
		MonitorElement *me;
		std::string period;
		if (info.getPS().exists("reset"))
		{
			period = info.getPS().getUntrackedParameter<std::string>("reset");
			if (period=="EVENT")
				_namesResetEv.push_back(info.getName());
			else if (period=="LS")
				_namesResetLS.push_back(info.getName());
		}

		debug("Starting Booking " + path + " " + info.getName());
		ib.setCurrentFolder(path);
		if  (kind=="INT")
//			case MonitorElement::DQM_KIND_INT:
			me = ib.bookInt(info.getName());
		else if (kind=="REAL")
//			case MonitorElement::DQM_KIND_REAL:
			me = ib.bookFloat(info.getName());
		else if (kind=="STRING")
//			case MonitorElement::DQM_KIND_STRING :
			me = ib.bookString(path, info.getName());
		else if (kind=="TH1D")
//			case MonitorElement::DQM_KIND_TH1D:
			me = this->create1D(ib, info);
		else if (kind=="TH2D")
//			case MonitorElement::DQM_KIND_TH2D:
			me = this->create2D(ib, info);
		else if (kind=="PROF")
//			case MonitorElement::DQM_KIND_TPROF:
			me = this->createProf(ib, info);
		else if (kind=="PROF2D")
//			case MonitorElement::DQM_KIND_TPROF2D:
			me = this->createProf2D(ib,info);
		else
			me = NULL;

		std::string key = info.getName();
		debug("Finished Booking " + path + " " + key);
		std::pair<MEMap::iterator, bool> r = _meMap.insert(key, me);
		if (r.second)
			return;

		//	If false, then it means we attempting double booking
		this->debug("Double Booking!!!");
		return;
	}

	//	for retirieving Monitor Elements based on PSet
	//	Right now done every time before retrieving MEs
	void HcalMECollection::retrieve(DQMStore::IGetter &ig)
	{
		if (_wasRetr)
			return;

		std::vector<std::string> const& meNames(_ps.getParameterNames());
		for (std::vector<std::string>::const_iterator it=meNames.begin();
				it!=meNames.end(); ++it)
		{
			std::string meName = *it;
			MEInfo meinfo(_ps.getUntrackedParameterSet(*it));
			meinfo.setName(meName);
			doRetrieve(ig, meinfo);
		}
		
		_wasRetr = true;
		return;
	}

	void HcalMECollection::doRetrieve(DQMStore::IGetter &ig, MEInfo const& info)
	{
		std::string path = info.getPS().getUntrackedParameter<std::string>(
				"path");
		MonitorElement *me = ig.get(path+info.getName());

		std::string key = info.getName();
		debug(key);
		std::pair<MEMap::iterator, bool> r = _meMap.insert(key, me);
		if (r.second)
			return;
	}

	MonitorElement& HcalMECollection::operator[](std::string name)
	{
		this->debug("Accessing: " + name);
		return _meMap[name];
	}
	
	MonitorElement* HcalMECollection::create1D(DQMStore::IBooker &ib, 
			MEInfo const& info)
	{
		edm::ParameterSet const& axisps = 
			info.getPS().getUntrackedParameterSet("xaxis");
		std::string desc = info.getPS().getUntrackedParameter<std::string>(
				"desc");
		MEAxis xaxis;
		xaxis.edges = GETPAR(axisps, bool, "edges");
		xaxis.nbins = GETPAR(axisps, int, "nbins");
		xaxis.title = GETPAR(axisps, std::string, "title");
		MonitorElement *me = NULL;
		if (!xaxis.edges)
		{
			xaxis.min = GETPAR(axisps, double, "min");
			xaxis.max = GETPAR(axisps, double, "max");
			me = ib.book1D(info.getName(), desc, xaxis.nbins, 
					xaxis.min, xaxis.max);
		}
		else
		{
			xaxis.bins = 
				axisps.getUntrackedParameter<std::vector<double> >("bins").data();
			me = ib.book1D(info.getName(), desc, xaxis.nbins, 
					(float const*)xaxis.bins);
		}
		
		me->setAxisTitle(xaxis.title);
		return me;
	}

	MonitorElement* HcalMECollection::createProf2D(DQMStore::IBooker &ib, 
			MEInfo const& info)
	{
		edm::ParameterSet const& xaxisps = 
			info.getPS().getUntrackedParameterSet("xaxis");
		edm::ParameterSet const& yaxisps = 
			info.getPS().getUntrackedParameterSet("yaxis");
		edm::ParameterSet const& zaxisps = 
			info.getPS().getUntrackedParameterSet("zaxis");
		std::string desc = info.getPS().getUntrackedParameter<std::string>(
				"desc");

		MEAxis xaxis, yaxis, zaxis;
		xaxis.nbins = GETPAR(xaxisps, int, "nbins");
		xaxis.min = GETPAR(xaxisps, double, "min");
		xaxis.max = GETPAR(xaxisps, double, "max");
		xaxis.title = GETPAR(xaxisps, std::string, "title");
		yaxis.nbins = GETPAR(yaxisps, int, "nbins");
		yaxis.min = GETPAR(yaxisps, double, "min");
		yaxis.max = GETPAR(yaxisps, double, "max");
		yaxis.title = GETPAR(yaxisps, std::string, "title");
		zaxis.min = GETPAR(zaxisps, double, "min");
		zaxis.max = GETPAR(zaxisps, double, "max");
		zaxis.wnbins = GETPAR(zaxisps, bool, "wnbins");
		MonitorElement *me = NULL;

		if (zaxis.wnbins)
		{
			// create 2D Profile with z-bins explicitly
			zaxis.nbins = GETPAR(zaxisps, int, "nbins");
			me = ib.bookProfile2D(info.getName(), desc, xaxis.nbins,
					xaxis.min, xaxis.max, yaxis.nbins, yaxis.min, yaxis.max,
					zaxis.nbins, zaxis.min, zaxis.max);
		}
		else
			me = ib.bookProfile2D(info.getName(), desc, xaxis.nbins,
					xaxis.min, xaxis.max, yaxis.nbins, yaxis.min, yaxis.max,
					zaxis.min, zaxis.max);

		me->setAxisTitle(xaxis.title, 1);
		me->setAxisTitle(yaxis.title, 2);
		return me;
	}

	MonitorElement* HcalMECollection::createProf(DQMStore::IBooker &ib, 
			MEInfo const& info)
	{	
		edm::ParameterSet const &xaxisps = 
			info.getPS().getUntrackedParameterSet("xaxis");
		edm::ParameterSet const &yaxisps = 
			info.getPS().getUntrackedParameterSet("yaxis");
		std::string desc = info.getPS().getUntrackedParameter<std::string>(
				"desc");

		MEAxis xaxis, yaxis;
		xaxis.edges = GETPAR(xaxisps, bool, "edges");
		xaxis.nbins = GETPAR(xaxisps, int, "nbins");
		yaxis.wnbins = GETPAR(yaxisps, bool, "wnbins");
		yaxis.edges = false;
		xaxis.title = GETPAR(xaxisps, std::string, "title");
		yaxis.title = GETPAR(yaxisps, std::string, "title");
		MonitorElement *me = NULL;

		if (!xaxis.edges && yaxis.wnbins)
		{
			xaxis.min = GETPAR(xaxisps, double, "min");
			xaxis.max = GETPAR(xaxisps, double, "max");
			yaxis.min = GETPAR(yaxisps, double, "min");
			yaxis.max = GETPAR(yaxisps, double, "max");
			yaxis.nbins = GETPAR(yaxisps,int, "nbins");
			me = ib.bookProfile(info.getName(), desc, xaxis.nbins, 
					xaxis.min, xaxis.max, yaxis.nbins, yaxis.min, yaxis.max);
		}
		else if (!xaxis.edges && !yaxis.wnbins)
		{
			xaxis.min = GETPAR(xaxisps, double, "min");
			xaxis.max = GETPAR(xaxisps, double, "max");
			yaxis.min = GETPAR(yaxisps, double, "min");
			yaxis.max = GETPAR(yaxisps, double, "max");
			me = ib.bookProfile(info.getName(), desc, xaxis.nbins, xaxis.min,
					xaxis.max, yaxis.min, yaxis.max);
		}
		else if (xaxis.edges && yaxis.wnbins)
		{
			xaxis.bins = 
				xaxisps.getUntrackedParameter<std::vector<double> >(
						"bins").data();
			yaxis.nbins = GETPAR(yaxisps,int, "nbins");
			yaxis.min = GETPAR(yaxisps, double, "min");
			yaxis.max = GETPAR(yaxisps, double, "max");
			me = ib.bookProfile(info.getName(), desc, xaxis.nbins, 
					xaxis.bins,	yaxis.nbins, yaxis.min, yaxis.max);
		}
		else if (xaxis.edges && !yaxis.wnbins)
		{
			xaxis.bins = 
				xaxisps.getUntrackedParameter<std::vector<double> >(
						"bins").data();
			yaxis.max = GETPAR(yaxisps, double, "max");
			yaxis.min = GETPAR(yaxisps, double, "min");
			me = ib.bookProfile(info.getName(), desc, xaxis.nbins, 
					xaxis.bins,	yaxis.min, yaxis.max);
		}

		me->setAxisTitle(xaxis.title, 1);
		me->setAxisTitle(yaxis.title, 2);
		return me;
	}

	MonitorElement* HcalMECollection::create2D(DQMStore::IBooker &ib, 
			MEInfo const& info)
	{
		edm::ParameterSet const &xaxisps = 
			info.getPS().getUntrackedParameterSet("xaxis");
		edm::ParameterSet const &yaxisps = 
			info.getPS().getUntrackedParameterSet("yaxis");
		std::string desc = info.getPS().getUntrackedParameter<std::string>(
				"desc");

		MEAxis xaxis, yaxis;
		xaxis.edges = GETPAR(xaxisps, bool, "edges");
		xaxis.nbins = GETPAR(xaxisps, int, "nbins");
		yaxis.edges = GETPAR(yaxisps, bool, "edges");
		yaxis.nbins = GETPAR(yaxisps, int, "nbins");
		xaxis.wnbins = false;
		yaxis.wnbins = false;
		xaxis.title = GETPAR(xaxisps, std::string, "title");
		yaxis.title = GETPAR(yaxisps, std::string, "title");
		MonitorElement *me = NULL;

		if (!yaxis.edges && !xaxis.edges)
		{		
			xaxis.min = GETPAR(xaxisps, double, "min");
			xaxis.max = GETPAR(xaxisps, double, "max");
			yaxis.min = GETPAR(yaxisps, double, "min");
			yaxis.max = GETPAR(yaxisps, double, "max");
			me = ib.book2D(info.getName(), desc, xaxis.nbins, xaxis.min, 
					xaxis.max, yaxis.nbins, yaxis.min, yaxis.max);
		}
		else if (yaxis.edges && xaxis.edges)
		{
			xaxis.bins = 
				xaxisps.getUntrackedParameter<std::vector<double> >(
						"bins").data();
			yaxis.bins = 
				yaxisps.getUntrackedParameter<std::vector<double> >(
						"bins").data();
			me = ib.book2D(info.getName(), desc, xaxis.nbins, 
					(const float*)xaxis.bins, yaxis.nbins, 
					(const float*)yaxis.bins);
		}
		
		me->setAxisTitle(xaxis.title, 1);
		me->setAxisTitle(yaxis.title, 2);
		return me;
	}

	//	reset
	//	periodflag == 0 for Event and 1 for LS
	void HcalMECollection::reset(int const periodflag)
	{
		if (periodflag==0)
		{
			//	Event Reset
			for (std::vector<std::string>::const_iterator 
					it=_namesResetEv.begin(); it!=_namesResetEv.end(); ++it)
			{
				MonitorElement::Kind kind = _meMap[*it].kind();
				if (kind==MonitorElement::DQM_KIND_INT || 
						kind==MonitorElement::DQM_KIND_REAL)
					_meMap[*it].Fill(0);
				else if (kind==MonitorElement::DQM_KIND_STRING)
					continue;
//					_meMap[*it].Fill("");
				else
					_meMap[*it].Reset();
			}
		}
		else if (periodflag==1)
		{
			//	LS Reset
			for (std::vector<std::string>::const_iterator
					it=_namesResetLS.begin(); it!=_namesResetLS.end(); ++it)
			{
				MonitorElement::Kind kind = _meMap[*it].kind();
				if (kind==MonitorElement::DQM_KIND_INT || 
						kind==MonitorElement::DQM_KIND_REAL)
					_meMap[*it].Fill(0);
				else if (kind==MonitorElement::DQM_KIND_STRING)
					continue;
//					_meMap[*it].Fill("");
				else
					_meMap[*it].Reset();
			}
		}
	}

	//	update all the MEs
	void HcalMECollection::update()
	{
		for (std::vector<std::string>::const_iterator it=_namesToUpdate.begin();
				it!=_namesToUpdate.end(); ++it)
			_meMap[*it].update();
	}
}







