def solution(arr, intervals):
    # 첫 번째 구간에 해당하는 배열
    first_interval = arr[intervals[0][0]:intervals[0][1] + 1]
    
    # 두 번째 구간에 해당하는 배열
    second_interval = arr[intervals[1][0]:intervals[1][1] + 1]
    
    # 두 배열을 앞뒤로 붙여서 새로운 배열 생성
    result = first_interval + second_interval
    
    return result