def solution(arr, delete_list):
    # delete_list의 원소를 제외한 arr의 원소를 유지한 새로운 리스트를 반환
    return [item for item in arr if item not in delete_list]