def solution(numbers, n):
    total_sum = 0
    for num in numbers:
        total_sum += num
        if total_sum > n:
            return total_sum
    return total_sum