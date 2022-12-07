input = open("input.txt",'r')
elves = [0]

elf = 0
# print("Elf #"+str(elf))
for line in input.readlines():
    if line == '\n':
        # print("Total: " + str(elves[elf]))
        elf += 1
        elves.append(0)
        # print("Elf #"+str(elf))
        continue;
    else:
        elves[elf] += int(line)
result = sorted(elves,reverse = True)
print("Part 1: Highest calories total - " + str(result[0]))
top3 = result[0] + result[1] + result[2]
print("Part 2: Top 3 total - " + str(top3))