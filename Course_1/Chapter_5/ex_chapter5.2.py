largest = None
smallest = None

while True:
    val = input('Enter a number: ')
    if val == ('done'):
        break
    try:
        num = float(val)
    except:
        print ('Invalid input')
        continue
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

print (largest, smallest)
