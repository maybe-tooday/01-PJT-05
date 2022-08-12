import sys
# queue ?? 

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for num in range(1,T+1):
    N = int(input())
    N1 = (N // 2) + (N % 2) #2로 나눈몫 + 2로 나눈나머지 -> 짝수와 홀수를 나누기 위한 변수

    queue = list(input().split())
    queue_A = queue[:N1] 
    queue_B = queue[N1:]

    answer = []
    for i in range(len(queue_A)):
        answer.append(queue_A.pop(0)) #파이썬의 리스트는 큐처럼 사용가능!
        if len(queue_B) == 0:
            break
        answer.append(queue_B.pop(0))

    print(f'#{num}',*answer)