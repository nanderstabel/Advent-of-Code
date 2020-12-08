#nstabel
import re

regex = r"(^\d*)|([\d]+?(?= ))|([a-z])(?=:)|([a-z]*$)"
count = 0
for it in [re.finditer(regex, line) for line in open('input', 'r').readlines()]:
	min, max, c, s = ([password.group() for password in it][:4])
	if bool(s[int(min) - 1] == c) != bool(s[int(max) - 1] == c):
		count += 1
print(count)	
