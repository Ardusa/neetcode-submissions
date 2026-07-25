class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_map_s = dict()
        letter_map_t = dict()

        for letter in s:
            if letter in letter_map_s:
                letter_map_s[letter] += 1
            else:
                letter_map_s[letter] = 0

        for letter in t:
            if letter in letter_map_t:
                letter_map_t[letter] += 1
            else:
                letter_map_t[letter] = 0

        return letter_map_s == letter_map_t