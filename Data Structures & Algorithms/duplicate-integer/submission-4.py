class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = defaultdict(int)
        for num in nums:
            if num in numMap:
                return True
            
            numMap[num] += 1
        
        return False