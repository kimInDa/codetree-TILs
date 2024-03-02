# 변수 선언
satisfied = True

# 5개의 수가 모두 3의 배수인지 판별
for i in range(1, 6):
    # 입력
    n = int(input())
    
    # 하나라도 3의 배수가 아니라면 거짓
    if n % 3 != 0:
        satisfied = False


# 모두 3의 배수라면 1, 아니면 0을 출력
if satisfied == True:
    print(1)
else:
    print(0)