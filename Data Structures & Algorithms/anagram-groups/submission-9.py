from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        string_dict = defaultdict(list) # keyed on the Counter signature for each string

        for string in strs:
            signature_counter = Counter(string)
            signature = frozenset(signature_counter.items())
            
            string_dict[signature].append(string)
        
        for signature, string_list in string_dict.items():
            result.append(string_list)
        return result