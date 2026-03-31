class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            word_map = [0] * 26
            for char in word:
                position = ord(char) - ord('a')
                word_map[position] += 1
            t_word_map = tuple(word_map)
            if t_word_map in group:
                group[t_word_map].append(word)
            else:
                group[t_word_map] = [word]
        return list(group.values())