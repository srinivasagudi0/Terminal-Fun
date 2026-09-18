# will write code here after the commit is done

while True:
    menu = ["1. HELP ME UNDERSTAND!"] # will be looking like empty and i will keep on adding when i add new features

    for i in menu:
        print(i)
    while True:
        try:
            choice = int(input("Choose a number: "))
            break
        except Exception:
            print("Please input a number from the menu")
            continue
    print("You choose ", choice)