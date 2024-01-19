def solution(num_str):
    num_sum = 0
    for digit in num_str:
        num_sum += int(digit)
    return num_sum