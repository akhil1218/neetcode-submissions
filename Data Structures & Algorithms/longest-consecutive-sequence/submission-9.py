class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        max=0
        if n>0:
            # for i in range(n):
            #     for j in range(i+1,n):
            #         if nums[i]>nums[j]:
            #             t=nums[i]
            #             nums[i]=nums[j]
            #             nums[j]=t
            nums.sort()

            cnt=1
            for k in range(n-1):
                if nums[k]+1==nums[k+1]:
                    cnt+=1
                    if max < cnt:
                        max = cnt
                elif nums[k]==nums[k+1]:
                    continue
                elif nums[k]+1>nums[k]:
                    cnt=1
            if max < cnt:
                max = cnt
        return max