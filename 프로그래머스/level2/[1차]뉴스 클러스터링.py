import re
def solution(str1, str2):
    answer = 0
    p = re.compile('[a-z]{2}')
    str1 =str1.lower()
    str2 =str2.lower()
    word1 = [str1[i:i+2] for i in range(len(str1)-1) if p.match(str1[i:i+2]) != None]
    word2 = [str2[i:i+2] for i in range(len(str2)-1) if p.match(str2[i:i+2]) != None]
    for i in set(word1+word2):
        answer += min(word1.count(i),word2.count(i))
    return 65536 if len(word1) == 0 and len(word2) == 0 else int((answer/(len(word1)+len(word2)-answer))*65536)