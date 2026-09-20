class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            want = target - num

            if want in seen:
                return [i, seen[want]] if i < seen[want] else [seen[want], i]
            
            seen[num] = i