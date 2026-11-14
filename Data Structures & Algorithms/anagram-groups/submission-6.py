from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            maps[sortedString].append(string)

        return list(maps.values())