#nstabel	

forest = open('input').read().split('\n')
x, count = 0, 0
width = len(forest[0])
for y in range(len(forest)):
	if forest[y][x] == '#':
		count += 1
	x = (x + 3) % width
print(count)
