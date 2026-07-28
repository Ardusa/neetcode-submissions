class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0 for _ in range(len(nums))]

        current = nums[0]

        for i in range(1, len(nums)):
            ret[i] = current
            current *= nums[i]
        
        current = nums[-1]
        
        for k in range(len(nums) - 2, 0, -1):
            ret[k] *= current
            current *= nums[k]
        
        ret[0] = current
        
        return ret