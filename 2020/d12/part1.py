#nstabel

class Ship:
	def __init__(self):
		self.vector = [1, 0, 0]
		self.compas = ((2, 1), (1, 1), (2, -1), (1, -1))
		self.encode = {letter:value for value, letter in enumerate('NESWLFR')}

	def get_dist(self):
		return abs(self.vector[1]) + abs(self.vector[2])

	def follow(self, instruction):
		action, value = self.encode[instruction[0]], int(instruction[1:])
		if action in (4, 6):
			self.rotate(action - 5, value // 90)
		else:
			self.move(self.vector[0] if action == 5 else action, value)

	def rotate(self, direction, degrees):
		self.vector[0] = (self.vector[0] + direction * degrees) % 4

	def move(self, direction, dist):
		self.vector[self.compas[direction][0]] += dist * self.compas[direction][1]

ship = Ship()
[ship.follow(instruction) for instruction in open('input').readlines()]

print(ship.get_dist())
