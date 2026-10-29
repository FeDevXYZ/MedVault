# This is a sample Python script.
import datetime

test = True
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
warning = 0 # TEST
choice = 0
expired = []
almostExpired = []

medications = [
    {"medication": "ibuprofen", "expiry": "24/08/2022", "quantity": 30},
    {"medication": "Enterogermina", "expiry": "02/12/2025", "quantity": 15}
]
def Menu():
    print("")
    print("╔═══════════════════════════╗")
    print("║  What do you want to do?  ║")
    print("║  1. Add a new product     ║")
    print("║  2. Remove a product      ║")
    print("║  3. View all products     ║")
    print("║  4. Read all the warnings ║")
    print("║  5. Quit                  ║")
    print("╚═══════════════════════════╝")
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        return 0
def checkWarnings():
    expired.clear()
    almostExpired.clear()
    today = datetime.datetime.now().date()
    if debug:
        print("[DEBUG] Warning check")
    for m in medications:
        expirydate = datetime.datetime.strptime(m["expiry"], "%d/%m/%Y").date()
        medicationname = m["medication"]
        if(today>=expirydate):
            expired.append({"medication": medicationname, "days": (today-expirydate).days})
        elif ((expirydate - datetime.timedelta(days=10))<= today):
            almostExpired.append({"medication": medicationname, "expiry": m["expiry"], "daysUntil": (expirydate - today).days})
    warning = len(expired)
    almostWarning = len(almostExpired)
    return warning, almostWarning

def showMedications():
    print("Medication".ljust(20), "Expiry".ljust(13), "Quantity")
    print("-" * 50)
    for m in medications:
        print(
            m["medication"].ljust(20),
            m["expiry"].ljust(13),
            m["quantity"]
        )
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    debug = False
    # debug = input("Debug mode? (Y/N)")
    # if (debug == "Y" or debug == "y"):
    #    debug = True
    # else:
    #    debug = False
    print("◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥")
    print("▮      Welcome to MedVault     ▮")
    print("◣◥◤◢◣◥◤◢◣◥◤◢◣◥◤◢")
    print("")
    warning, almostWarning = checkWarnings()
    total = warning + almostWarning
    print("╔══════════════════════════╗")
    if total == 0:
        print("    You have no warnings.   ")
    elif total == 1:
        print(f"     You have 1 warning.")
    else:
        message = f"You have {warning} warnings."
        print(message.center(28))
    print("╚══════════════════════════╝")
    while True:
        choice = Menu()
        if choice == 1:
            if debug:
                print("[DEBUG] Add a new product")
            print("")
            name = input("Insert the product name here or type 'back' to return:")
            if name.lower() == "back":
                break
            expiry = input("Insert the expiry date (DD/MM/YYYY):")
            while True:
                try:
                    datetime.datetime.strptime(expiry, "%d/%m/%Y")
                    valida = True
                    break
                except ValueError:
                    valida = False
                    print("Date not valid. Please try again.")
                    expiry = input("Insert the expiry date (DD/MM/YYYY):")
            while True:
                try:
                    quantity = int(input("Insert the quantity: "))
                    break
                except ValueError:
                    print("Quantity must be a number.")
            medications.append({"medication": name, "expiry": expiry, "quantity": quantity})
        elif choice == 2:
            print("")
            if debug:
                print("[DEBUG] Remove a product")
            while True:
                found = False
                risposta = input("Insert the product name here or type 'list' to view all products, type 'back' to return: ")
                if risposta.lower() == "list":
                    showMedications()
                elif risposta.lower() == "back":
                    break
                else:
                    for m in medications:
                        if risposta.lower() == m["medication"].lower():
                            print(f"Medication {m['medication']} removed.")
                            medications.remove(m)
                            found = True
                            break
                    if found == False:
                        print(f"Medication {risposta} not found. Try again.")
                    else:
                        break
        elif choice == 3:
            showMedications()
        elif choice == 4:
            print("")
            if debug:
                print("[DEBUG] Read all the warnings")
            warning, expiring = checkWarnings()
            for e in expired:
                print(f"The medication {e["medication"]} is expired. It expired {e["days"]} days ago.")
            for a in almostExpired:
                print(f"The medication {a["medication"]} will expire in {a["daysUntil"]} days.")
            if warning == 0:
                print("╔══════════════════════════╗")
                print("║   You have no warnings.  ║")
                print("╚══════════════════════════╝")
        elif choice == 5:
            exit("Goodbye! ")
        else:
            print("Choice is not valid. (1-5)")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
