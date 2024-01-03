def solution(myString, pat):
    converted_string = myString.replace("A", "X").replace("B", "A").replace("X", "B")
    
    if pat in converted_string:
        return 1
    else:
        return 0
