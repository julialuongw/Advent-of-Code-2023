import os

# Read in the puzzle input and extract a sample for testing
curr_dir = os.path.dirname(__file__)
infile_path = os.path.join(curr_dir, "input.txt")

with open(infile_path, 'r') as f:
    INFILE = f.read().splitlines()
    SAMPLE = INFILE[0]


"""
PART A SOLUTION
A game is possible if and only if none of its draws contains a color exceeding its given maximum. This function uses this sole criteria to determine game possibility. 
"""
CUBE_MAX = {
    "RED": 12,
    "GREEN": 13,
    "BLUE": 14
}
def process_game_A(game: str) -> int:
    # Extract the draws
    game_prefix_idx = game.find(": ")
    draws = game[game_prefix_idx + len(": "):].split("; ")

    for draw in draws:
        # For each draw, extract a list of pairs of form [n, color]
        pairs = [pair.split(" ") for pair in draw.split(", ")]
        
        # Assess each pair, updating the draw-minimum of this color as needed
        for pair in pairs:
            n, color = int(pair[0]), pair[1].upper()
            if n > CUBE_MAX[color]:
                return 0
    
    # Game is possible -- return its id
    return int(game[:game_prefix_idx].replace("Game ", ""))

# Testing
# print(process_game(SAMPLE))

# Solve
sum_of_ids = 0
for game in INFILE:
    sum_of_ids += process_game_A(game)
print(sum_of_ids)


"""
PART B
"""

def process_game_B(game: str) -> int:
    # Extract the draws and save the prefix for return value later
    game_prefix_idx = game.find(": ")
    draws = game[game_prefix_idx + len(": "):].split("; ")

    min_cubes = dict.fromkeys(["RED", "GREEN", "BLUE"], 0)
    for draw in draws:
        # For each draw, extract a list of pairs of form [n, color]
        pairs = [pair.split(" ") for pair in draw.split(", ")]
        
        # Assess each pair, returning impossible if any number exceeds the max of that color
        for pair in pairs:
            n, color = int(pair[0]), pair[1].upper()
            if n > min_cubes[color]:
                min_cubes[color] = n
    
    # Compute and return this game's power
    power = 1
    for n in min_cubes.values():
        power *= n
    return power

# Testing
# print(process_game_B(SAMPLE))

sum_of_prods = 0
for game in INFILE:
    sum_of_prods += process_game_B(game)
print(sum_of_prods)
