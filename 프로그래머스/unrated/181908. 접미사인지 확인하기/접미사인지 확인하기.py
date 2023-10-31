def solution(my_string, is_suffix):
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    # is_suffix와 일치하는 접미사를 찾아 1을 반환
    if is_suffix in suffixes:
        return 1
    else:
        return 0

//endswitch 사용
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))
