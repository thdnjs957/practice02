# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(*arg):
    sum = 0
    for i in arg:
        sum += i
    print(sum)

sum(0)
sum(1,2)
sum(2,4,5,7)