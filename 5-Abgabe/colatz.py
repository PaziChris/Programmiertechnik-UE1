import time
def colatz(n):
    if n <= 1:
        return [1]
    if n & 1:
        result = colatz(3 * n + 1)
    else:
        result = colatz(n // 2)
    result.insert(0,n)
    return result

def colatz_iter(n):
    result = []
    while n > 1:
        result.append(n)
        if n & 1:
            n = 3 * n + 1
        else:
            n //= 2
    result.append(n)
    return result

def colatz_2(n,cnt=0):
    if n <= 1:
        return [1] * ( cnt + 1)
    if n & 1:
        result = colatz_2(3 * n + 1,cnt+1)
    else:
        result = colatz_2( n//2,cnt+1)
    result[cnt] = n
    return result

def main():
    
    while True:
        for_n = input("input colatz series for n: (q quits)")
        if for_n in 'qQ':
            return
        try:
            for_n = int(for_n)
        except ValueError:
            print("n must be > 0")
        else:
            if for_n > 0:
                start = time.perf_counter()
                result = colatz(for_n)
                duration = time.perf_counter() - start
                print("colatz series for {} computed in {} s):".format(for_n,duration),result)
                start = time.perf_counter()
                result_2 = colatz_2(for_n)
                duration = time.perf_counter() - start
                print("slightly optimized version computed in {} s:".format(duration),result_2)
                start = time.perf_counter()
                result_3 = colatz_iter(for_n)
                duration = time.perf_counter() - start
                print("iterative version computed in {} s:".format(duration),result_3)
                
        for_n = 0
    
if __name__ == '__main__':
    main()    
    
