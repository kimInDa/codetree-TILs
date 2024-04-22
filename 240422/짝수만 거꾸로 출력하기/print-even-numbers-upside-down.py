# 정수의 갯수 입력 받기
n = int(input())

# 짝수를 저장할 배열
even_arr = [];

# n개의 정수 입력 받기
for _ in range(n):
    num = int(input())

    # 입력된 수가 짝수이면 배열에 저장
    if(num!=0 and num % 2 == 0):
        even_arr.append(num)

# 배열 뒤집기
reversed_even_arr = even_arr[::-1]

# 짝수 배열 역순으로 출력하기
if len(reversed_even_arr) == 0:
    print(0)
else :
    for elem in reversed_even_arr:
        print(elem, end = " ")