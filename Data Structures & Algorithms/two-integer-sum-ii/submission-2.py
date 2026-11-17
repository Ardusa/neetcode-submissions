class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = 0, len(numbers) - 1

        while leftPtr < rightPtr:
            Sum = numbers[leftPtr] + numbers[rightPtr]

            if Sum < target:
                leftPtr += 1
            
            elif Sum > target:
                rightPtr -= 1
            
            else:
                return [leftPtr + 1, rightPtr + 1]
            
        return tuple(0, 0)