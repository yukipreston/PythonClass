fhand = open('mbox-short.txt')
final = list()
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    address = line.split()
    count = count + 1
    print (address[1])
print ("There were", count, "lines in the file with From as the first word")
