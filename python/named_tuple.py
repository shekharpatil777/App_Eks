from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
pt = Point(10, 20)
print(pt.x, pt.y)  # 10 20
