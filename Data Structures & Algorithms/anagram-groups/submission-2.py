class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        ret = list()

        for ls in res.values():
            inner = list()

            for string in ls:
                inner.append(string)

            ret.append(inner)

        print(ret)

        return ret