class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        
        for num in nums:
            freqMap[num] += 1
        
        print(dict(freqMap))

        freqSet = [ [] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            freqSet[freq].append(num)
        
        print(freqSet)

        ret = list()

        for i in range(len(freqSet) - 1, 0, -1):
            for num in freqSet[i]:
                if (len(ret) == k):
                    return ret

                ret.append(num)
            
        return ret