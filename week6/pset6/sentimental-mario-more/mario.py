
while (True):
    try:
        height = int(input("Height: "))
    except ValueError:
        continue
    else:
        if (height > 0 and height <= 8):
            break

for row in range(height):

    for spacel in range(height - (row + 1)):
        print(" ", end="")

    for hashl in range(row + 1):
        print("#", end="")

    print("  ", end="")

    for hashr in range(row + 1):
        print("#", end="")

    print("")
