import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
#aeiou = ['a','e','i','o','u']

for num in range(1,T+1):
    
    S = input()
    answer = S.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    #문자열에서 relace를 연속으로 적용하여 처리
    print(f'#{num}',answer)