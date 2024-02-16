# 변수 선언, 입력
A_arr = input().split()
B_arr = input().split()

A_math = int(A_arr[0])
A_eng = int(A_arr[1])
B_math = int(B_arr[0])
B_eng = int(B_arr[1])

# 출력
if (A_math > B_math) or (A_math == B_math and A_eng > B_eng):
    print("A")
else:
    print("B")