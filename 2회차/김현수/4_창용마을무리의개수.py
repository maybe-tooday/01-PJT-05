import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for num in range(1,T+1):
    N, M = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a ,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print('그래프',graph)

    visited = [False]*(N+1)
    #print(visited)
    cnt = 0 #N의 최소값이 1이므로 무조건 한개의 무리는 존재하지만 stack_before = []덕분에 처음에 바로 카운팅.
    for i in range(1,N+1):
        stack = []
        stack.append(i)
        stack_before = [] 

        if not visited[i]:
            cnt += 1
            visited[i] = True

        while len(stack) != 0:
            number = stack.pop()
            num_values = graph[number]

            for n in num_values:
                if not visited[n]: #방문하지 않았을 떄만 넣어준다.
                    stack.append(n)
                    # print(stack)
                    # if len(stack) > len(stack_before):
                    #     cnt += 1
                    # stack_before = stack
                    visited[n] = True
                    
    print(f'#{num}',cnt)