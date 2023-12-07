# import input .txt file

with open('input.txt', encoding="ASCII") as f:
    lines = f.read().splitlines()

# read line 1 into list

line1 = lines[0].split(',')
line2 = lines[1].split(',')

# print line1 and line2 on separate lines

print(line1)
print(line2)
