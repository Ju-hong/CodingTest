
from sys import stdin
from collections import deque

n, m, k = map(int, stdin.readline().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    graph[i][j], graph[j][i] = 1, 1

visited_b = [0 for _ in range(n+1)]
visited_d = [0 for _ in range(n+1)]


def BFS(k):
    que = deque([k]) # n
    visited_b[k] = 1 ## 몇개의?

    while que :
        k = que.popleft()
        print(k, end = " ") ##
        for i in range(1, n+1):
            if not visited_b[i] and graph[k][i]:
                que.append(i)
                visited_b[i] = 1

def DFS(k):
    visited_d[k] = 1
    print(k, end = " ")
    for i in range(1, n+1):
        if not visited_d[i] and graph[k][i]:
            DFS(i)

DFS(k)
print()
BFS(k)


