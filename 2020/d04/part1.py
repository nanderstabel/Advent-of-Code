#nstabel

required = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
count = 0
for passport in open('input', 'r').read().split('\n\n'):
	if all(field in passport for field in required):
		count += 1
print(count)
