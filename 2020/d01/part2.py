#nstabel

input = [int(num) for num in open('input', 'r').readlines()]
print([x * y * z for x in input for y in input for z in input if x + y + z == 2020][0])
