def solution(info, query):
    answer = [0] * len(query)
    choice=[]
    cnt = 0
    A = []
    for i in range(len(query)):
        choice +=[query[i].split(' ')]
        del choice[i][5],choice[i][3],choice[i][1]
        choice[i][-1] = int(choice[i][-1])
    for i in range(len(info)):
        A += [info[i].split(' ')]
        A[i][-1] = int(A[i][-1])
    for i in range(len(choice)):
        for j in range(len(A)):
            if (choice[i][0]==A[j][0] or choice[i][0]=='-') and (choice[i][1]==A[j][1] or choice[i][1]=='-') and (choice[i][2]==A[j][2] or choice[i][2]=='-') and (choice[i][3]==A[j][3] or choice[i][3]=='-') and (choice[i][-1]<=A[j][-1]):
                cnt +=1
        answer[i] = cnt
        cnt = 0
    return answer

def solution(info, query):
    answer = [0] * len(query)
    I = ','.join(info).replace(',',' ').split(' ')
    Q = ','.join(query).replace(',',' ').split(' ')
    for i in range(len(query)):
        I[4::5] = list(map(int,I[4::5]))
        Q[7::8] = list(map(int,Q[7::8]))
        langs = list(filter(lambda x: (Q[::8][i] in [I[::5][x],'-'])&(Q[2::8][i] in [I[1::5][x],'-'])&(Q[4::8][i] in [I[2::5][x],'-'])&(Q[6::8][i] in [I[3::5][x],'-'])&(I[4::5][x] >= Q[7::8][i]), range(len(info))))
        answer[i] = len(langs)
    return answer