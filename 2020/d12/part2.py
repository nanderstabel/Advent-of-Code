#nstabel

class Ship:
	def __init__(self):
		self.vector = [1, 0, 0]
		self.waypoint = [1, 10, 0, 0]
		self.compas = ((2, 1), (1, 1), (2, -1), (1, -1))
		self.encode = {letter:value for value, letter in enumerate('NESWLFR')}

	def get_dist(self):
		return abs(self.vector[1]) + abs(self.vector[2])

	def follow(self, instruction):
		action, value = self.encode[instruction[0]], int(instruction[1:])
		if action in (4, 6):
			self.rotate(action - 5, value // 90)
		elif action == 5:
			self.move(value)
		else:
			self.set_waypoint(action, value)

	def rotate(self, direction, degrees):
		x = direction * degrees
		self.waypoint = self.waypoint[-x:] + self.waypoint[:-x]

	def move(self, value):
		for i, dist in enumerate(self.waypoint):
			if dist > 0:
				self.vector[self.compas[i][0]] += dist * value * self.compas[i][1]

	def set_waypoint(self, action, dist):
		self.waypoint[action] += dist

ship = Ship()
[ship.follow(instruction) for instruction in open('input').readlines()]
print(ship.get_dist())