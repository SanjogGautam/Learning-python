value='sunday'
match value:
    case "sunday"|"saturday":
        print("Weekend")
    case _:
        print("Workday")

