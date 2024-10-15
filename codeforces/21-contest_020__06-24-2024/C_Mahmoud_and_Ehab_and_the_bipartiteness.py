import sys, threading
def main():
    n = int(input())
    
    graph = [[] for _ in range(n)]
    edges = n - 1
    
    for _ in range(edges):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # partitionning the graph
    teams = {'A': set(), 'B': set()}


    def dfs(graph, pos, team, visited):
        visited.add(pos)
        
        if team == 'A':
            teams['A'].add(pos)
        else:
            teams['B'].add(pos)

        for node in graph[pos]:
            next_team = 'A' if team == 'B' else 'B'
            if node not in visited:
                dfs(graph, node, next_team, visited)


    dfs(graph, 0, 'A', set())
    print(len(teams['A']) * len(teams['B']) - edges)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
