from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)

        for ch in s:
            letters[ch] += 1
        
        for ch in t:
            letters[ch] -= 1

        for letter, count in letters.items():
            if count != 0:
                return False
        return True