import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "data"))
# import team_player_ids

if __name__  == '__main__':
	print __file__
	print 'Path: ', os.path.dirname(__file__)
	print 'Path2: ', os.path.join(os.path.realpath(__file__), "/data")
	# print players