#nstabel
from itertools import combinations
from numpy import prod

input = [int(num) for num in open('input').readlines()]
[print(prod(comb)) for comb in combinations(input, 2) if sum(comb) == 2020]