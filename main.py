# This is a sample Python script.
test = True
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
warning = 1
choice = 0


def Menu():
    print("")
    print("")
    print("What do you want to do?")
    print("1. Add a new product")
    print("2. Remove a product")
    print("3. View all products")
    print("4. Read all the warnings")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    return choice

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("__-------------------------__")
    print("     Welcome to MedVault     ")
    print("--_________________________--")
    print("")
    if test:
        warning = int(input("Set the amount of warnings: "))
    print("╔══════════════════════════╗")
    if warning == 0:
        print("    You have no warnings.   ")
    elif warning == 1:
        print(f"     You have 1 warning.")
    else:
        print(f"    You have {warning} warnings.  ")
        print("╚══════════════════════════╝")
    while True:
        choice = Menu()
        if choice == 1:
            print("[DEBUG] Add a new product")
        elif choice == 2:
            print("[DEBUG] Remove a product")
        elif choice == 3:
            print("[DEBUG] View all products")
        elif choice == 4:
            print("[DEBUG] Read all the warnings")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Choice is not valid. (1-5)")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
