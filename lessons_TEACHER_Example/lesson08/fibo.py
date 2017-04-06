def fibo1(n):
    if n < 2:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)
def fibo2(n):
    if n < 2:
        result = [1]
    elif n == 2:
        result = [1, 1]
    else:
        result = [1, 1]
        for i in range(2,n+1):
            result.append(result[i-1] + result[i-2])
    return result

CONST = "FIBO CONST"

print "fibo: ", fibo1(6)
print "fibo: ",fibo2(6)

if __name__ == '__main__':

    print "fibo__main__: ", fibo1(6)
    print "fibo__main__: ",fibo2(6)