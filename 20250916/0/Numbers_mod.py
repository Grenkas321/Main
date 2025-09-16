match n := int(input()):
    case 1:
        print("один")
    case 2:
        print("два")
    case 3:
        print("три")
    case _:
        if (n % 2):
            print(n , "-- много")
        else:
            print("чётное")
