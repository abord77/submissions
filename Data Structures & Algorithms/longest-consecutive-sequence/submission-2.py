class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        start_points = []
        for num in num_set:
            if num - 1 not in num_set:
                start_points.append(num)
        
        longest = 0
        for start in start_points:
            curr = 1
            while start + 1 in num_set:
                curr += 1
                start += 1
            longest = max(longest, curr)
        return longest