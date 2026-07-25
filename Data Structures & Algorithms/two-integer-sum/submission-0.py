class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict() # remainder of target - nums[index] : index

        for i, num in enumerate(nums):
            if num in mapping:
                print(mapping, num)
                return [mapping[num], i]
                # return [i, mapping[remainder]]

            remainder = target - num
            mapping[remainder] = i
            