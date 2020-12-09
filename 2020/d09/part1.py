#nstabel	

input = [int(num) for num in open('input', 'r').readlines()]
for cur in range(25, len(input)):
	preamble = input[cur - 25:cur]
	if all(x + y != input[cur] for x in preamble for y in preamble):
		print(input[cur])
