from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1
        
        return sorted(numMap, key=lambda x: numMap[x])[-k:]