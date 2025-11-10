def ask_int(prompt="Введи целое число, по братски -- "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Не, браток, ты что-то перепутал, попробуй ещё раз.")

if __name__ == "__main__":
    n = ask_int()
    print("Красавчик, на легенде ввёл - ", n)
