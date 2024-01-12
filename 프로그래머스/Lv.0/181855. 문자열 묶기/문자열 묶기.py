def solution(strArr):
    length_dict = {}

    for str in strArr:
        if len(str) in length_dict:
            length_dict[len(str)] += 1
        else:
            length_dict[len(str)] = 1

    return max(length_dict.values())