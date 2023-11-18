def solution(num_list):
    odd_sum = sum(num_list[::2])
    even_sum = sum(num_list[1::2])
    
    if odd_sum >= even_sum:
        return odd_sum
    else:
        return even_sum