def solution(l, r):
    special_numbers = []
    
    for num in range(l, r + 1):
        if all(digit in ['0', '5'] for digit in str(num)):
            special_numbers.append(num)
    
    if not special_numbers:
        return [-1]
    
    return special_numbers