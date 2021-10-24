
def add( x , y) :
    _add = x + y
    return _add
def mul(x , y) :
    _mul = x * y
    return _mul
def div ( x , y ) :
    _div = format (x / y ,'.2f')
    return _div
def sub ( x , y ) :
    _sub = x - y
    return _sub
x = int (input ( ' Enter X :'))
y = int (input ( ' Enter Y :'))
print ( f' ADD = {add(x,y)}, MUL = {mul(x,y)} , DIV = {div(x,y)} , SUB = {sub(x,y)}' )
