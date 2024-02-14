def fibo_recursion(number: int) -> int:
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else :
        return fibo_recursion(number-1) + fibo_recursion(number-2)


n = int(input("Input first number : "))
# for i in range(0, n) :
#     print(i)
#     print(fibo_recursion(i), end=' ')


def fibo_repetition(number : int) -> int:
    a = 0
    b = 1
    for _ in range(number):
        # a = b
        # b= a + b // 임시변수 temp or 언패킹으로 문제 해결
        a, b = b, a + b
    return a

print(fibo_repetition(n))



