class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 2)
        suffix = [1] * (len(nums) + 2)

        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[len(nums) - i + 1] = suffix[len(nums) - i + 2] * nums[len(nums) - i]

        result = []
        for i in range(1, len(nums) + 1):
            result.append(prefix[i - 1] * suffix[i + 1])
        return result
