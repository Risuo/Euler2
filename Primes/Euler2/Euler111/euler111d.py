import itertools 
import CommonFunctions 
 
primes = find_primes_less_than(350000)
 
def is_prime(n):
    for p in primes:
        if p >= n:
            return True
        if n % p == 0:
            return False
    return True
 
def generator(n, d, rep):
 
    def filt_func(t):
        if t[0][0] == 0 and t[1][0] == 0:
            return False
        if t[0][-1] == n - 1 and (t[1][-1] & 1 == 0 or t[1][-1] == 5):
            return False
        return True
 
    others_indexes = combinations(range(n), n - rep)
    others_numbers = product(*([tuple(set(range(10)) - set([d]))] * (n - rep)))
    joined = filter(filt_func, product(others_indexes, others_numbers))
    for tup in joined:
        base = [d for i in range(n)]
        for ind, val in zip_longest(*tup):
            base[ind] = val
        if base[0] == 0 or base[-1] & 1 == 0 or base[-1] == 5:
            continue
        yield int(''.join(map(str, base)))
 
if __name__ == '__main__':
    result = 0
    n = 10
    for d in range(0, 10):
        found_l = []
        rep = n - 1
        while not found_l:
            for i in generator(n, d, rep):
                if not is_prime(i):
                    continue
                found_l.append(i)
            rep -= 1
        result += sum(found_l)
    print("The result is:", result)