quitList = ["Q", "q", "quit", "Quit", "exit", "Exit", "kill"]

# Your Input Should be like this:
#
#   align-items:center;align-content:center;align-self:center;align-items:baseline;align-self:auto;
#    

while True:
    print("Doesnt Work With Multiline.")
    print("Enter in format like this: align-content:center; <<>> to Quit: Q")
    text = input()
    classNames = text.split(";")

    if text in quitList:
        break

    for classValues in classNames:
        val = classValues.split(":")
        print(f".{val[0]}-{val[1]}" + "{" + f"{val[0]}:{val[1]};" + "}")
