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
        for right in range(len(s)):
            while s[right] in in_window:
                in_window.remove(s[left])
                left += 1

            in_window.add(s[right])
            longest = max(longest, right - left + 1)
        return longest