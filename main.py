number = float(input())
while True:
    move = input()
    if (move[0] == "="):
        print(number)

    else:
        if (move[0] == "+"):
            number += float(move[1:])

        elif (move[0] == "-"):
            number -= float(move[1:])

        elif (move[0] == "*"):
            number *= float(move[1:])

        elif (move[0] == "/"):
            number /= float(move[1:])

        elif ((move[0] == "*") & (move[1] == "*")):
            number **= float(move[3])

        else:
            print("Ошибка")