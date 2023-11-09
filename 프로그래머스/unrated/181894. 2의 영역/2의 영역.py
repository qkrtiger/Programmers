def solution(arr):
    if 2 not in arr:
        return [-1]

    start = 0
    end = len(arr) - 1

    while arr[start] != 2 or arr[end] != 2:
        if arr[start] != 2:
            start += 1
        if arr[end] != 2:
            end -= 1

    return arr[start:end+1]