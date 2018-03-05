fname = input("Enter file name: ")
fhand = open(fname)
final = list()
for line in fhand:
    line = line.rstrip()
    words = line.split() # String --> List
    for word in words:
        if word not in final:
            final.append(word)
final.sort()
print (final)
