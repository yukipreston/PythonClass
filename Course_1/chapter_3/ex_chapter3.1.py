hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print ("Please type in numeric number")
    quit ()

if h > 40 :
    pay = ((h - 40) * 1.5 * r) + (40 * r)
else :
    pay = h * r

print (pay)
