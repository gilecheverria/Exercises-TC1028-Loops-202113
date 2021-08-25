def invert_digits(num):
    # escribe tu código abajo de esta línea
    pass


def main():
    num = int(input("Enter a number: "))
    if num >= 1000000 or num <= -1000000:
        print("Too long")
    else:
        print(invert_digits(num))


if __name__ == '__main__':
    main()
