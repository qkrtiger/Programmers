def solution(a, b, c):
    if a == b == c:
        # 세 숫자가 모두 같은 경우
        score = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or a == c or b == c:
        # 두 숫자가 같은 경우
        score = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        # 모든 숫자가 다른 경우
        score = a + b + c
    
    return score

# set 활용
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
