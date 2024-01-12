def solution(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    if len_arr1 != len_arr2:  # 배열의 길이가 다른 경우
        return 1 if len_arr1 > len_arr2 else -1
    else:  # 배열의 길이가 같은 경우
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)
        if sum_arr1 != sum_arr2:  # 배열 원소의 합이 다른 경우
            return 1 if sum_arr1 > sum_arr2 else -1
        else:  # 배열 원소의 합이 같은 경우
            return 0