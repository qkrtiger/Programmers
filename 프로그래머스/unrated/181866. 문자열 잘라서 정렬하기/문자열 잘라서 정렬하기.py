def solution(myString):
    # "x"를 기준으로 문자열을 잘라 배열을 만듭니다.
    split_strings = myString.split("x")
    
    # 빈 문자열을 제거합니다.
    split_strings = [s for s in split_strings if s]
    
    # 배열을 사전순으로 정렬합니다.
    sorted_strings = sorted(split_strings)
    
    # 정렬된 배열을 반환합니다.
    return sorted_strings