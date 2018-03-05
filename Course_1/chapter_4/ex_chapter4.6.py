hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
def computepay(h,r):
    award = (h - 40) * r * 1.5
    return award
if h > 40:
    pay = computepay(h,r) + 40 * r
else :
    pay = h * r
print (pay)
