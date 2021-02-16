def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n - 1)


def fibo(n):
    
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

res = fatorial(3)
print(res)