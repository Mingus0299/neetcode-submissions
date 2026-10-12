class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ls = []

        for t in tokens:
            if t == "+":
                ls.append(ls.pop() + ls.pop())

            elif t == "-":
                a, b = ls.pop(), ls.pop()
                ls.append(b - a)

            elif t == "*":
                ls.append(ls.pop() * ls.pop())

            elif t == "/":
                a, b = ls.pop(), ls.pop()
                ls.append(int(float(b) / a))

            else:
                ls.append(int(t))

        return ls[0]
