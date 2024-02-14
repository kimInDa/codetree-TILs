# 변수 선언, 입력
arrA = input().split()
arrB = input().split()

mathA = int(arrA[0])
engA = int(arrA[1])

mathB = int(arrB[1])
engB = int(arrB[1])

# 출력
if mathA > mathB and engA > engB:
    print(1)
else:
    print(0)