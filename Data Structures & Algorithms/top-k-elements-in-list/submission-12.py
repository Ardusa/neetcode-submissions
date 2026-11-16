import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1

        heap = []

        for number, frequency in numMap.items():
            tup = (frequency, number)

            heapq.heappush(heap, tup)

            if len(heap) > k:
                pop = heapq.heappop(heap)

        ret = []

        for x in heap:
            ret.append(x[1])

        return ret
