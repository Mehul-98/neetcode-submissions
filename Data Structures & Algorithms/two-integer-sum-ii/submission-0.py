class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        result = ["",""]
        while(i < j):
            if(numbers[i]+numbers[j] == target):
                result[0] = i+1
                result[1] = j+1
                break
            elif(numbers[i]+ numbers[j] < target):
                i += 1
            else:
                j -= 1
        return result
        