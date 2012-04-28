import math

#lines = sys.stdin.readlines()[1:]

def get_angle(coords, x):
    p1 = coords[:2]
    p2 = coords[2:]
    if p1[0] <= p2[0]:
        pa = p1
        pb = p2
    else:
        pa = p2
        pb = p1
    pc = [x, 0]
    a = distance(pb, pc)
    b = distance(pa, pc)
    c = distance(pa, pb)
    return math.degrees(math.acos((a**2 + b**2 - c**2) / 2*a*b))

def distance(p1, p2):
    return (abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2)**0.5

def binary_search(coords):
    p1 = coords[:2]
    p2 = coords[2:]
    middle = (p1[0] + p2[0]) / 2
    angle = get_angle(coords, middle)


lines = ['1 1 3 1', '-2 1 -1 2', '0 2 3 3']
lines = [map(float, lst.split(' ')) for lst in lines]

for coords in lines:
    binary_search(coords)
