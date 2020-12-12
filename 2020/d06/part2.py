#nstabel

groups = open('input').read().split('\n\n')
total = 0
for group, size in [(g.replace('\n', ''), g.count('\n') + 1) for g in groups]:
	total += sum([group.count(c) == size for c in set(group)])
print(total)
