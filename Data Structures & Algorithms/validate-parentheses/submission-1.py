class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}':'{', ']' : '['}
        for i in s:
            if i not in pair:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
        return not stack

