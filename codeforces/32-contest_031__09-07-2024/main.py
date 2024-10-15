root = [i for i in range(len(accounts))]
size = [1] * len(accounts)

def find(account):
    if account == root[account]:
        return account
    root[account] = find(root[account])
    return root[account]

def union(account1, account2):
    root1, root2 = find(account1), find(account2)
    if root1 == root2:
        return
    if size[root1] > size[root2]:
        root[root2] = root1
        size[root1] += size[root2]
    else:
        root[root1] = root2
        size[root2] += size[root1]
