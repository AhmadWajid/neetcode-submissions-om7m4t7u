class Solution:

    def encode(self, strs: List[str]) -> str:
        full_str = ""
        for word in strs:
            temp = f"{len(word)}#{word}"
            full_str += temp
        return full_str


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            start = i
            while s[start] != "#":
                start += 1
            num = s[i:start]
            start += 1
            word = s[start:start + int(num)]
            decoded.append(word)
            i = start+int(num)
        return decoded