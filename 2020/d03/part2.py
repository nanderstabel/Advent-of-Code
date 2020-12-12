#nstabel	

forest = open('input').read().split('\n')
width = len(forest[0])
product = 1
for hor, ver in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
	x, count = 0, 0
	for y in range(len(forest))[::ver]:
		if forest[y][x] == '#':
			count += 1
		x = (x + hor) % width
	product *= count
print(product)
