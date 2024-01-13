def solution(num_list):
    sorted_list = sorted(num_list)  # 리스트를 오름차순으로 정렬합니다.
    result = sorted_list[:5]  # 가장 작은 5개의 수를 추출합니다.
    return result