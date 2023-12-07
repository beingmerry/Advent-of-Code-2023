"""
Solution for day 1 of Advent of Code.
"""

with open("Day 1/testInputPart2.txt", encoding="ASCII") as f:
    lines = f.read().splitlines()
# create dictionary of translating words to numbers for 1 to 9
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
print(lines)

CALIBRATION_VALUE_SUM = 0
for line in lines:
    EXTRACTED_VALUE = ""

    for character in line:
        if character.isdigit():
            EXTRACTED_VALUE += character

    # Find  size of extracted digits
    size = len(EXTRACTED_VALUE) - 1
    calibrationValue = EXTRACTED_VALUE[0] + EXTRACTED_VALUE[size]
    CALIBRATION_VALUE_SUM += int(calibrationValue)

print(CALIBRATION_VALUE_SUM)
