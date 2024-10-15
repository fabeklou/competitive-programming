import sys

ipt = sys.stdin.readline
n = int(input())
stk = []
count = 0
nxt = 1

for _ in range(n*2):
    cmd = ipt()

    if cmd[0] == 'a':
        num = int(cmd.split()[1])
        stk.append(num)
    else:
        if not stk:
            pass
        elif stk[-1] == nxt:
            stk.pop()
        else:
            stk = []
            count += 1
        nxt += 1

print(count)
