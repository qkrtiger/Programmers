def solution(strArr):
    for i in range(len(strArr)):
        # 짝수번째 인덱스일 때 문자열 모두를 소문자로 변환
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        # 홀수번째 인덱스일 때 문자열 모두를 대문자로 변환
        else:
            strArr[i] = strArr[i].upper()
    return strArr
