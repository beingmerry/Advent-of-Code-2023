"""
Solution for day 1 of Advent of Code.
"""

with open("Day 1/input.txt", encoding="ASCII") as f:
    lines = f.read().splitlines()

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

CALIBRATION_VALUE_SUM = 0
for line in lines:
    EXTRACTED_VALUE = ""
    i = 0
    for character in line:
        if character.isdigit():
            EXTRACTED_VALUE += character
        else:
            for word, number in NUMBERS.items():
                if line[i:i+len(word)] == word:
                    EXTRACTED_VALUE += str(number)
        i += 1
    # Find  size of extracted digits
    size = len(EXTRACTED_VALUE) - 1
    calibrationValue = EXTRACTED_VALUE[0] + EXTRACTED_VALUE[size]
    CALIBRATION_VALUE_SUM += int(calibrationValue)

print(CALIBRATION_VALUE_SUM)
