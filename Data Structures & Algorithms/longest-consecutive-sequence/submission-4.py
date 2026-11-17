class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        theSet = set(nums)
        highest = 0

        for x in nums:
            while x - 1 in theSet:
                x -= 1

            counter = 1
            while x + 1 in theSet:
                counter += 1
                x += 1
                theSet.remove(x)

            if counter > highest:
                highest = counter

        return highest
