def solution(my_string, is_prefix):
    # my_string의 접두사 리스트 생성
    prefixes = [my_string[:i] for i in range(1, len(my_string) + 1)]
    
    # is_prefix가 my_string의 접두사 중 하나인지 확인
    if is_prefix in prefixes:
        return 1
    else:
        return 0