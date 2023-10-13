n = int(input())

if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")


# 비트연산 & 슬라이싱 활용

n=int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")
