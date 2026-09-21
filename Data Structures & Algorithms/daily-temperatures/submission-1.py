class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                old_day = stack.pop()
                result[old_day[1]] = i - old_day[1]
            
            stack.append((temp, i))
        return result