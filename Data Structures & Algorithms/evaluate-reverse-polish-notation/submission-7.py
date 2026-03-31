class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                first = stack.pop()
                second = stack.pop()
                first = int(first)
                second = int(second)
                if token == "+":
                    new_val = second + first
                elif token == "-":
                    new_val = second - first
                elif token == "*":
                    new_val = second * first
                elif token == "/":
                    new_val = second / first
                stack.append(new_val)
            else:
                stack.append(int(token)) 
        return int(stack[-1])
                                                            