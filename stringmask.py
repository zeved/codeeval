import sys

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

i = 1
words = []
masks = []

for line in lines:
	split_line = line.split()
	masks.insert(i, split_line.pop())
	words.insert(i, split_line.pop())
	i += 1

def maskit(word, mask):
	word_array = list(word)
	mask_array = list(mask)
	for i in range(0, len(word)):
		if mask[i] == "1":
			old = word_array[i]
			new = old.upper()
			word_array[i] = new
		if mask[i] == "0":
			old = word_array[i]
			new = old.lower()
			word_array[i] = new
	print(''.join(word_array))

for i in range(0, len(lines)):
	word = words[i]
	mask = masks[i]
	maskit(word, mask)
