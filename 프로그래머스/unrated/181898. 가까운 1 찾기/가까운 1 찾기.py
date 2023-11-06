def solution(arr, idx):
    # 초기값으로 -1을 설정
    result = -1

    for i in range(idx, len(arr)):
        if arr[i] == 1:
            # idx보다 크면서 값이 1인 첫 번째 인덱스를 찾으면 결과로 반환
            result = i
            break

    return result