def solution(n_str):
    # 문자열의 첫 글자부터 순회하면서 0이 아닌 문자가 나올 때까지 슬라이싱
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]
    return '0'  # 모든 문자가 0인 경우