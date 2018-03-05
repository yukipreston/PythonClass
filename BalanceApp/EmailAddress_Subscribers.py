handle = open("subscribers-2017-08-13.csv")
new = open("emailaddress_08.13.17.csv", "w+")

for line in handle:
    line = line.rstrip()
    line = line.split(",")
    new.write(line[0] + ",\n")

new.close()
handle.close()
