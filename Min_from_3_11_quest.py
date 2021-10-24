
def _min_from_3 (x,y,z):

    if x < y and x < z  :
        return (x)
    elif y < x and y <z :
        return (y)
    else :
        return (z)
x = int(input(' Enter first number :'))
y = int(input(' Enter second number :'))
z = int(input('Enter third number :'))
print (f' Your minimum number : {_min_from_3(x,y,z)}')

