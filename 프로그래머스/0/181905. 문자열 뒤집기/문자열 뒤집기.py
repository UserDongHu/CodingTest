def solution(my_string, s, e):
    return my_string[:s] + "".join(reversed([i for i in my_string[s:e+1]])) + my_string[e+1:]