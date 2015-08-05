import numpy as np
import pandas as pd

import json
import requests
import logging
import time

from team_player_ids import *
from NbaStatsPlayer import NbaStatsPlayer

URL_SHOT_LOG = """http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID={playerId}&Season={season}&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="""

logging.basicConfig(filename='log_NBA_Shot_Chart.log', level=logging.INFO,
		format='%(asctime)s | %(levelname)s | %(message)s',
		datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


def extract_date_from_matchup(matchup):
    return datetime.datetime.strptime(matchup[:12], "%b %d, %Y").date()

def extract_oppenent_from_matchup(matchup):
	away = '@' in matchup
	if away:
		opp = matchup.split(' ')[-3]
	else:
		opp = matchup.split(' ')[-1]
	return opp

seasons = ['2014-15', '2013-14']
for season in seasons:
	DF_FINAL = pd.DataFrame()
	for ii, p in enumerate(players):
		if ii%50 == 0:
			print ii, p['firstName'] + ' ' + p['lastName']
		logger.info(p['playerId'])
		playerStat = NbaStatsPlayer(p['playerId'], season)
		playerStat.get_shots_and_fill_df()
		if playerStat.has_data:
			DF_FINAL = pd.concat([DF_FINAL, playerStat.dfShots])
			time.sleep(5)
		else:
			logger.info('{pId}: {player} has no data.'.format(pId = p['playerId'], player = p['firstName'] + ' ' + p['lastName']))
			time.sleep(1)
	try:
		DF_FINAL.insert(2, 'dt', DF_FINAL.MATCHUP.apply(lambda m: extract_date_from_matchup(m)))
		DF_FINAL.insert(4, 'opp', DF_FINAL.MATCHUP.apply(lambda m: extract_oppenent_from_matchup(m)))
		DF_FINAL['season'] =  season.replace('-', '')
	except:
		pass
	finally:
		DF_FINAL.to_csv('shot_chart{season}.csv'.format(season = season.replace('-', '')), index = False)
		print '{season} completed.'.format(season = season)
		logger.info('{season} completed.'.format(season = season))
