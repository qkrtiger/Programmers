def solution(myString, pat):
    index = myString.rindex(pat)
    return myString[:index]+pat