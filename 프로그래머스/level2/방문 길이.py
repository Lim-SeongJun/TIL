def solution(dirs):
    answer = 0
    List = []
    x = 5
    y = 5
    move = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    for i in dirs:
        (dx,dy) = move[i]
        if not (0 <= x+dx and x+dx <=10 and 0<=y+dy and y+dy<=10):
            continue
        List.append((x,y,x+dx,y+dy))
        List.append((x+dx,y+dy,x,y))
        x += dx
        y += dy
    answer = len(set(List))//2
    return answer