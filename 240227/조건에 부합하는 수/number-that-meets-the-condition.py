# 변수 선언, 입력
a = int(input())

# 1부터 a까지 조건을 모두 만족하지 않는 수 출력
# 조건1. 짝수이면서 4의 배수가 아닌 수
# 조건2. 8로 나눈 몫이 짝수인 수
# 조건3. 7로 나눈 나머지가 4보다 작은 수
for i in range(1, a + 1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    if (i // 8) % 2 == 0:
        continue
    if (i % 7) < 4:
        continue
    print(i, end = ' ')