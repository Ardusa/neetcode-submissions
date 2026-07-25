class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = dict()
        for i in nums:
            if str(i) in mapping:
                return True
            
            mapping[str(i)] = True

        return False