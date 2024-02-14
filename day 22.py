# 호출하는 함수
def dfs(g, i, visited):#g : graph, i : 횟수, visited: 방문 기록
    visited[i] = 1 #0번을 초기화
    print(chr(ord('A')+i), end = ' ')
    #print(i, end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]


# 전역변수
visited = [0] * len(graph)
dfs(graph, 0, visited)