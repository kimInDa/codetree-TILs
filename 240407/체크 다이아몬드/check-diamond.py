# 변수 선언, 입력
n = int(input())

# 상단 부분 그리기
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

# 하단 부분 그리기
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)


# 풀이
# 변수 선언 및 입력
# n = int(input())

# # 모양에 맞게 위쪽 별을 출력합니다.
# for i in range(n):
# 	for _ in range(n - i - 1):
# 		print(" ", end="")
# 	for _ in range(i + 1):
# 		print("* ", end="")
# 	print()

# # 모양에 맞게 아래쪽 별을 출력합니다.
# for i in range(n-2, -1, -1):
# 	for _ in range(n - i - 1):
# 		print(" ", end="")
# 	for _ in range(i + 1):
# 		print("* ", end="")
# 	print()