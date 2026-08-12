class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for letter in s:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        for letter in t:
            if letter in freq:
                freq[letter] -= 1
                if freq[letter] == 0:
                    del freq[letter]
        return len(freq) == 0               