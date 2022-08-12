import sys
import copy #리스트를 카피하기 위해 가져왔습니다.

sys.stdin = open("_등산로조성.txt")

def pprint(list):
    for _ in range(len(list)):
        print(list[_])

dx = [-1,0,0,1] #가로세로로만 탐색
dy = [0,-1,1,0]

T = int(input())

for testcase in range(1,T+1):

    N, K = map(int,input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    # print('main')
    # pprint(graph)
    # print('---------')
    max_ = 0 #꼭대기 높이 
    for num in range(N):
        if max(graph[num]) > max_:
            max_ = max(graph[num]) #dfs탐색 시작점 획득
    cnt_sum = 0
    for k in range(K+1):   #0~K 까지   
        for i in range(N):
            for j in range(N):
                subgraph = copy.deepcopy(graph) # -> 리스트를 복사하는 법을 찾아서 풀수 있었습니다.
                subgraph[i][j] -= k #판을 미리 만들어서 
                # print(graph,'main')
                # print(subgraph,'copy')
                for y in range(N):
                    for x in range(N):
                        stack =[]
                        if subgraph[y][x] == max_:                        
                            cnt = 1 # 길이측정 자신포함
                            stack.append((y,x,cnt))
                            while len(stack)!=0:
                                #visited = [[False] * N for _ in range(N)]
                                yy, xx, cnt = stack.pop()
                                for d in range(4):
                                    ny = yy + dy[d]
                                    nx = xx + dx[d]
                                    if not(-1 < ny < N and -1 < nx < N): #범위를 나가면 안돼
                                        #print(1)
                                        continue
                                    # if visited[ny][nx] == True: #한번 방문 했던것은 안돼 -> 필요없는 조건 같다
                                    #      print(2)
                                    #      continue
                                    if subgraph[ny][nx] >= subgraph[yy][xx]: #이동한곳의 높이가 높거나 같다
                                        #print(3)
                                        continue

                                    stack.append((ny,nx,cnt+1))

                                    if stack[len(stack)-1][2] > cnt_sum : 
                                        cnt_sum = stack[len(stack)-1][2]
                                    #print(stack)
                                    #visited[ny][nx] = True

    print(f'#{testcase}', cnt_sum)
    #print(cnt_sum)