# 변수 선언, 입력
n = int(input())
prod = 1

# 1부터 10까지 1씩 증가시키며 곱을 구하다가 곱의 값이 n 이상이되는 순간 곱해진 수를 출력
for i in range(1, 11):
    prod *= i
    if prod >= n:
        print(i)
        break