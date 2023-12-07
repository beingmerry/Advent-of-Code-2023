"""
Solution for day 1 of Advent of Code.
"""

with open("Day 1/input.txt", encoding="ASCII") as f:
    lines = f.read().splitlines()

# print line1 and line2 on separate lines
CALIBRATION_VALUE_SUM = 0
for line in lines:
    # print(line)
    # extract first digit found on line
    EXTRACTED_VALUE = ""
    for character in line:
        if character.isdigit():
            EXTRACTED_VALUE += character

    size = len(EXTRACTED_VALUE) - 1
    calibrationValue = EXTRACTED_VALUE[0] + EXTRACTED_VALUE[size]
    CALIBRATION_VALUE_SUM += int(calibrationValue)

print(CALIBRATION_VALUE_SUM)
