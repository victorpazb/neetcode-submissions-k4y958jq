class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated = False
        my_set = set()
        for num in nums:
            my_set.add(num)
        repeated = len(nums) != len(my_set)

        return repeated
        