# def decimal_to_octal(number: int) -> str:
#     """
#     decimal number to octal number
#     :param number: integer (base dec)
#     :return: string (base octal)
#     """
#     octal = ''
#     while number > 0:
#         octal = str(number % 8) + octal
#         number = number // 8
#     return octal
#
# #
# n = int(input("Input decimal number : "))
# print(decimal_to_octal(n))


# 재귀함수를 사용하면 속도도 빠르고 직관적임
def decimal_to_octal(number: int) -> str:
    """
    decimal number to octal number
    :param number: integer (base dec)
    :return: string (base octal)
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(n//8) + str(n % 8)


n = int(input("Input decimal number : "))
print(decimal_to_octal(n))
