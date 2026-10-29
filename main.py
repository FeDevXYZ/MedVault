
import datetime
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
warning = 0 # TEST
choice = 0
expired = []
almostExpired = []

medications = [
    {"medication": "ibuprofen", "expiry": "24/08/2022", "quantity": 30, "usedFor": ""},
    {"medication": "Enterogermina", "expiry": "02/12/2025", "quantity": 15, "usedFor": ""}
]
def Menu():
    print(bcolors.OKBLUE)
    print("╔═══════════════════════════╗")
    print("║  What do you want to do?  ║")
    print("║  1. Add a new product     ║")
    print("║  2. Remove a product      ║")
    print("║  3. View all products     ║")
    print("║  4. Read all the warnings ║")
    print("║  5. Quit                  ║")
    print("╚═══════════════════════════╝")
    try:
        choice = int(input(bcolors.ENDC + "Enter your choice: "))
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

if __name__ == '__main__':
    debug = False
    # debug = input("Debug mode? (Y/N)")
    # if (debug == "Y" or debug == "y"):
    #    debug = True
    # else:
    #    debug = False
    print(bcolors.HEADER + "◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥" + bcolors.ENDC)
    print(bcolors.HEADER + "▮      Welcome to MedVault     ▮" + bcolors.ENDC)
    print(bcolors.HEADER + "◣◥◤◢◣◥◤◢◣◥◤◢◣◥◤◢" + bcolors.ENDC)
    print("")
    warning, almostWarning = checkWarnings()
    total = warning + almostWarning
    print(bcolors.OKCYAN + "╔══════════════════════════╗")
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
            name = input("Insert the product name here or type 'back' to return: ")
            if name.lower() == "back":
                break
            expiry = input("Insert the expiry date (DD/MM/YYYY): ")
            while True:
                try:
                    datetime.datetime.strptime(expiry, "%d/%m/%Y")
                    valida = True
                    break
                except ValueError:
                    valida = False
                    print("Date not valid. Please try again.")
                    expiry = input("Insert the expiry date (DD/MM/YYYY): ")
            while True:
                try:
                    quantity = int(input("Insert the quantity: "))
                    break
                except ValueError:
                    print("Quantity must be a number.")
            print("Optional Values (press Enter to leave blank)")
            answer = input("Insert what it is used for (e.g. headache, stomachache): ")
            medications.append({"medication": name, "expiry": expiry, "quantity": quantity, "usedFor": answer})
        elif choice == 2:
            print("")
            if debug:
                print("[DEBUG] Remove a product")
            while True:
                found = False
                answer = input("Insert the product name here or type 'list' to view all products, type 'back' to return: ")
                if answer.lower() == "list":
                    showMedications()
                elif answer.lower() == "back":
                    break
                else:
                    for m in medications:
                        if answer.lower() == m["medication"].lower():
                            print(f"Medication {m['medication']} removed.")
                            medications.remove(m)
                            found = True
                            break
                    if found == False:
                        print(f"Medication {answer} not found. Try again.")
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
            exit("Goodbye!")
        else:
            print("Choice is not valid. (1-5)")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
