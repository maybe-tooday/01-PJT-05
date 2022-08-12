import sys

sys.stdin = open("_등산로조성.txt")

#K 값이 없을때 코드
#강사님들이 기본적인 구조를 만들고 하나씩 추가하셔서 조건을 뺴고 기본구조를 만들기 위해 제작하였습니다

def pprint(list):
    for _ in range(len(list)):
        print(list[_])

dx = [-1,0,0,1] #가로세로로만 탐색
dy = [0,-1,1,0]

T = int(input())

for testcase in range(T):
    N, K = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]

    #pprint(graph)
    max_ = 0 #꼭대기 높이 
    for num in range(N):
        if max(graph[num]) > max_:
            max_ = max(graph[num]) #dfs탐색 시작점 획득
    cnt_sum = 0

    for y in range(N):
        for x in range(N):
            stack =[]
            if graph[y][x] == max_:
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
                        if graph[ny][nx] >= graph[y][x]: #이동한곳의 높이가 높거나 같다
                            #print(3)
                            continue
                        
                        stack.append((ny,nx,cnt+1))

                        if cnt + 1 > cnt_sum :
                            cnt_sum = cnt + 1
                        #print(stack)
                        #visited[ny][nx] = True

    print(cnt_sum)
