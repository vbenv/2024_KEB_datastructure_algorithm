# 호출하는 함수
def dfs(g, i, visited):#g : graph, i : 횟수, visited: 방문 기록
    visited[i] = 1 #0번을 초기화
    print(f'{name_ary[i]}', end=' ')
    #print(chr(ord('A')+i), end = ' ')
    #print(i, end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

name_ary = ["문별", "솔라", "휘인", "쯔위", '선미', "화사"]
mb, sl, hi, zz, sm, hs = 0, 1, 2, 3, 4, 5
graph = [
    [0, 1, 1, 0, 0, 0],  #mb
    [1, 0, 0, 1, 0, 0],  #sl
    [1, 0, 0, 1, 0, 0],  #hi
    [0, 1, 1, 0, 1, 1],  #zz
    [0, 0, 0, 1, 0, 1],  #sm
    [0, 0, 0, 1, 1, 0]   #hs
]


# 전역변수
visited = [0] * len(graph)
#visited = [0 for _ in range(len(graph))] #위랑 같은 코드

dfs(graph, 0, visited)