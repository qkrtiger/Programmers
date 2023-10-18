def solution(arr):
    stk = []  # 새로운 배열 stk를 초기화
    i = 0  # i를 초기값 0으로 설정

    while i < len(arr):
        if not stk:  # stk가 빈 배열이면
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:  # stk의 마지막 원소가 arr[i]보다 작으면
            stk.append(arr[i])
            i += 1
        else:  # stk의 마지막 원소가 arr[i]보다 크거나 같으면
            stk.pop()

    return stk