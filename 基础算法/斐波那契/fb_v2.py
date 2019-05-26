



import timeit


#斐波那契2

def fb2(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def fb1(n):
    print(n)
    return 1 if n == 0 or n == 1 else fb1(n - 1) + fb1(n - 2)


def fb3(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fb3(n-1) + fb3(n-2)


memo = {0:0, 1:1}
def fb4(n):
    if not n in memo:
        memo[n] = fb4(n-1)+fb4(n-2)
    return memo[n]


def fb5(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b,a+b
        n+=1
    return re_list



if __name__ == "__main__":
    f = fb5(10)
    print(f)