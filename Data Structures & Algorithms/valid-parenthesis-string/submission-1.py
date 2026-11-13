class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the minimum and maximum possible open parentheses
        leftMin = 0
        leftMax = 0

        for c in s:
            if c == "(":
                # Opening bracket adds one unmatched '('
                leftMin += 1
                leftMax += 1

            elif c == ")":
                # Closing bracket removes one unmatched '('
                leftMin -= 1
                leftMax -= 1

            else:
                # '*' can be ')', '(' or empty
                # Min assumes ')' and max assumes '('
                leftMin -= 1
                leftMax += 1

            # Even the maximum possible openings can't match the ')'
            if leftMax < 0:
                return False

            # Can't have fewer than 0 unmatched openings
            leftMin = max(leftMin, 0)

        # Valid if at least one interpretation closes everything
        return leftMin == 0