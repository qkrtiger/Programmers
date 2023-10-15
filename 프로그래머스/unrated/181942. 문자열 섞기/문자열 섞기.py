def solution(str1, str2):
    answer = ''

    # 두 문자열 중에서 짧은 문자열의 길이를 찾습니다.
    min_len = min(len(str1), len(str2))

    # 두 문자열을 번갈아가면서 한 문자씩 출력합니다.
    for i in range(min_len):
        answer += str1[i] + str2[i]

    # 길이가 다른 나머지 부분을 출력합니다.
    answer += str1[min_len:] + str2[min_len:]

    return answer

# 예시
str1 = "abc"
str2 = "12345"
result = solution(str1, str2)
print(result)  # "a1b2c345"
