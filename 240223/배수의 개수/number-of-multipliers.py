# 변수 선언
cnt3, cnt5 = 0, 0

# 입력, 카운트
for i in range(10):
    n = int(input())
    
    if n % 3 == 0:
        cnt3 += 1
    if n % 5 == 0:
        cnt5 += 1

# 출력
print(cnt3, cnt5)