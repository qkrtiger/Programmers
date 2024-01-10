def solution(arr):
    stk = []  # 새로운 배열 stk 초기화

    i = 0  # 인덱스 i 초기값 설정
    while i < len(arr):  # i가 arr의 길이보다 작을 때까지 반복
        if not stk:  # stk가 빈 배열이라면
            stk.append(arr[i])  # arr[i]를 stk에 추가
        elif stk[-1] == arr[i]:  # stk의 마지막 원소가 arr[i]와 같으면
            stk.pop()  # stk의 마지막 원소를 제거
        else:  # stk의 마지막 원소가 arr[i]와 다르면
            stk.append(arr[i])  # stk의 맨 마지막에 arr[i]를 추가
        i += 1  # i에 1을 더한다

    return stk if stk else [-1]