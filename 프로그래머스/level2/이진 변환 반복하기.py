def solution(s):
    zero_cnt = 0
    cycle_cnt = 0
    while len(s)!=1:
        cycle_cnt += s.count('0')
        s = s.replace("0",'')
        s = bin(len(s))[2:]
        zero_cnt+=1
    return [zero_cnt,cycle_cnt]