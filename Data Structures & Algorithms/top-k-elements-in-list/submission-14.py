from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k = [] # each element will be a tuple (count, num)

        for num, count in counts.items():
            if len(top_k) == k:
                if top_k[0][0] < count:
                    heapq.heappushpop(top_k, (count, num))
                continue
            heapq.heappush(top_k, (count, num))
        
        result = []
        for count, num in top_k:
            result.append(num)
        return result