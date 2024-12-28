quitList = ["Q", "q", "quit", "Quit", "exit", "Exit", "kill"] 
A_list = ["A", "a"]
S_list = ["S", "s"]

while True:
    print("A: for rad, S: for Color, Q: for quit")
    option = input()

    if option in quitList:
        break
    if option in A_list:
        print("enter step:")
        step = int(input())

        print("enter limit:")
        limit = int(input())

        for x in range(0, limit+1, step):
            print(f".border-{x}px" + "{" + f"border-radius: {x}px;" + "}")
    if option in S_list:
        print("enter color values:")
        color = input()

        colors = color.split(";")
        for x in colors:
            colVal = x.split(":")
            colorName = colVal[0]
            colorCode = colVal[1]
            print(f".border{colorName[1:]}" + "{" + f"border-color: {colorCode.strip()};" + "}")