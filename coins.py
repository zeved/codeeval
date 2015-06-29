import sys

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

for line in lines:
	num = int(line.strip())
	fives = 0
	threes = 0

	fives = num // 5;
	if (fives != 0) and (num % fives == 0):
		total = fives
	else:
		rest = num - (fives * 5)
		threes = rest // 3;
		total = fives + threes + (num - (fives * 5 + threes * 3))
	print(total)
