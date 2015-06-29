import sys

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

i = 1
longest = ""


def longest_word(_list):
	longestw = ""
	for word in _list:
		if len(word) > len(longestw):
			longestw = word
	return longestw

words = []

for line in lines:
	words = line.split()
	longest = longest_word(words)
	letters = list(longest)
	for i in range(0, len(letters)):
		sys.stdout.write(letters[i]+' ')
		if i != len(letters)-1:
			sys.stdout.write(''.join('*' * (i+1)))
	sys.stdout.write('\n')
