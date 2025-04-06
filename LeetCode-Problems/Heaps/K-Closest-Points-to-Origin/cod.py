import heapq
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    def dist(x, y):
        return x**2 + y**2

    heap = []
    for x, y in points:
        d = dist(x, y)
        if len(heap) < k:
            heapq.heappush(heap, (-d, x, y))
        else:
            heapq.heappushpop(heap, (-d, x, y))

    return [(x, y) for d, x, y in heap]