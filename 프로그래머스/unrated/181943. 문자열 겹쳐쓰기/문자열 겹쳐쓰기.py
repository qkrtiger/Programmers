def solution(my_string, overwrite_string, s):
    # 주어진 인덱스 s 이전과 이후 부분을 추출
    part1 = my_string[:s]
    part2 = my_string[s + len(overwrite_string):]
    
    # 새로운 문자열을 생성하여 이전 부분, 덮어쓸 문자열, 그리고 이후 부분을 합침
    result = part1 + overwrite_string + part2
    
    return result