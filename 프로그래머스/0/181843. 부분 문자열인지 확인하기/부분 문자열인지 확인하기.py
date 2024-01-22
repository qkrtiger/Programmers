def solution(my_string, target):
    # target이 my_string의 부분 문자열이면 1을, 아니면 0을 반환
    return 1 if target in my_string else 0
