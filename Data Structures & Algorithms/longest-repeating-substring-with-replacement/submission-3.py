from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)

        left, right = 0, 0

        max_len = 0
        for right in range(len(s)):
            frequencies[s[right]] += 1

            max_freq = max(frequencies.values())

            window_size = right - left + 1

            while window_size - max_freq > k:
                frequencies[s[left]] -= 1
                max_freq = max(frequencies.values())
                window_size -= 1
                left += 1

            max_len = max(window_size, max_len)
        return max_len
