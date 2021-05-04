from heapq import *
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))

    def return_point(self):
        return [self.x, self.y]

def find_closest_points(points, k):
    distance_and_points = {}
    min_heap = []
    for point in points:
        distance_and_points[point.distance_from_origin()] = point
        min_heap.append(point.distance_from_origin())
    heapify(min_heap)
    k_closest_distances = nsmallest(k, min_heap)
    result = []
    for distance in k_closest_distances:
        result.append(distance_and_points[distance].return_point())
    return result
    

print(find_closest_points([Point(1,2), Point(1,3)],1))
print(find_closest_points([Point(1,3), Point(3,4), Point(2,-1)],2))

