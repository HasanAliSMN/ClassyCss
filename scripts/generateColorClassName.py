quitList = ["Q", "q", "quit", "Quit", "exit", "Exit", "kill"]


# Your Input Should be like this:
#
#   --white: #ffffff;--black: #000000;--red: #ff0000;--green: #00ff00;--blue: #0000ff;
#    

while True:
    print("Doesnt Work With Multiline. Can take Multiple Color Values")
    print("Enter in format like this: --blue-100: #adadff; to Quit: Q")
    text = input()
    classNames = text.split(";")

    if text in quitList:
        break

    for classValues in classNames :
        val = classValues.split(":").pop(0)
        print(f".bg{val[1:]}" + "{" + f"background-color: var({val});" +"}")

