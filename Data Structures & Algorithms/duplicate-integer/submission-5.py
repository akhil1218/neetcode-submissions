class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)-1
        nums.sort()
        for i in range(n):
            if nums[i]==nums[i+1]:
                return True
        return False