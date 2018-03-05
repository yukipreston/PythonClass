number = list()
total = 0
import re
name = input("Enter File: ")
if len(name) < 1 : name = "regex_sum_7860.txt"

handle = open(name)
for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) < 1 : continue
    for x in num:
        value = int(x)
        total = total + value
print (total)
