class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            i_s={}
            n=len(s)
            fs=""
            for i in range(n):
                if s[i] not in i_s and t[i] not in i_s.values():
                    i_s[s[i]]=t[i]
            for i in range(n):
                fs=fs+i_s.get(s[i],"")
            if fs==t:
                return True
            else:
                return False
        else:
            return False
        