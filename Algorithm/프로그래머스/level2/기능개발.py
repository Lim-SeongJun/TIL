def solution(progresses, speeds):
    answer = []
    count = 0
    for i in range(len(speeds)):
        a = progresses[i]-100
        if progresses[i] < 100:
            count = -(a//speeds[i])
            progresses = list(map(lambda x,y: x+(y*count),progresses,speeds))
        else:
            continue
        b = list(map(lambda x: 1 if x<100 else 0, progresses))
        answer.append((b.index(max(b)) if max(b) != 0 else len(b))-sum(answer))
    return answer