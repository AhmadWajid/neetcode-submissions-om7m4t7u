class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for pos, speed in pairs:
            end = ((target - pos) / speed)
            if not stack:
                stack.append(end)
            else:
                if stack[-1] < end:
                    stack.append(end)



        return len(stack)     