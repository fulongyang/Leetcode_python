
# 斐波那契

def fb1(n):
    return 1 if n == 0 or n == 1 else fb1(n - 1) + fb1(n - 2)

def fb2(n):
    x ,y = 1 ,1
    for _ in range(n):
        x ,y =y, x + y
    return x


def fb5(max):
    n, a, b = 0, 0, 1
    while n < max:
        n += 1
        a, b = b, a + b
        if a >= 100:
            break
        yield a


# 递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)


if __name__ == "__main__":
    print(Fibonacci_Recursion_tool(10))

    print([f for f in fb5(30)])