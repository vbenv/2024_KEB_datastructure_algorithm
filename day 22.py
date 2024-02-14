# 호출하는 함수
def dfs(g, v, visited):
    visited[v] = True #0번을 초기화
    print(chr(ord('A')+v), end = ' ')
    #print(v, end=' ')
    for i in range(len(graph)):
        if g[v][i] == True and not visited[i]:
            dfs(g, i, visited)

graph = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]


# 전역변수
visited = [False] * len(graph)
dfs(graph, 0, visited)