def ask_int(prompt="Введите целое: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Не целое, попробуйте ещё раз.")

if __name__ == "__main__":
    n = ask_int()
    print("OK:", n)
