import numpy as np
import pandas as pd
import json
import requests


####
# Add Error Handling for response codes.
####
class NbaStats(object):
	def __init__(self, playerId, season):
		self.playerId = playerId
		self.season = season
		self.has_data = False

	# def get_shotlog_response(self):
	def get_nba_response(self):
		url = self.url_template.format(playerId = self.playerId, season = self.season) 
		response = requests.get(url)
		self.data = json.loads(response.text)
		if 'rowSet' in self.data['resultSets'][0].keys():
			if len(self.data['resultSets'][0]['rowSet']) > 0:
				self.has_data = True

	def bld_dataframe_from_response(self):
		headers = self.data['resultSets'][0]['headers']
		data = self.data['resultSets'][0]['rowSet']
		self.df = pd.DataFrame(data, columns=headers)
		
	def add_playerId(self):
		self.df.insert(0, 'playerId', self.playerId)

	def get_shots_and_fill_df(self):
		self.get_nba_response()
		if self.has_data:
			self.bld_dataframe_from_response()
			self.add_playerId()
