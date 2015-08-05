import numpy as np
import pandas as pd

import json
import requests
import logging
import time

import sys
sys.path.append('/home/chris/Desktop/nba2015/nba-python/data')
from team_player_ids import *

from NbaStats import NbaStats
from NbaStatsShotDetail import NbaStatsShotDetail
from NbaStatsShotLog import NbaStatsShotLog
# from NbaStatsReboundDetail import NbaStatsReboundDetail
from NbaStatsReboundLog import NbaStatsReboundLog


logging.basicConfig(filename='log_NBA_Shot_Chart.log', level=logging.INFO,
		format='%(asctime)s | %(levelname)s | %(message)s',
		datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

SEASONS = ['2014-15', '2013-14']

def extract_date_from_matchup(matchup):
    return datetime.datetime.strptime(matchup[:12], "%b %d, %Y").date()

def extract_oppenent_from_matchup(matchup):
	away = '@' in matchup
	if away:
		opp = matchup.split(' ')[-3]
	else:
		opp = matchup.split(' ')[-1]
	return opp


def create_statgrabber(grabber, playerId, season):
	stats = grabber(playerId, season)
	return stats

if __name__ == '__main__':

for season in SEASONS:
	statgrabbers = [NbaStatsShotDetail, NbaStatsReboundLog]
	for sg in statgrabbers:
		logger.info('--------', sg.__name__, ' starting. --------')
		df_agg = pd.DataFrame()
		for p in players:
			logger.info(p['playerId'])
			psl = sg(p['playerId'], season)
			psl.get_data_and_fill_df()
			df_agg = pd.concat([df_agg, psl.df])
			time.sleep(4)

		if not df_agg.empty:
			if 'MATCHUP' in df_agg.columns:
				df_agg.insert(2, 'dt', df_agg.MATCHUP.apply(lambda m: extract_date_from_matchup(m)))
				df_agg.insert(4, 'opp', df_agg.MATCHUP.apply(lambda m: extract_oppenent_from_matchup(m)))
			df_agg['season'] =  season.replace('-', '')
		df_agg.to_csv('{stat_name}{season}.csv'.format(stat_name = psl.__name__, season = season.replace('-', '')), index = False)
