class Solution:
    key = " asdfasdgdasfeacsadfase "
    key_len = len(key)

    def encode(self, strs: List[str]) -> str:
        ret = ""

        if len(strs) == 0:
            return ret

        for i in range(len(strs)):
            s = strs[i]
            ret += s
            ret += self.key
        
        ret += strs[-1]

        return ret


    def decode(self, s: str) -> List[str]:
        cache = ""
        strs = list()

        for ch in s:
            cache += ch

            if self.key in cache:
                append = cache[0:-self.key_len]
                strs.append(append)
                cache = ""

        return strs