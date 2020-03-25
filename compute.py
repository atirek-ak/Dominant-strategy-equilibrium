from numpy import zeros
import numpy as np
import sys

players = 0
actions = []
players_list = []

def extract():
	global players
	global actions
	global players_list
	game = open('./input.nfg','r')
	first_line = game.readline()
	second_line = game.readline()
	third_line = game.readline()
	fourth_line = game.readline()

	# computing number of players
	for character in second_line:
		if character == '}':	
			break
		elif character == '"':
			players += 1
	players /= 2
	players = int(players)
	players_list = [i for i in range(players)]
	#computing number of actions for each player
	second_line = second_line[1:]
	second_line = second_line[:-2]
	x = second_line.split('{')
	actions = x[1].strip().split(' ')
	actions = [int(element) for element in actions]
	# actions.reverse()
	# actions.append(players)
	# actions.reverse()
	
	#form matrix
	# payoff = np.array(fourth_line.strip().split(' '))
	# payoff = payoff.reshape(actions)
	# print(payoff)

#find dominant strategies for players
def find_dominant_strategy(player, total_players, strategies = [], equilibrium_index):
	if len(total_players) > 0:
		cur_player = total_players[0]
		res = []
		total_players = total_players[1:]
		for action in range(actions[cur_player]):
			temparray = strategies
			temparray.append(action)
			equilibrium_index = find_dominant_strategy(player, total_players, temparray, equilibrium_index)

	else:	
		max_payoff = -sys.maxint
		max_index = []
		for action in range(action[player]):
			temp_array = strategies
			temp_array.insert(player, action)
			

def main():
	extract()
	equilibria = []
	for i in range(players):
		other_players = players_list
		other_players.remove(i)
		i_dominant = find_dominant_strategy(i, other_players,,[])
		if len(i_dominant):
			equilibria.append(i_dominant)
		else:
			print(0)
			return	


main()