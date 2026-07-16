class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                second = stack.pop()
                first = stack.pop()
                result = second + first
                stack.append(result)
            elif i == '-':
                second = stack.pop()
                first = stack.pop()
                result = first - second
                stack.append(result)
            elif i == '*':
                second = stack.pop()
                first = stack.pop()
                result = second * first
                stack.append(result)
            elif i == '/':
                second = stack.pop()
                first = stack.pop()
                result = first/second
                stack.append(int(result))
            else:
                stack.append((int(i)))
        return stack[-1]

        