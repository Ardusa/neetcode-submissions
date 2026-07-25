class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        ls = list()

        for string in strs:
            key = [0] * 26

            for ch in string:
                key[ord(ch) - ord('a')] += 1
            
            key_str = tuple(key)

            if key_str in d:
                ls[d[key_str]].append(string)
            
            else:
                index = len(ls)
                d[key_str] = index
                ls.append([string])

        return ls