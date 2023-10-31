def solution(my_string):
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    # 접미사 배열을 사전순으로 정렬
    sorted_suffixes = sorted(suffixes)
    
    return sorted_suffixes