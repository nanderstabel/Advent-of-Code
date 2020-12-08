#nstabel

input = [int(num) for num in open('input', 'r').readlines()]
print([x * y for x in input for y in input if x + y == 2020][0])
