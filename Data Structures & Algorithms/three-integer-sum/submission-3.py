class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        solutions = set()
        for num in nums:
            diff = target - num
            if diff in seen:
                solutions.add((diff, num))
            seen.add(num)
            
        return solutions
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix 1 number and then do 2 sum
        nums.sort()

        i = 0
        result = []
        while i < len(nums):
            curr = nums[i]
            
            twoSum = self.twoSum(nums[i + 1:], 0 - curr)
            for pairs in twoSum:
                result.append(list(pairs) + [curr])
            
            while i < len(nums) and nums[i] == curr:
                i += 1
        return result

