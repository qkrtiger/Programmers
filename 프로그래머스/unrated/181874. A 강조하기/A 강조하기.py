def solution(myString):
    result = ''
    for char in myString:
        if char == 'a':
            result += 'A'
        elif char.isupper() and char != 'A':
            result += char.lower()
        else:
            result += char
    return result
