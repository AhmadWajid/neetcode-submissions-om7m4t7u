class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = {}
        for word in strs:
            freq= [0]*26
            for letter in word:
                freq[ord(letter)- ord('a')] += 1
            tupled = tuple(freq)
            if tupled in grouper:
                grouper[tupled].append(word)
            else:
                grouper[tupled] = [word]
        return [v for v in grouper.values()]