class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=-1
        for i in range(n-1,-1,-1):
            curr=arr[i]
            arr[i]=res
            res=max(res,curr)
        return arr




        