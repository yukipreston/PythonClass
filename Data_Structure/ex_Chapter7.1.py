# Use words.txt as the file name
fname = input("Enter file name: ")
inp = open(fname)
for line in inp:
    print (line.rstrip().upper())
