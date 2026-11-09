class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { "}": "{", ")": "(", "]": "["}
        for string in s:
            if string in mapping:
                if stack and stack[-1] == mapping[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
        return not stack
