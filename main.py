class color:  # Color Class
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print("The Area Calculator of Circle and Rectangle")


def area(number1):
    return number1


def area1(number1, number2):
    return number1 * number2


def circlewithradius(number1):
    return number1


def circlewithdiameter(number1a):
    return number1a


def inputask():
    inputask()


while True:
    inputask = input(
        "What shape's area do you want to calculate? \nIf Circle then 'C' , If Regular Quadilateral then 'R'\n(To "
        "Quit Type 'quit' or 'q') ")

    if inputask == "Rectangle" or inputask == "rectangle" or inputask == "R" or inputask == "r":

        input1 = input(
            "\nChoose between Rectangle and Square\nIf square then S ,if rectangle then R\n(To Quit Type 'quit' or "
            "'q') ")

        if input1 == "S" or input1 == "s" or input1 == "square" or input1 == "Square":
            length = float(input("\nWhat is the side-length of your square "))
            Area = float(length * length)
            print("\nThe area of the square is  " + str(area(Area)) + "\n-----------------------------------")
            continue

        elif input1 == "R" or input1 == "r" or input1 == "rectangle" or input1 == "Rectangle":

            width = float(input("\nWhat is the width of your rectangle "))
            length1 = float(input("What is the length of your rectangle "))
            Area1 = float(width * length1)
            print("\nThe area of the rectangle is " + str(
                area1(length1, width)) + "\n-----------------------------------")
            continue

        elif input1 == "quit" or input1 == "Quit" or input1 == "q" or input1 == "Q":
            break

        else:
            print("Enter 'S' or 'R'")
            continue
    else:
        if inputask == "Circle" or inputask == "circle" or inputask == "c" or inputask == "C":
            input2 = input(
                "\nChoose between Radius and Diameter\nIf radius then R , if diameter then D\n(To Quit Type 'quit' or "
                "'q') ")

            if input2 == "R" or input2 == "r":
                radius = float(input("\nWhat is the radius of your circle "))
                Area = float(radius * radius * 3.14)
                circ = float(2 * 3.14 * radius)
                print("The area of the circle is " + str(circlewithradius(Area)))
                print("The circumference of the circle is " + str(
                    circlewithradius(circ)) + "\n-----------------------------------")
                continue

            elif input2 == "D" or input2 == "d":

                dia = float(input("\nWhat is the diameter of your circle "))
                Area1 = float(dia * dia * 0.25 * 3.14)
                circ1 = float(3.14 * dia)
                print("The area of the circle is " + str(circlewithdiameter(Area1)))
                print("The circumference of the circle is " + str(
                    circlewithdiameter(circ1)) + "\n-----------------------------------")
                continue

            elif input2 == "quit" or input2 == "Quit" or input2 == "q" or input2 == "Q":
                break

            elif inputask == "quit" or inputask == "Quit" or inputask == "q" or inputask == "Q":
                break

            else:
                print("Enter 'R' or 'D'\n")
                continue
        elif inputask == "quit" or inputask == "Quit" or inputask == "q" or inputask == "Q":
            break
        else:
            print("Enter 'C' or 'R'\n")
