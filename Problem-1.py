def myreduce(func, lis):
    ret=lis[0]
    for x in lis[1:]:
        ret=func(ret, x)
    return ret

def multiply(x, y):
    return x*y

