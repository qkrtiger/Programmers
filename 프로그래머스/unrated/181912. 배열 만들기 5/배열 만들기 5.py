def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        if s < 0 or s + l > len(string):
            continue  # 부분 문자열을 추출할 수 없는 경우 스킵
        substring = string[s:s + l]  # s번 인덱스에서 시작하는 길이 l짜리 부분 문자열 추출
        try:
            num = int(substring)  # 추출한 부분 문자열을 정수로 변환
            if num > k:
                result.append(num)
        except ValueError:
            continue
    return result