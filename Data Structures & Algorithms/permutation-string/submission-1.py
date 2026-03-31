class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c_s1 = {}
        c_s2 = {}
        for i in range(len(s1)):
            if s1[i] in c_s1:
                c_s1[s1[i]] += 1
            else:
                c_s1[s1[i]] = 1
            if s2[i] in c_s2:
                c_s2[s2[i]] += 1
            else:
                c_s2[s2[i]] = 1
        if c_s1 == c_s2:
            return True
        for i in range(len(s1), len(s2)):
            if s2[i] in c_s2:
                c_s2[s2[i]] += 1
            else:
                c_s2[s2[i]] = 1 
            # decrease the left window
            c_s2[s2[i - len(s1)]] -= 1
            if c_s2[s2[i - len(s1)]] == 0:
                del c_s2[s2[i - len(s1)]]
            if c_s1 == c_s2:
                return True  
        return False