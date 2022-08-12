import sys

sys.stdin = open("_Flatten.txt")

for num in range(1,10+1):
    number = int(input())
    boxlist = list(map(int,input().split()))

    for _ in range(number): #받은 숫자 만큼 반복할껀데
        #그중에서 가장큰값 -1 하고 가장작은값 +1을 반복한다.
        check_max = 0
        check_min = 0
        max_box = max(boxlist)
        min_box = min(boxlist)
        cnt = 0
        for n in range(100): #가로길이가 100이다
            if boxlist[n] == max_box and check_max == 0:
                check_max = 1 #한루틴에 한번만 하도록
                boxlist[n] -= 1
                #cnt += 1

            if boxlist[n] == min_box and check_min == 0:
                check_min = 1
                boxlist[n] += 1
                #cnt -= 1
    #print(cnt) 반복분에 둘다 잘들어가면 0이 출력되야한다.
    print(f'#{num}',max(boxlist)-min(boxlist))