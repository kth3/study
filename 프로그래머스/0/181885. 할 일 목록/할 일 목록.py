def solution(todo_list, finished):
    answer = []
    for idx, f in enumerate(finished):
        if f == False:
            answer.append(todo_list[idx])
    return answer