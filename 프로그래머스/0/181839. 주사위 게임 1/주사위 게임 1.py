def solution(a, b):
    # 두 수 모두 홀수인 경우
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    # 두 수 중 하나만 홀수인 경우
    elif (a % 2 == 1 and b % 2 == 0) or (a % 2 == 0 and b % 2 == 1):
        return 2 * (a + b)
    # 두 수 모두 홀수가 아닌(짝수인) 경우
    else:
        return abs(a - b)

# 예시로 1과 6을 입력했을 때의 점수를 확인해봅시다.
print(solution(1, 6))  # 이 경우에는 하나만 홀수이므로 2 * (1 + 6) = 14 점을 얻습니다.
