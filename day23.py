import tkinter as tk

memo = [0 if i == 0 else i if i  == 1 else None for i in range(100)]
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
    else:
        result = fibo_memoization(number-1) + fibo_memoization(number-2)
        memo[number] = result
    return result



# create window object
w = tk.Tk()
w.title("Fibonacci")
w.geometry("300x150")


# create widget
lbl_display_fibonacci_result = tk.Label(w, text = 'Fibonacci by memoization')
en_input_number = tk.Entry(w)
btn_click = tk.Button(w, text = "Click")

# layout - 배치
lbl_display_fibonacci_result.pack()
en_input_number.pack(fill = "x")
btn_click.pack(fill = "x")

w.mainloop()    # x 누를 때까지 계속 실행.
# n = int(input("Input number :x ")) # Input box로 대치
# print(f"fibonacci({n}) = {fibo_memoization(n)}") # Lable로 대치
