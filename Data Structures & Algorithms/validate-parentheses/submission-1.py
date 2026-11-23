class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')':'(', ']':'[', '}':'{'}
        for p in s:
            if p in ('(', '[', '{'):
                stack.append(p)
            else:
                if stack and stack[-1] == close[p]:
                    stack.pop()
                else:
                    return False
        
        return not stack