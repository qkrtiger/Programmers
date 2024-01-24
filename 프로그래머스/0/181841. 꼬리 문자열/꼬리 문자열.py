def solution(str_list, ex):
    # 결과 문자열을 초기화합니다.
    result = ""
    
    # 리스트의 각 문자열에 대해 반복합니다.
    for s in str_list:
        # 현재 문자열이 제외할 문자열을 포함하지 않으면 결과에 추가합니다.
        if ex not in s:
            result += s
            
    # 최종 결과 문자열을 반환합니다.
    return result