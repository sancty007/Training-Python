
from unittest import result


maList =[3, 5, 8, 2, 11, 7]

target = 14
class Solution(object):
    def __init__(self) -> None:
        pass
    def twoSum(self, nums, target)-> None:
        list_simple = []
        indice =  []

        for i , num in enumerate(nums):
            complement = target - num
            list_simple.append(complement)
            indice.append(i)
        return self.additionNum(list_simple,indice,target)

    def additionNum(self ,list_simple,indice,target):
        n = len(list_simple)
        for i in range(n - 1) :
            for j in range(i+1 , n) :
                if list_simple[i] + list_simple[j] == target :
                    return [i,j]





#result = solution.twoSum(maList,target)

#print(result)
solution =Solution()
result = solution.twoSum(maList, target)

print(result)