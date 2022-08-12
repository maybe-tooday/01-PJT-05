import sys

sys.stdin = open("_반반.txt")

T = int(input())

for num in range(1,T+1):
    S = input() #문자열 입력받기
    str_ = S
    cnt = []
    for s in str_:        
        cnt.append(str_.count(s))
    #print(cnt) #문자열에 문자가 2개씩들어와 있는것을 이용하여 같은 숫자를 센다
    # [2,2,2,2] 를 출력하면 두개의 서로다른문자 이며 두번등장한다
    if sum(cnt) == 8:
        print(f'#{num} Yes')
    else:
        print(f'#{num} No')