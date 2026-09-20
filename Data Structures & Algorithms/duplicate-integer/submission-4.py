class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num not in unique_nums:
                unique_nums.add(num)
            else:
                return True
        return False