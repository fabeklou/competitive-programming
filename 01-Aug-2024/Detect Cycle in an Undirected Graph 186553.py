# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List


class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = set()

		def dfs(node, parent):
            visited.add(node)
		    for neighbor in adj[node]:
		        if neighbor not in visited:
		            if dfs(neighbor, node):
		                return True
		        elif neighbor != parent:
		            return True
            return False

		for node in range(V):
		    if node not in visited:
		        if dfs(node, -1):
		            return 1

		return 0