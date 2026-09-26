from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        if len(s1) > len(s2):
            return False

        wanted = dict(Counter(s1))
        curr_needed = wanted.copy()
        target = {key: 0 for key, value in curr_needed.items()}
        for right in range(len(s2)):
            if s2[right] not in wanted:
                curr_needed = wanted.copy()
                left = right + 1
                continue
            
            while curr_needed[s2[right]] - 1 < 0:
                curr_needed[s2[left]] += 1
                left += 1
            curr_needed[s2[right]] -= 1

            if curr_needed == target:
                return True
        return False