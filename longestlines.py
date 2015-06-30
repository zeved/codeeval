import sys

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

number = int(lines[0].strip())

i = 0

lengths = []

for i in range(1, len(lines)):
	lengths.insert(i-1, len(lines[i]))

def get_longest(lengths_array, num):
	l = []
	i = 0
	while i < num:
		for j in range(0, len(lengths_array)):
			if lengths_array[j] == max(lengths_array):
				l.append(lengths_array[j])
				del lengths_array[j]
				break
		i += 1
	return l

longest = get_longest(lengths, number)

del lines[0]

while len(longest) != 0:
	for line in lines:
		if len(line) == max(longest):
			sys.stdout.write(line)
			longest.remove(max(longest))
			break
