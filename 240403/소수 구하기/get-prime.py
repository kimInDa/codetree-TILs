# 변수 선언, 입력
n = int(input())

# 1이상 n이하의 수 중 소수를 오름차순으로 출력
for i in range(2, n + 1):
    for j in range(2, i + 1):
        if i == j:
            print(i, end = ' ')

        if i % j == 0:
           break;