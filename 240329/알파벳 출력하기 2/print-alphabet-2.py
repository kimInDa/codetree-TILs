# 변수 선언, 입력
n = int(input())
cnt = 65

# 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(" ", end = " ")
    
    # 영문자 출력
    for j in range(n - i):
        print(chr(cnt), end = " ")
        cnt += 1
        if cnt > ord('Z'):
            cnt = ord('A')
    
    print()






# n = 3인 경우 출력
# A B C
#   D E
#     F