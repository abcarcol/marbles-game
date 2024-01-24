import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='absolute or relative path to the game input file', required=True)
args = parser.parse_args()

with open(args.path, 'r') as fp:
    games = fp.readlines() #Each element of the list contains information about one game
    nGames = len(games) #Total number of games played 

colors_map = {'RED':0 , 'GREEN': 1, 'BLUE': 2}

import numpy as np

matrix = np.zeros((nGames,len(colors_map)))

part1_matrix = [[12, 13, 14] for _ in range(nGames)] #Matrix for games with 12 red, 13 green and 14 blue cubes, respectively

import re

game_index = 0

for game in games:
    
    redData = re.findall(r"\s*(?:(\d+) (red))", game)
    redData = [eval(i) for i in (list(zip(*redData))[0])]

    blueData = re.findall(r"\s*(?:(\d+) (blue))", game)
    blueData = [eval(i) for i in (list(zip(*blueData))[0])]

    greenData = re.findall(r"\s*(?:(\d+) (green))", game)
    greenData = [eval(i) for i in (list(zip(*greenData))[0])]

    matrix[game_index][colors_map['RED']] = max(redData)
    matrix[game_index][colors_map['GREEN']] = max(blueData)
    matrix[game_index][colors_map['BLUE']] = max(greenData)          
    
    game_index+=1

offset_matrix = part1_matrix - matrix

def divide_by_abs(x): #We convert positive offsets into +1 and negative offsets into -1
    if x != 0: 
        return x / abs(x)
    else: #0 offsets are converted into +1
        return 1

divide_by_abs_vect = np.vectorize(divide_by_abs)
offset_matrix = divide_by_abs_vect(offset_matrix) #We apply the divide_by_abs() function to every value of the offset matrix

part1_result = 0
game_index = 0

for row in offset_matrix: 
    if sum(row) == len(colors_map): #Only games corresponding to rows with all positive (including 0) offsets are possible
        part1_result+=(game_index+1)
    game_index+=1

print("The result for the first part is: {}".format(part1_result))

part2_result = 0

for row in matrix: 
    part2_result+=(np.prod(row))

print("The result for the second part is: {}".format(part2_result))
