#nstabel	
from itertools import combinations

input = [int(num) for num in open('input').readlines()]
for pos, cur in enumerate(input[25:], 25):
	if all(sum(comb) != cur for comb in combinations(input[pos - 25:pos], 2)):
		print(cur)
