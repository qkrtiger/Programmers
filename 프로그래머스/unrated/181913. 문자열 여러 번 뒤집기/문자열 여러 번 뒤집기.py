def reverse_substring(s, e, my_string):
    # 문자열을 리스트로 변환하여 s부터 e까지의 부분 문자열을 뒤집습니다.
    my_list = list(my_string)
    my_list[s:e+1] = reversed(my_list[s:e+1])
    # 리스트를 문자열로 변환하여 반환합니다.
    return ''.join(my_list)

def solution(my_string, queries):
    for query in queries:
        s, e = query
        my_string = reverse_substring(s, e, my_string)
    return my_string