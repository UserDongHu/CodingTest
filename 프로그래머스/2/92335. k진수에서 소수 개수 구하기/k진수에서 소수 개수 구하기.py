def solution(n, k):
    
    def change(n, q):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)
        return rev_base[::-1]
    
    def is_prime_num(x):
        if type(x) is not int or x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    return len(list(filter(is_prime_num ,map(lambda x: int(x) ,filter(lambda x: x.isdigit() ,str(change(n, k)).split('0'))))))