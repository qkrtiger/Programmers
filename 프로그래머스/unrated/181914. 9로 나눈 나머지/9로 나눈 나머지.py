def solution(number):
    # 문자열로 주어진 숫자를 각 자리 숫자로 분리
    digits = [int(digit) for digit in number]

    # 숫자의 각 자리 숫자의 합을 구함
    digit_sum = sum(digits)

    # 숫자의 각 자리 숫자의 합을 9로 나눈 나머지를 계산
    digit_sum_mod_9 = digit_sum % 9

    # 주어진 숫자를 9로 나눈 나머지를 구함
    number_mod_9 = int(number) % 9

    # 위에서 계산한 두 값을 비교하여 같다면 숫자를 9로 나눈 나머지를 반환, 다르다면 -1 반환
    if digit_sum_mod_9 == number_mod_9:
        return number_mod_9
    else:
        return -1
