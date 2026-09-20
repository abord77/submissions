class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            diff = target - numbers[start]

            while numbers[end] >= diff:
                if numbers[end] == diff:
                    return [start + 1, end + 1]
                end -= 1
            start += 1