handle = open('mbox-short.txt')
address = list()
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    lines = line.split()
    counts[lines[1]] = counts.get(lines[1], 0) + 1

biggest = None
bigword = None
for key, value in counts.items():
    if biggest is None or value > biggest:
        bigword = key
        biggest = value
print (bigword, biggest)
