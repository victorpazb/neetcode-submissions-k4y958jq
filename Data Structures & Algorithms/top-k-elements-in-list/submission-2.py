class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for index, num in enumerate(nums):
            myMap.setdefault(num, 0)
            myMap[num] += 1
        
        return (sorted(myMap, key=lambda x: myMap[x], reverse=True))[:k]

        