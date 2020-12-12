#nstabel
import finditer from re

regex = r'(^\d*)|([\d]+?(?= ))|([a-z])(?=:)|([a-z]*$)'
count = 0
for it in [finditer(regex, line) for line in open('input').readlines()]:
	min, max, c, s = ([password.group() for password in it][:4])
	if int(min) <= s.count(c) <= int(max):
		count += 1
print(count)	
