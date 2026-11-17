class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr, rightPtr = 0, len(s) - 1

        while leftPtr < rightPtr:
            while not s[leftPtr].isalnum() and leftPtr < rightPtr:
                leftPtr += 1
            
            while not s[rightPtr].isalnum() and rightPtr > leftPtr:
                rightPtr -= 1

            print(s[leftPtr], s[rightPtr])

            if s[leftPtr].lower() != s[rightPtr].lower():
                return False            

            leftPtr += 1
            rightPtr -= 1
        
        return True