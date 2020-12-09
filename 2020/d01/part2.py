#nstabel

input = [int(num) for num in open('input', 'r').readlines()]
print([i * j * k for i in input for j in input for k in input if i + j + k == 2020][0])
