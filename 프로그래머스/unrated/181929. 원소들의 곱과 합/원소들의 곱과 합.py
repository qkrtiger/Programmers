def solution(num_list):
    product = 1
    total = 0

    for num in num_list:
        product *= num
        total += num

    # 원소들의 곱이 원소들의 합의 제곱보다 작으면 1을 반환, 그렇지 않으면 0을 반환
    if product < total ** 2:
        return 1
    else:
        return 0