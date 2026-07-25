class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = {}

        for i, num in enumerate(nums):
            gap = target - num

            if gap in targetMap:
                return sorted([i, targetMap[gap]])
            
            targetMap[num] = i
        
        return [0, 0]
