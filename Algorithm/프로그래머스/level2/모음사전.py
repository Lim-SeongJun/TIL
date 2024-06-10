from itertools import product

def solution(word):
    answer = 0
    lis = []
    keyword = ['A','E','I','O','U']
    for i in range(1,6):
        for j in product(keyword,repeat=i):
            lis.append(j)
    lis.sort()
    for num,i in enumerate(lis):
        if "".join(i) == word:
            return num+1