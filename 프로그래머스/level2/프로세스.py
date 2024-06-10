def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        # 배열의 0번째보다 우선순위가 높은 값이 있을 경우 queue 맨 뒤에 append
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        # 없을경우 우선순위가 높은값을 다시 넣지 않음, 그 값이 location과 같을경우 리턴
        else:
            answer += 1
            if cur[0] == location:
                return answer