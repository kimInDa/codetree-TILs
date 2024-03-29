# 변수 선언, 입력
n = int(input())
cnt = 'A'

# 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(" ", end = " ")
    
    # 영문자 출력
    for j in range(n - i):
        print(cnt, end = " ")
        cnt = chr(ord(cnt) + 1)
        if ord(cnt) > ord('Z'):
            cnt = 'A'
    
    print()






# n = 3인 경우 출력
# A B C
#   D E
#     F