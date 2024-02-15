def fibo_recursion(number: int) -> int: # 속도가 너무 느림,,
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)


def fibo_repetition(number: int) -> int:
    """
    fibonacci function by repetition.
    :param number: integer number
    :return: integer number
    """
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a + b
        # a = b
        # b = a + b 는 틀린 이유 : a, b = b, a+b에서 b에 할당하는 a의 값은 a=b할당하기 이전의 a의 값. 임시변수 역할 해줌.
    return a


memo = [None for _ in range(100)]
#memo = [0 if i == 0 else i if i  == 1 else None for i in range(100)]
#memo = [0, 1] + [None] * (100-1)
def fibo_memoization(number: int) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number-1) + fibo_memoization(number-2)
        memo[number] = result
    return result



n = int(input("Input number : "))

for i in range(0, n):
    print(i)
    print(fibo_memoization(i))
print("===========================")
for i in range(0, n):
    print(i)
    print(fibo_recursion(i))
print("===========================")
for i in range(0, n):
    print(i)
    print(fibo_repetition(i))


# def open_box():
#     global count
#     count -= 1
#     if count == 0:
#         return
#     open_box()
#     print("박스를 닫았습니다.")
#
# count = 3
#
# print(open_box())
