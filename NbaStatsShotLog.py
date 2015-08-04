import numpy as np
import pandas as pd
import json
import requests


####
# Add Error Handling for response codes.
####
class NbaStatsShotLog(NbaStats):
	def __init__(self, *args, **kwargs):
		super(NbaStats, self).__init__(*args, **kwargs)
		self.url_template = "http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID={player_id}&Season={season}&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="
