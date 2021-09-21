import constants
from copy import deepcopy
import math

players_copy = deepcopy(constants.PLAYERS)
teams_copy = deepcopy(constants.TEAMS)

panthers = []
bandits = []
warriors = []
experienced = []
inexperienced = []


def clean():

	for value in players_copy:
		height = value['height'].split()
		value['height'] = int(height[0])
		
		if value['experience'] == 'YES':
			value['experience'] = True
			experienced.append(value)
		else:
			value['experience'] = False
			inexperienced.append(value)
			
		value['guardians'] = value['guardians'].split(' and ')
			
	
def team_balance():
	
	num_experienced = int(len(experienced) / len(teams_copy))
	num_inexperienced = int(len(inexperienced)/len(teams_copy))
	total_players = num_experienced + num_inexperienced
	
	for player in experienced:
		if len(panthers) < num_experienced:
			panthers.append(player)
		elif len(bandits) < num_experienced:
			bandits.append(player)
		else:
			warriors.append(player)
	
	for player in inexperienced:
		if len(panthers) < total_players:
			panthers.append(player)
		elif len(bandits) < total_players:
			bandits.append(player)
		else:
			warriors.append(player)
		

def team_stats(team):
	
	names = []
	num_experienced = []
	num_inexperienced = []
	guardians = []
	guardians_together = []
		
	for name in team:
		names.append(name['name'])
		
	for player in team:
		if player['experience'] == True:
			num_experienced.append(player)
		else:
			num_inexperienced.append(player)
	
	for value in team:
		sum_height = 0
		sum_height += value['height']
		av_height = sum_height / len(team)
	
	for guardian in team:
		guar_names = ', '.join(guardian['guardians'])
		guardians_together.append(guar_names)
	
	print("\nTotal players = {}".format(len(team)))
	print("Names of players = {}".format(', '.join(names)))
	print("\nNumber of experienced players = {}".format(len(num_experienced)))
	print("Number of inexperienced players = {}".format(len(num_inexperienced)))
	print("\nAverage height = {:.3} inches".format(av_height))
	print("\nGuardians for players on team = {}".format(', '.join(guardians_together)))

			
def main():
	
	print("\nWELCOME TO THE BASKETBALL TEAM STATS TOOL!")

	while True:
		
		print("\n------ MENU ------")
		first_choice = input("\nWhat would you like to do? \n\nA) Display Team Stats \nB) Quit\n\nEnter an option: ")
		if first_choice.upper() == "A":
			
			while True:
				
				print("\nWhich team would you like to see the stats for? \n\nA) Panthers \nB) Bandits \nC) Warriors")
				print("\n(Type 'X' to return to Menu)")
				second_choice = input("\nEnter an option: ")
				if second_choice.upper() == "A":
					print("\nTeam: Panthers \n-------------------")
					team_stats(panthers)
					print("\n-------------------")
				elif second_choice.upper() == "B":
					print("\nTeam: Bandits \n-------------------")
					team_stats(bandits)
					print("\n-------------------")
				elif second_choice.upper() == "C":
					print("\nTeam: Warriors \n-------------------")
					team_stats(warriors)
					print("\n-------------------")
				elif second_choice.upper() == "X":
					break
				else:
					print("\n(Please enter a valid choice! Team: A, B or C?)")
					continue
			
		elif first_choice.upper() == "B":
			print("\nOkay, see you soon!")
			break
		else:
			print("\n(Oops! Please enter either choice A or B.)")
			continue		
			
if __name__ == '__main__':
	clean()
	team_balance()
	main()
	