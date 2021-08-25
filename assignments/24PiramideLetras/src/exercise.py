def print_letter_pyramid(height):
    #escribe tu código abajo de esta línea
    pass


def main():
    height = int(input("Enter pyramid height: "))
    if height < 1 or height > 26:
        print("Out of range")
    else:
        print_letter_pyramid(height)


if __name__ == '__main__':
    main()
