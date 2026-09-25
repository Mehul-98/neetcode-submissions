class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+','*','/','-'):
                stack.append(token)
            else:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if token == '+':
                    ans = val2 + val1
                elif token == '*':
                    ans = val2 * val1
                elif token == '/':
                    ans = int(val2 / val1)
                elif token == '-':
                    ans = val2 - val1
                stack.append(ans)
        return int(stack[-1])

        