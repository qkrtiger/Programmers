def solution(num_list):
    odd_digits = "".join(str(num) for num in num_list if num % 2 != 0)
    even_digits = "".join(str(num) for num in num_list if num % 2 == 0)

    odd_sum = int(odd_digits) if odd_digits else 0
    even_sum = int(even_digits) if even_digits else 0

    return odd_sum + even_sum
