"""
Solution for day 2 of Advent of Code.
"""

with open("Day 2/input.txt", encoding="ASCII") as f:
    games = f.read().splitlines()
# Max cubes for each color
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}
VALID_GAME_SUM = 0
GAME_NUMBER = 1
POWER_SUM = 0
for game in games:
    VALID_GAME = True
    gameCubesMax = {}
    # print(game)
    gameGrabs = game.split(":")[1].split(";")
    for grabsCounts in gameGrabs:
        colorsCounts = grabsCounts.split(",")
        for cubesColor in colorsCounts:
            # print(cubesColor)
            cubesColorSplit = cubesColor.strip().split(" ")
            cubes = int(cubesColorSplit[0])
            currentColor = cubesColorSplit[1]
            if currentColor not in gameCubesMax:
                gameCubesMax[currentColor] = cubes
            elif gameCubesMax[currentColor] < cubes:
                gameCubesMax[currentColor] = cubes
            if cubes > MAX_CUBES[currentColor]:
                VALID_GAME = False

    # print(f"Game Number: {GAME_NUMBER}")
    # print(gameCubesMax)
    POWER = 1
    for _color, value in gameCubesMax.items():
        POWER *= value
    # print(POWER)
    POWER_SUM += POWER
    if VALID_GAME:
        VALID_GAME_SUM += GAME_NUMBER
    GAME_NUMBER += 1

print(f"Valid game sum: {VALID_GAME_SUM}")
print(f"Power game sum: {POWER_SUM}")
