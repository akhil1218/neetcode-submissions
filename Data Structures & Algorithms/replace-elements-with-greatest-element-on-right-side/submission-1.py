class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        for i in range(n):
            res=0
            if i+1==n:
                res=-1
            for j in range(i+1,n):
                if j+1==n:
                    res=max(res,arr[j])
                else:
                    if arr[j]>arr[j+1]:
                        res=max(res,arr[j])
                    else:
                        res=max(res,arr[j+1])
            arr[i]=res
        return arr

        