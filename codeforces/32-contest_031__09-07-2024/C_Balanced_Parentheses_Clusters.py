for _ in range(int(input())):
    n = int(input())
    s = input()
    root = [i for i in range(2*n)]
    size = [1] * (2*n)

    def find(v):
        if v == root[v]:
            return v
        root[v] = find(root[v])
        return root[v]

    def union(v1, v2):
        root1, root2 = find(v1), find(v2)
        if root1 == root2:
            return
        if size[root1] > size[root2]:
            root[root2] = root1
            size[root1] += size[root2]
        else:
            root[root1] = root2
            size[root2] += size[root1]

    stk = []
    last_open = -1
    for i in range(n*2):
        if s[i] == '(':
            stk.append(i)
        else:
            j = stk.pop()
            union(j, i)

    # for i in range(len(s)):
    #     if s[i] == ')':
    #         continue
    #     stk = ['(']
    #     for j in range(i+1, len(s)):
    #         if s[j] == ')' and not stk:
    #             break
    #         elif s[j] == ')':
    #             stk.pop()
    #         else:
    #             stk.append('(')
    #         if not stk:
    #             union(i, j)

    uniq = set()
    for index in range(2*n):
        uniq.add(find(index))
    print(len(uniq))
