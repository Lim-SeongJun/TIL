def GCD(Hap):
    GCD=[]
    for i in range(3,int(Hap**(1/2))+1):
        if Hap%i==0:
            GCD.append(i)
    return GCD
def solution(brown, yellow):
    answer = []
    Hap = brown+yellow
    A = GCD(Hap)
    for i in A:
        if yellow%(i-2)==0 and Hap==i*((yellow//(i-2))+2):
            return [(yellow//(i-2))+2,i]
    return answer