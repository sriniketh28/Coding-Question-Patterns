from heapq import *

def minimum_cost_to_connect_ropes(ropeLenghts):
    min_heap = ropeLenghts.copy()
    heapify(min_heap)
    cost, temp = 0, 0
    while len(min_heap)>1:
        temp = heappop(min_heap) + heappop(min_heap)
        cost += temp
        heappush(min_heap, temp)

    return cost

print(minimum_cost_to_connect_ropes([1, 3, 11, 5]))
print(minimum_cost_to_connect_ropes([3, 4, 5, 6]))
print(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]))

