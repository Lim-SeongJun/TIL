def solution(s):
    answer = ''
    a = s.split(" ")
    return f"{str(min(list(map(int,a))))} {str(max(list(map(int,a))))}"