#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        noDupes = set()

        for num in nums:
            if num in noDupes:
                return True
            noDupes.add(num)

        return False