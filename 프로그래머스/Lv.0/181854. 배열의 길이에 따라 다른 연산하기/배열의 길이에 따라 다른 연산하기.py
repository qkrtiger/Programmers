def solution(arr, n):
    if len(arr) % 2 == 1:  # arr의 길이가 홀수인 경우
        for i in range(0, len(arr), 2):  # 짝수 인덱스에 n을 더함
            arr[i] += n
    else:  # arr의 길이가 짝수인 경우
        for i in range(1, len(arr), 2):  # 홀수 인덱스에 n을 더함
            arr[i] += n

    return arr