
class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_map_s = defaultdict(int)
        freq_map_t = defaultdict(int)
        if len(s) == len(t):
            for i in range(len(s)):
                freq_map_s[s[i]] += 1 
                freq_map_t[t[i]] += 1 
        
        if freq_map_s == freq_map_t:
            return True
        else:
            return False