"""
This module calculates the sum of the IDs in the games based on certain conditions.

The module performs the following steps:
1) Ingests the sample data from a file.
2) Converts the data into structured format.
3) Evaluates a conditional for each game and sums the IDs of the games that meet the condition.
"""

# Step 1: Ingest the sample data
with open("input.txt", encoding="utf-8") as f:
    data = f.readlines()

# Step 1a. Convert to structured data
games = {}
colors = ["red", "green", "blue"]

for game_str in data:
    # Split each line into game number and game data
    game_num, game_data = game_str.split(": ")
    # Convert game number to int as ID
    game_num = int(game_num.split()[1])
    game = []
    # Split game data into sub games (samples)
    for sub_game_str in game_data.split("; "):
        sub_game = {}
        # Split sub game into color count pairs
        for color_count_str in sub_game_str.split(", "):
            count, color = color_count_str.split()
            sub_game[color] = int(count)
        # Add zero-counts for missing colors
        for color in colors:
            if color not in sub_game:
                sub_game[color] = 0
        game.append(sub_game)
    games[game_num] = game

# Step 2: Create & evaluate a conditional for 12 RED, 13 GREEN, 14 BLUE
# Step 3 along the way, sum the IDs


TOTAL = 0

for game, samples in games.items():
    red = []
    green = []
    blue = []
    for sample in samples:
        red.append(sample["red"])
        green.append(sample["green"])
        blue.append(sample["blue"])

    if max(green) <= 13 and max(red) <= 12 and max(blue) <= 14:
        TOTAL += game

print(f"The sum of the IDs in the games is {TOTAL}")
