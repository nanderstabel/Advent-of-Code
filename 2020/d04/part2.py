#nstabel
from re import match

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count = 0
for passport in open('input', 'r').read().split('\n\n'):
	fields = dict([field.split(':') for field in passport.split()])
	if all(field in fields for field in required):
		if all([
			1920 <= int(fields['byr']) <= 2002,
			2010 <= int(fields['iyr']) <= 2020,
			2020 <= int(fields['eyr']) <= 2030,
			match(r'^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$', fields['hgt']),
			match(r'^#[a-f\d]{6}$', fields['hcl']),
			fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
			match(r'^\d{9}$', fields['pid'])]):
			count +=1
print(count)
