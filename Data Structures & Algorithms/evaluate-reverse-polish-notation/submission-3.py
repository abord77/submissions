from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    second_num = stack.pop()
                    first_num = stack.pop()
                    stack.append(first_num + second_num)
                case "-":
                    second_num = stack.pop()
                    first_num = stack.pop()
                    stack.append(first_num - second_num)
                case "*":
                    second_num = stack.pop()
                    first_num = stack.pop()
                    stack.append(first_num * second_num)
                case "/":
                    second_num = stack.pop()
                    first_num = stack.pop()
                    stack.append(int(first_num / second_num))
                case _:
                    stack.append(int(token))

        return stack[0]
            