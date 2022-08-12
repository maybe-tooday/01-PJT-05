import sys

sys.stdin = open("_등산로조성.txt")

def pprint(list):
    for _ in range(len(list)):
        print(list[_])

dx = [-1,0,0,1] #가로세로로만 탐색
dy = [0,-1,1,0]

T = int(input())

for testcase in range(1,T+1):
    N, K = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]

    #pprint(graph)
    max_ = 0 #꼭대기 높이 
    for num in range(N):
        if max(graph[num]) > max_:
            max_ = max(graph[num]) #dfs탐색 시작점 획득
    cnt_sum = 0
    for k in range(K+1): #      
        for y in range(N):
            for x in range(N):
                stack =[]
                if graph[y][x] == max_:
                    for i in range(N):
                        for j in range(N):
                            subgraph = []
                            subgraph = graph
                            if not(y == i and x == j): # x 나 y 중 하나만 달라도                                
                                subgraph[i][j] -= k
                            cnt = 1 # 길이측정 자신포함
                            stack.append((y,x,cnt))
                            while len(stack)!=0:
                                #visited = [[False] * N for _ in range(N)]
                                y, x, cnt = stack.pop()
                                for d in range(4):
                                    ny = y + dy[d]
                                    nx = x + dx[d]
                                    if not(-1 < ny < N and -1 < nx < N): #범위를 나가면 안돼
                                        #print(1)
                                        continue
                                    # if visited[ny][nx] == True: #한번 방문 했던것은 안돼 -> 필요없는 조건 같다
                                    #      print(2)
                                    #      continue
                                    if subgraph[ny][nx] >= subgraph[y][x]: #이동한곳의 높이가 높거나 같다
                                        #print(3)
                                        continue
                                    
                                    stack.append((ny,nx,cnt+1))

                                    if cnt + 1 > cnt_sum :
                                        cnt_sum = cnt + 1
                                    #print(stack)
                                    #visited[ny][nx] = True

    print(f'#{testcase}', cnt_sum)

# K값을 어떻게 해야할지 아예 감을 잡지 못했습니다.