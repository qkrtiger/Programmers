def solution(my_string, index_list):
    result = ""
    for index in index_list:
        if 0 <= index < len(my_string):
            result += my_string[index]
    return result
