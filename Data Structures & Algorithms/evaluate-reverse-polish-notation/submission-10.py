class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {"+", "*", "-", "/"}
        for char in tokens:
            if char in operation:
                second_num = stack.pop(-1)
                first_num = stack.pop(-1)
                if char == "+":
                    stack.append(second_num + first_num)
                if char == "-":
                    stack.append(first_num - second_num)
                if char == "*":
                    stack.append((first_num * second_num))
                if char == "/":
                    stack.append(int(first_num / second_num))
            else:
                stack.append(int(char))
        return int(stack[-1])