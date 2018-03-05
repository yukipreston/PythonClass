name = input("Enter File: ")
count = dict()

if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    line = line.rstrip()
    if line.startswith ('From '):
        line = line.split()
        time = line[5].split(":")
        count[time[0]] = count.get(time[0], 0) + 1

lst = list()

for key, val in list(count.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print (key, val)

# print (count)
# time_dic = list(count.items())
# time_dic.sort()
# print (time_dic)
#
# time_list = list()
# for key, val in list(time_dic):
#     time_list.append((key, val))
#
# for key, val in time_list:
#     print (key, val)
