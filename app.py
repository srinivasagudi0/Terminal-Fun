# will write code here after the commit is done

print("---MENU---")
menu = ["1. HELP ME UNDERSTAND!", "2. exit"] # will be looking like empty and i will keep on adding when i add new features

for i in menu:
    print(i)

while True:
    
    while True:
        try:
            choice = int(input("Choose a number: "))
            if choice == 2:
                print("\nStay Wild!")
                exit()
            print(f"You choose the option {menu[choice -1]}")
            break
        except Exception:
            print("Please input a number from the menu")
            continue

        