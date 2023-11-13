def solution(num_list, n):
    # n번째 원소부터의 리스트와 n번째 원소까지의 리스트로 나누기
    first_part = num_list[n:]
    second_part = num_list[:n]

    # 두 부분의 리스트를 순서를 바꿔서 연결하기
    result = first_part + second_part

    return result