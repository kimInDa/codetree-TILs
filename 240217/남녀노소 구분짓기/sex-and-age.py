# 변수 선언, 입력
gender = int(input())
age = int(input())

# 출력
if gender == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")