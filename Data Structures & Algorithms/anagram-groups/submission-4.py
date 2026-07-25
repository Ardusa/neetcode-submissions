class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        # fill out strMap
        for s in strs:
            sMap = defaultdict(int)

            for ch in s:
                sMap[ch] += 1
            
            key = tuple(sorted(sMap.items()))

            strMap[key].append(s)
        
        ret = list(strMap.values())

        return ret