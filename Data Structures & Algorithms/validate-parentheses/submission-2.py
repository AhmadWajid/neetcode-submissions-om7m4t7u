class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = { "}": "{", ")": "(", "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
            elif stack == []:
                return False
            elif stack and char_map[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack