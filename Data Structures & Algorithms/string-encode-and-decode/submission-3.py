class Solution:
    # start with # of chars in the next word, process that and then continue pattern
    # we should pad anything with len less than 3 with # (since strs[i].length < 200 so need 3 digits)

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            str_len = str(len(string)).ljust(3, '#')
            subsection = str_len + string
            encoded += subsection
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            next_string_len = int(s[i:i + 3].replace('#', ''))
            curr_str = ""
            for j in range(i + 3, i + next_string_len + 3):
                curr_str += s[j]
            strs.append(curr_str)
            i += next_string_len + 3
        return strs

