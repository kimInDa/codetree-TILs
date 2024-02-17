# 변수 선언, 입력
a = input().split()
a_symp = a[0]
a_temp = int(a[1])

b = input().split()
b_symp = b[0]
b_temp = int(b[1])

c = input().split()
c_symp = c[0]
c_temp = int(c[1])


if a_symp == "Y" and a_temp >= 37:
    if (b_symp == "Y" and b_temp >= 37) or (c_symp == "Y" and c_temp >= 37):
        print("E")
    else:
        print("N")
else:
    if (b_symp == "Y" and b_temp >= 37) and (c_symp == "Y" and c_temp >= 37):
        print("E")
    else:
        print("N")