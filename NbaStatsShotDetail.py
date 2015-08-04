import numpy as np
import pandas as pd
import json
import requests


####
# Add Error Handling for response codes.
####
class NbaStatsShotDetail(NbaStats):
	def __init__(self, *args, **kwargs):
		super(NbaStats, self).__init__(*args, **kwargs)
		self.url_template = "http://stats.nba.com/stats/shotchartdetail?Period=0&VsConference=&LeagueID=00&LastNGames=0&TeamID=0&Position=&Location=&Outcome=&ContextMeasure=FGA&DateFrom=&StartPeriod=&DateTo=&OpponentTeamID=0&ContextFilter=&RangeType=&Season={season}&AheadBehind=&PlayerID={playerId}&EndRange=&VsDivision=&PointDiff=&RookieYear=&GameSegment=&Month=0&ClutchTime=&StartRange=&EndPeriod=&SeasonType=Regular+Season&SeasonSegment=&GameID="
