class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        count_of_s1 = {}
        count_of_s2 = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            count_of_s1[s1[i]] = 1 +  count_of_s1.get(s1[i],0)
        for r in range(len(s2)):
            count_of_s2[s2[r]] = 1 +  count_of_s2.get(s2[r],0)
            while (r-l+1) > len(s1):
                count_of_s2[s2[l]] -= 1
                if count_of_s2[s2[l]] == 0:
                    del count_of_s2[s2[l]]
                l += 1
            if count_of_s1 == count_of_s2:
                return True

        return False

