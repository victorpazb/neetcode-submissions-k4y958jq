'''
Aqui usei uma abordagem simples de n2; não sei se podería ser feito de outra forma,
mas foi a forma mais rápida que me veio a mente.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, num  in enumerate(nums):
                if(i != j and nums[i] + nums[j] == target):
                    return [i, j]
        