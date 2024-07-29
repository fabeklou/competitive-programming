# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

string  = input()
stack = []
count = 0

for char in string:
    if char == '(':
        stack.append(char)
    else:
        if len(stack) == 0:
            pass
        else:
            stack.pop()
            count += 1
            
print(count*2)
