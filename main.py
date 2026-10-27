# This is a sample Python script.
import datetime
from calendar import month

test = True
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
warning = 0 # TEST
choice = 0

medications = [
    {"medication": "ibuprofen", "expiry": "24/08/2029", "quantity": "30"},
    {"medication": "Enterogermina", "expiry": "02/12/2025", "quantity": "15"}
]
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
def checkWarnings():
    DateObject = datetime.datetime.now()
    Day = DateObject.day
    Month = DateObject.month
    Year = DateObject.year
    print(Day)
    print(Month)
    print(Year)
    print("[DEBUG] Warning check")
    for m in medications:
        expirystr = datetime.datetime.strptime(m["expiry"], "%d/%m/%Y")
        medicationname = m["medication"]
        if (Year > expirystr.year):
            print(f"The medication called '{medicationname}' is expired.")
        elif (Year == expirystr.year):
            if (Month > expirystr.month):
                print(f"The medication called '{medicationname}' is expired.")
            elif (Month == expirystr.month):
                if (Day >= expirystr.day):
                    print(f"The medication called '{medicationname}' is expired.")
                else:
                    print(f"The medication called '{medicationname}' is not expired.")
            else:
                print(f"The medication called '{medicationname}' is not expired.")
        else:
            print(f"The medication called '{medicationname}' is not expired.")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("__-------------------------__")
    print("     Welcome to MedVault     ")
    print("--_________________________--")
    print("")
    checkWarnings()
    print("╔══════════════════════════╗")
    if warning == 0:
        print("You have no warnings.".rjust(28))
    elif warning == 1:
        print(f"     You have 1 warning.")
    else:
        print(f"    You have {warning} warnings.  ")
    print("╚══════════════════════════╝")
    while True:
        choice = Menu()
        if choice == 1:
            print("[DEBUG] Add a new product")
            print("Add a new product")
            name = input("Insert the product name here:")
            expiry = input("Insert the expiry date (DD/MM/YYYY):")
            quantity = int(input("Insert the quantity: "))
            medications.append({"medication": name, "expiry": expiry, "quantity": quantity})
        elif choice == 2:
            print("[DEBUG] Remove a product")
        elif choice == 3:
            print("[DEBUG] View all products")
            print("Medication".ljust(20), "Expiry".ljust(13), "Quantity")
            print("-"*50)
            for m in medications:
                print(
                    m["medication"].ljust(20),
                    m["expiry"].ljust(13),
                    m["quantity"]
                )
        elif choice == 4:
            print("[DEBUG] Read all the warnings")
        elif choice == 5:
            checkWarnings()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Choice is not valid. (1-5)")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
