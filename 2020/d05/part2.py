#nstabel

move = {
	'F': lambda loc: -(loc['F'] - loc['B'] + 1) // 2,
	'B': lambda loc: (loc['F'] - loc['B'] + 1) // 2,
	'L': lambda loc: -(loc['L'] - loc['R'] + 1) // 2,
	'R': lambda loc: (loc['L'] - loc['R'] + 1) // 2}

def get_seat(boarding):
	loc = {'B': 0, 'F': 127, 'R': 0, 'L': 7}
	for c in boarding[:-1]:
		loc[c] += move[c](loc)
	return loc['B'] * 8 + loc['R']
		
seats = [get_seat(boarding) for boarding in open('input', 'r').readlines()]
[print(id) for id in range(max(seats)) if all([
											id not in seats,
											id - 1 in seats,
											id + 1 in seats])]
		
