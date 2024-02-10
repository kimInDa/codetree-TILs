# 변수 선언, 입력
inp = input().split()
height = int(inp[0])
weight = int(inp[1])

# 체질량 지수
bmi = (weight * (100 ** 2)) // (height ** 2)

# 출력
print(bmi)
if bmi >= 25:
    print("Obesity")