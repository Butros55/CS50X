import sys

def main():
    while (True):
        try:
            number = int(input("Number: "))
            n = len(str(number))
        except ValueError:
            continue
        else:
            break

    strn = str(number)
    if (n == 15 and strn[0] == "3" and (strn[1] == "4" or strn[1] == "7")):
        print("AMEX")
        quit(0)

    if ((n == 13 or n == 16) and strn[0] == "4"):
        print("VISA")
        quit(0)

    if (n == 16 and strn[0] == "5" and (strn[1] == "1" or strn[1] == "2" or strn[1] == "3" or strn[1] == "4" or strn[1] == "5")):
        print("MASTERCARD")
        quit(0)


    print("INVALID")


main()