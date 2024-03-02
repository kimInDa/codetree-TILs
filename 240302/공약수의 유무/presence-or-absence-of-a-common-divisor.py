# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

satisfied = False

# a와 b 사이에 1920과 2880의 공약수가 존재하는지 판별
for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        satisfied = True

# 공약수가 존재한다면 1, 존재하지 않는다면 0 출력
if satisfied == True:
    print(1)
else:
    print(0)