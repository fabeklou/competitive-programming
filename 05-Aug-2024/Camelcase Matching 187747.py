# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for querie in queries:
            q = deque(querie)
            p = deque(pattern)

            for _ in range(max(len(q), len(p))):
                if q and p and q[0] == p[0]:
                    q.popleft()
                    p.popleft()
                elif q and q[0].islower():
                    q.popleft()
                else:
                    break
            result.append(q == p)

        return result            
