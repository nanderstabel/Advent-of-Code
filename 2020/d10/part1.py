#nstabel

adapters = sorted([0] + [int(num) for num in open('input').readlines()])
diffs = [nexts - cur for cur, nexts in zip(adapters[:-1], adapters[1:])]
print(diffs.count(1) * (diffs.count(3) + 1))
