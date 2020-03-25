import numpy as np
import gambit

g = gambit.Game.read_game("input.nfg")

# print(list(g.contingencies))
undominated_strategies = g.support_profile().undominated()
undominated_strategies = np.array(undominated_strategies)
print(g.payoff_matrices[0])
no_equilibrium = 0
equilibriums = []
# print(undominated_strategies)
# print(players)
# print(undominated_strategies)
for player in range(len(g.players)):
	temp_undominated = []
	for i in range(len(undominated_strategies)):
		if str(undominated_strategies[i]).find(str(g.players[player].label)) != -1:
			# print(str(undominated_strategies[i]))
			# print(str(g.players[player].label))
			temp_undominated.append(str(undominated_strategies[i]))
	# print(temp_undominated)		
	# if len(temp_undominated) > 1:


if no_equilibrium == 1:
	print(0)
