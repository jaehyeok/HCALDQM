#ifndef HCALDQUTILS_H
#define HCALDQUTILS_H

/*	
 *	file:				HcalDigiTask.h
 *	Author:				Viktor Khristenko
 *	Start Date:			03/04/2015
 *
 *	TODO:
 *		1) Other utilities???	
 */

#include "DQM/HcalCommon/interface/HcalCommonHeaders.h"

#include <vector>
#include <string>
#include "boost/ptr_container/ptr_map.hpp"
#include "boost/container/map.hpp"

namespace hcaldqm
{

	//	a struct of labels
	struct Labels
	{
		Labels(edm::ParameterSet const&);		
		edm::InputTag& operator[](std::string s) 
		{
			return _labels[s];
		}

		typedef boost::container::map<std::string, edm::InputTag> LabelMap;
		LabelMap _labels;
	};

	/*
	 *	Namespace containing all the Math Stuff.
	 */
	namespace math
	{
		//	Copmute a TS with max nominal fC
		template<typename Hit>
		int maxTS(Hit const& hit, double ped=0)
		{	
			int maxT = -1;
			double maxQ = -1;
			for (int i=0; i<hit.size(); i++)
				if ((hit.sample(i).nominal_fC()-ped)>maxQ)
				{
					maxQ = hit.sample(i).nominal_fC()-ped;
					maxT=i;
				}

			return maxT;
		}

		//	Compute the nominal_fC-weighted Time average
		template<typename Hit>
		double aveT(Hit const& hit, double ped=0)
		{
			double sumQ = 0;
			double sumQT = 0;
			double ave = 0;
			for (int i=0; i<hit.size(); i++)
			{
				sumQ+=hit.sample(i).nominal_fC()-ped;
				sumQT+=(i+1)*(hit.sample(i).nominal_fC()-ped);
			}
			
			ave = sumQT/sumQ - 1;
			return ave;
		}

		//	Compute the Sum over the digi
		template<typename Hit>
		double sum(Hit const& hit, int i, int j, double ped=0)
		{
			if (i<0 || j>=hit.size())
				return -1;

			double sumQ = 0;
			for (int ii=i; ii<=j; ii++)
				sumQ+=hit.sample(ii).nominal_fC()-ped;

			return sumQ;
		}
	}
}

#endif








