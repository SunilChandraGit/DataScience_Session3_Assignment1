def myfilter(func, lis):
    retlis=[]
    for x in lis:
        if func(x):
            retlis.append(x)
    return retlis

def isPrime(x):
    isPrime=True
    if x%2==0:
        isPrime = False
    else:
        for r in range(2, int(x/2)):
            if x%r==0:
                isPrime = False
                break
    return isPrime
 