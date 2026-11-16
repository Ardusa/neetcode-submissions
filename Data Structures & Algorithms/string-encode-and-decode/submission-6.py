class Solution:
    def encode(self, strs: List[str]) -> str:
        def process(string: str) -> str:
            return f"{len(string)}#{string}"

        ret = ""

        for string in strs:
            ret += process(string)

        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        print(s)

        while i < len(s):
            j = i + 1

            while s[j] != "#":
                j += 1
            j + 1

            iters = int(s[i:j])
            i = j + iters + 1

            strs.append(s[j + 1:i])

        return strs
