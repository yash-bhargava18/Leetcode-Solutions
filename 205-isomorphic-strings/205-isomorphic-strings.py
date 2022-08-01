class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        
        for i in range(len(s)):
            if s[i] in h1:
                if h1[s[i]] != t[i]:
                    return False
            else:
                h1[s[i]] = t[i]
            
            if(t[i] in h2):
                if h2[t[i]] != s[i]:
                    return False
            else:
                h2[t[i]] = s[i]
            
        return True