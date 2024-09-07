# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = {}
        accs = [{'name': acc[0], 'email': set(acc[1:])} for acc in accounts]

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

        for index, acc in enumerate(accs):
            name, email = acc.get('name'), acc.get('email')
            if name not in visited:
                visited[name] = [index]
                continue
            for i in visited[name]:
                if email & accs[i].get('email'):
                    union(index, i)
            visited[name].append(index)

        # merge accounts
        merged_accs = [{'name': acc.get('name'), 'email': set()} for acc in accs]
        for index in range(len(accs)):
            merged_accs[find(index)]['email'] |= accs[index].get('email')

        return [
            [acc.get('name'), *sorted(acc.get('email'))]
            for acc in merged_accs if acc.get('email')
        ]
