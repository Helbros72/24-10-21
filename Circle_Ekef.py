import math

def getCircleHekef(r):
    _hekef = 2 * math.pi * r
    return _hekef

radius = float(input('please enter radius [f]: '))
circle_hekef = getCircleHekef(radius)
print(f'circle hekef: {circle_hekef}')
