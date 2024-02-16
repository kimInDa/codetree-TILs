# 변수 선언, 출력
a = input().split()
a_age, a_gender = int(a[0]), a[1]

b = input().split()
b_age, b_gender = int(b[0]), b[1]

# 출력
if a_age < 19 or b_age < 19 or a_gender == "W" or b_gender == "W":
    print(1)
else:
    print(0)