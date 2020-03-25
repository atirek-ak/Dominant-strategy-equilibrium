import sys
import numpy as np
import itertools

players = 0
actions = []
players_list = []
payoff_matrix = []
multiplier = []

def extract():
	global players
	global actions
	global players_list
	global payoff_matrix
	global payoff_matrix_index
	global multiplier
	filename = sys.argv[1]
	game = open(filename, 'r')
	first_line = game.readline()
	second_line = game.readline()
	third_line = game.readline()
	fourth_line = game.readline()
	game.close()
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
	payoff_matrix = np.array(fourth_line.strip().split(' '))
	payoff_matrix = [int(payoff_matrix[i]) for i in range(0, len(payoff_matrix))]
	temp = 1
	for i in range(len(actions)):
		multiplier.append(temp)
		temp *= actions[i]
	# length = len(payoff_matrix)
	# payoff_matrix = [payoff_matrix[x:x + players] for x in range(0, length, players)]
	# payoff_matrix.reverse()
	# payoff_matrix = np.array(payoff_matrix)
	# payoff_matrix_index = [i for i in range(len(payoff_matrix))]
	# payoff_matrix_index = np.array(payoff_matrix_index)
	# payoff_matrix_index = payoff_matrix_index.reshape(actions)
	# print(payoff_matrix)
	# print(payoff_matrix_index)

def find_payoff(cur_player, temp_counter):
	result = 0
	i = 0
	for index in temp_counter:
		result = result + (index * multiplier[i] * players)
		i += 1
	# result *= players
	result += cur_player
	return result	


def find_dominant_strategy(cur_player, other_players, other_actions):
	max_index = [i for i in range(actions[cur_player])]
	counter = [0 for i in range(len(other_players))]
	while 1:	
		max_payoff = -sys.maxsize - 1
		temp_max_index = []
		for index in range(actions[cur_player]):
			temp_counter = counter[:]
			temp_counter.insert(cur_player, index)
			payoff = payoff_matrix[find_payoff(cur_player, temp_counter)]
			# print(payoff)
			# find max_payoff
			# payoff_index = payoff_matrix_index[:]
			# for i in range(len(temp_counter)):
				# payoff_index = payoff_index[temp_counter[i]]
			# payoff = int(payoff_matrix[payoff_index][cur_player])
			# print(payoff)
			if payoff > max_payoff:
				max_payoff = payoff
				temp_max_index = []
				temp_max_index.append(index)
			elif payoff == max_payoff:
				temp_max_index.append(index)
		# print("########")
		max_index = list(set(max_index) & set(temp_max_index))
		if max_index == []:
			return []
		counter[0] += 1
		for i in range(len(other_actions)):
			if counter[i] < other_actions[i]:
				break
			elif counter[i] == other_actions[i] and i == len(other_actions) - 1:
				return max_index
			elif counter[i] == other_actions[i]:
				counter[i] = 0
				counter[i+1] += 1




def main():
	extract()
	equilibria = []
	output = open(sys.argv[2], 'w')
	for i in range(players):
		other_players = players_list[:]
		other_players.pop(i)
		other_actions = actions[:]
		other_actions.pop(i)
		i_dominant = find_dominant_strategy(i, other_players,other_actions)
		if len(i_dominant) == 0:
			output.write("No Dominant Strategy Equilibria exist\n")
			output.close()	
			return
		else:
			equilibria.append(i_dominant)
	result = []
	# print(equilibria)
	for i in itertools.product(*equilibria):
		result.append(i)
	result.sort()	
	output.write(str(len(result)) + "\n")
	for element in result:
		for i in range(len(element)):
			arg = str(element[i]) + " "
			output.write(arg)
		output.write("\n")	
	output.close()	

main()	