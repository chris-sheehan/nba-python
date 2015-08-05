import numpy as np
import pandas as pd
import json
import requests

from NbaStats import NbaStats

####
# Add Error Handling for response codes.
####
class NbaStatsReboundLog(NbaStats):
	def __init__(self, *args, **kwargs):
		super(NbaStatsReboundLog, self).__init__(*args, **kwargs)
		self.__name__ = 'ReboundLog'
		self.url_template = "http://stats.nba.com/stats/playerdashptreboundlogs?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID={playerId}&Season={season}&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="
