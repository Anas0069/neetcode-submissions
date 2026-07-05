class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_S, counter_T = {},{}
        for i in range(len(s)):
            counter_S[s[i]] = 1 + counter_S.get(s[i],0)
            counter_T[t[i]] = 1 + counter_T.get(t[i],0)
        for n in counter_S:
            if counter_S != counter_T:
                return False
        return True
            

        