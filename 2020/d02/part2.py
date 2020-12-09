#nstabel
import finditer from re

regex = r'(^\d*)|([\d]+?(?= ))|([a-z])(?=:)|([a-z]*$)'
count = 0
for it in [finditer(regex, line) for line in open('input', 'r').readlines()]:
	min, max, c, s = ([password.group() for password in it][:4])
	if (s[int(min) - 1] == c) != (s[int(max) - 1] == c):
		count += 1
print(count)	
