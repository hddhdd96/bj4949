import sys

while True:
    s = sys.stdin.readline().rstrip()
    temp = True
    stack = []

    if s == ".":
        break

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if temp == True and not stack:
        print('yes')
    else:
        print('no')