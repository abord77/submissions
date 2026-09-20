from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)] # fixed length and only stores the elements that appear that many times
        # for example, if we have [4, 3, 3, 1, 1, 0, 0, 0] then freq = [[], [4], [3, 1], [0], [], [], ...]

        for num, count in counts.items():
            freq[count].append(num)
        
        result = []
        i = len(freq) - 1
        while k > 0:
            if len(freq[i]) <= k:
                result += freq[i]
                k -= len(freq[i])
            else:
                for j in range(len(freq[i]) - k):
                    result.append(freq[i][j])
                k = 0
            i -= 1
            
        return result