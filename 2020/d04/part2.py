#nstabel

count = 0
for passport in open('input', 'r').read().split('\n\n'):
	fields = dict([map(str.strip, field.split(':', 1)) for field in passport.split()])
	if 1920 <= int(fields['byr']) <= 2002 and 2010 <= int(fields['iyr']) <= 2020:
		count +=1

print(count)

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
'''