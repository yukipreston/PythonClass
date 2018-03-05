fname = input("Enter file name: ")
inp = open(fname)
spam = 0
number is 0
for line in inp:
    if line.startswith('X-DSPAM-Confidence:'):
        spam = spam + 1
        number = number + float(line[20:])

print ('Average spam confidence:', number / spam)
