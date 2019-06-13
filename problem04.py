# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요
num = 99
input = str(num)

def cal_count(input):
    count = 0
    list_input = list(input)
    for i in range(len(list_input)):
        if(int(list_input[i]) % 3 == 0):
            count += 1
    return count

for i in range(1,num):
    if(cal_count(str(i)) != 0):
        print("{0}:{1}".format(i,'짝'* cal_count(str(i))))
