from alpha.mathlib.geometry import circle_area, rectangle_area, square_area
import heapq
import sys
print(sys.modules['heapq'])
import numpy
print(sys.modules['numpy'])

a1 = circle_area(8)
a2 = rectangle_area(10, 12)
a3 = square_area(7.9)
print(a1, a2, a3)
