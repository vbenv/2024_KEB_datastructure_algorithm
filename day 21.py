def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': ')', ']' : '[', '}' : '{', '>' : '<'}
    for char in expr:
        if char not in table:
            #push(char)
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0
