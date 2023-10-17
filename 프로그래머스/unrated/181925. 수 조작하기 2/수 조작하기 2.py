def solution(numLog):
    control_map = {1: "w", -1: "s", 10: "d", -10: "a"}
    result = []

    for i in range(len(numLog)):
        if i == 0:
            diff = numLog[i]
        else:
            diff = numLog[i] - numLog[i - 1]

        if diff in control_map:
            result.append(control_map[diff])

    return "".join(result)