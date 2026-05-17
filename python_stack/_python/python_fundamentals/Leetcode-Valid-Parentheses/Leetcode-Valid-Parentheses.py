class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in match:
                top = stack.pop() if stack else ""
                if top != match[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

        
