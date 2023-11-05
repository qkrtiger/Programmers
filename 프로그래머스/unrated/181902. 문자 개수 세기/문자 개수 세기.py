def solution(my_string):
    # 52개의 요소를 가진 배열을 0으로 초기화
    count_array = [0] * 52

    for char in my_string:
        if 'A' <= char <= 'Z':
            # 대문자 알파벳인 경우
            index = ord(char) - ord('A')  # A=0, B=1, ..., Z=25
        elif 'a' <= char <= 'z':
            # 소문자 알파벳인 경우
            index = 26 + ord(char) - ord('a')  # a=26, b=27, ..., z=51
        else:
            # 알파벳이 아닌 경우, 무시
            continue

        # 해당 알파벳의 개수를 증가
        count_array[index] += 1

    return count_array