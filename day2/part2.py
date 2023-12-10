# What is the fewest number of cubes of each color
# that could have been in the bag to make the game possible?

# So basically find the max value of each color within the samples

# Goal 1: Find the max value of each color within the samples
# Goal 2: Multiply each max color value together to find the POWER
# Add the power values together for each set.

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


# Part 2: Find the max value of each color within the samples
# Then multiply each max color value together to find the POWER

TOTAL = 0
for game in games:
    red = max(game["red"] for game in games[game])
    green = max(game["green"] for game in games[game])
    blue = max(game["blue"] for game in games[game])

    POWER = red * green * blue

    TOTAL += POWER

print(TOTAL)
