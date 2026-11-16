class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPtr, rightPtr = 0, len(nums) - 1
        leftSum, rightSum = 1, 1
        ret = [1 for _ in range(len(nums))]

        while leftPtr < len(nums):
            ret[leftPtr] = ret[leftPtr] * leftSum
            ret[rightPtr] = ret[rightPtr] * rightSum

            leftSum *= nums[leftPtr]
            rightSum *= nums[rightPtr]

            leftPtr += 1
            rightPtr -= 1

        return ret