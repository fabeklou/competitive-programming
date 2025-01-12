# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orderedStrs = ["".join(sorted(s)) for s in strs]
        visited = {}
        result = []
        for index, word in enumerate(orderedStrs):
            if word in visited:
                result[visited[word]].append(strs[index])
            else:
                visited[word] = len(result)
                result.append([strs[index]])
        return result
