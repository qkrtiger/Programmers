def solution(todo_list, finished):
    f = []
    for i in range(len(todo_list)):
        if finished[i] != True:
            f.append(todo_list[i])
    return f
