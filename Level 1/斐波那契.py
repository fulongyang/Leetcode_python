




# 斐波那契
def fb1(n):
    return 1 if n == 0 or n == 1 else fb1(n - 1) + fb1(n - 2)


def fb2(n):
    x ,y = 1 ,1
    for _ in range(n):
        x ,y =y, x + y
    return x


def fb3(max):
    n, a, b = 0, 0, 1
    while n < max:
        n += 1
        a, b = b, a + b
        if a >= 100:
            break
        yield a


def fb4(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def fb5(n):
    print(n)
    return 1 if n == 0 or n == 1 else fb1(n - 1) + fb1(n - 2)



def fb6(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fb3(n-1) + fb3(n-2)



def fb8(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b,a+b
        n+=1
    return re_list



# 递归
def fb9(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fb9(n - 1) + fb9(n - 2)



if __name__ == "__main__":
    print(fb6(10))






















