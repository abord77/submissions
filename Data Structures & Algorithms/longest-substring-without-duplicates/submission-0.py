class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzyxz
        # z, zx, zxy, zxyz
        # xyz, xyzy
        # yzy, zy, zyx, zyxz
        # yxz
        in_window = set()

        left, right = 0, 0

        longest = 0
        while right < len(s):
            if s[right] not in in_window:
                in_window.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
                continue

            while s[right] != s[left]:
                in_window.remove(s[left])
                left += 1
            in_window.remove(s[left])
            left += 1
        return longest