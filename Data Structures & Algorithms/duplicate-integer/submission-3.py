# The main idea here was to compare the set formed by the numbers of the array, this way there will be no repeated numbers.
# So, we just compare the original array with the final set length. If equal, no number was repeated.
# If different, the are repeated numbers.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            my_set.add(num)
        repeated = len(nums) != len(my_set)

        return repeated