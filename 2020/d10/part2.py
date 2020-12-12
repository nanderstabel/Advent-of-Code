#nstabel	
from itertools import combinations

input = [int(num) for num in open('input').readlines()]
size = len(input)
for pos, cur in enumerate(input[25:], 25):
	if all(sum(comb) != cur for comb in combinations(input[pos - 25:pos], 2)):
		result = [input[i:j] for i in range(size) for j in range(i + 2, size + 1) if sum(input[i:j]) == cur][0]
		print(max(result) + min(result))