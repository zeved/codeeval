import sys

with open(sys.argv[1], "r") as f:
	lines = f.readlines()


iterations = []
numbers = []

nr_lines = 0

for line in lines:
	split_line = line.split()
	split_line.remove('|')
	it = split_line[len(split_line)-1]
	iterations.append(int(it))
	split_line.remove(it)
	numbers.append(list(map(int,split_line)))
	nr_lines += 1

def bsort(nums, times):
	k = 0
	for i in reversed(range(len(nums))):
		done = True
		for j in range(i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				done = False
		if done:
			break
		k += 1
		if k == times:
			break
	return nums

for i in range(nr_lines):
	sorted_nums = bsort(numbers[i], iterations[i])
	for j in range(len(sorted_nums)):
		sys.stdout.write(str(sorted_nums[j])),
		sys.stdout.write(' '),
	print("\n"),
