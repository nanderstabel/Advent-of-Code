#nstabel

input = [int(num) for num in open('input', 'r').readlines()]
print([i * j for i in input for j in input if i + j == 2020][0])
