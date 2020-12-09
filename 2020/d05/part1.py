#nstabel

def get_seat(boarding):
	loc = {
		'F': [127, lambda loc: -(loc['F'][0] - loc['B'][0] + 1) // 2],
		'B': [0, lambda loc: (loc['F'][0] - loc['B'][0] + 1) // 2],
		'L': [7, lambda loc: -(loc['L'][0] - loc['R'][0] + 1) // 2],
		'R': [0, lambda loc: (loc['L'][0] - loc['R'][0] + 1) // 2]}
	for c in boarding[:-1]:
		loc[c][0] += loc[c][1](loc)
	return loc['B'][0] * 8 + loc['R'][0]
		
print(max([get_seat(boarding) for boarding in open('input', 'r').readlines()]))
