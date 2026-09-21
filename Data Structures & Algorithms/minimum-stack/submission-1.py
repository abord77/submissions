import heapq

class MinStack:
    def __init__(self):
        self.min_heap = []
        self.stack = []
        self.element_id = 0
        self.removed = set()

    def push(self, val: int) -> None:
        self.element_id += 1
        self.stack.append((val, self.element_id))
        heapq.heappush(self.min_heap, (val, self.element_id))

    def pop(self) -> None:
        removed = self.stack.pop()
        self.removed.add(removed)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        while self.min_heap[0] in self.removed:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]
