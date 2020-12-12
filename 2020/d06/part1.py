#nstabel

groups = open('input').read().split('\n\n')
print(sum([len(set(group.replace('\n', ''))) for group in groups]))
