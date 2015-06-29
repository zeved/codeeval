import sys

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

i = 1
divisor_1 = []
divisor_2 = []
stopper = []

for line in lines:
	ints = [int(s) for s in line.split() if s.isdigit()]
	stopper.insert(i, ints.pop())
	divisor_2.insert(i, ints.pop())
	divisor_1.insert(i, ints.pop())
	i += 1

divisor_1.reverse()		# yes I am lazy
divisor_2.reverse()
stopper.reverse()

def check(num, div1, div2):
	if ((j % div1 == 0) and (j % div2 == 0)):
		return "FB"
	if ((j % div1 == 0) and (j % div2 != 0)):
		return "F"
	if ((j % div1 != 0) and (j % div2 == 0)):
		return "B"
	if ((j % div1 != 0) and (j % div2 != 0)):
		return num

for i in range(1,len(lines)+1):
	div1 = divisor_1.pop()
	div2 = divisor_2.pop()
	stop = stopper.pop()
	for j in range(1, stop+1):
		sys.stdout.write(str(check(j, div1, div2))+' ')
	sys.stdout.write('\n')
