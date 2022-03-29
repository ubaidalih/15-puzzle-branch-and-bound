from heapq import heappush, heappop

class Node:
    def __init__(self, parent,id, matrix, cost, block_pos, level):
        self.parent = parent
        self.id = id
        self.matrix = matrix
        self.cost = cost
        self.block_pos = block_pos
        self.level = level

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.level < other.level
        return self.cost < other.cost

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap