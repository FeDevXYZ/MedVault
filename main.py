import datetime

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
    {"ID": "1", "medication": "ibuprofen", "expiry": "24/08/2022", "quantity": 30, "usedFor": "Fever, headache", "opened": "-"},
    {"ID": "2", "medication": "Enterogermina", "expiry": "02/12/2025", "quantity": 15, "usedFor": "Stomachache", "opened": "-"},
    {"ID": "3", "medication": "ibuprofen", "expiry": "24/08/1522", "quantity": 0, "usedFor": "Fever, headache", "opened": "-"}
]
def Menu():
    print(bcolors.OKBLUE)
    print("╔════════════════════════════╗")
    print("║  What do you want to do?   ║")
    print("║  1. Add a new product      ║")
    print("║  2. Remove a product       ║")
    print("║  3. View all products      ║")
    print("║  4. Read all the warnings  ║")
    print("║  5. Add 'Opened' date      ║")
    print("║  6. Quit                   ║")
    print("╚════════════════════════════╝")
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
    print("Medication".ljust(20), "Expiry".ljust(13), "Quantity".ljust(13), "Opened")
    print("-" * 60)
    for m in medications:
        print(
            m["medication"].ljust(20),
            m["expiry"].ljust(13),
            str(m["quantity"]).ljust(13),
            m["opened"]
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
            ID = str(max(int(m["ID"]) for m in medications) + 1)
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
            medications.append({"ID": ID, "medication": name, "expiry": expiry, "quantity": quantity, "usedFor": answer, "opened": "-"})
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
                    matches = []
                    matches.clear()
                    nfound = 0
                    for m in medications:
                        if answer.lower() == m["medication"].lower():
                            nfound = nfound + 1
                            matches.append(m)
                            #print(f"Medication {m['medication']} removed.")
                    for m in medications:
                        if answer.lower() == m["medication"].lower() and nfound == 1:
                            print(f"Medication {m['medication']} removed.")
                            medications.remove(m)
                            found = True
                            break
                    if nfound > 1:
                        n = 1
                        for m in matches:
                            print(f"{m["ID"]}. {m["medication"]} - Expiry: {m["expiry"]} - Quantity: {m["quantity"]}")
                            n = n + 1
                        chosenID = input("Type the ID of the product to remove: ")
                        for m in matches:
                            if str(m["ID"]) == chosenID:
                                medications.remove(m)
                                print(f"Medication {m['medication']} (ID {m['ID']}) removed.")
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
                found = False  # <-- 1. azzerato ogni volta
                selected = None  # <-- 1.
                answer = input("Insert the product where you want to add an opening date: ")
                if answer.lower() == "list":
                    showMedications()
                elif answer.lower() == "back":
                    continue  # <-- 2. era break (chiudeva il programma)
                else:
                    matches = []
                    matches.clear()
                    nfound = 0
                    for m in medications:
                        if answer.lower() == m["medication"].lower():
                            nfound = nfound + 1
                            matches.append(m)
                            # print(f"Medication {m['medication']} removed.")
                    for m in medications:
                        if answer.lower() == m["medication"].lower() and nfound == 1:
                            print(f"Medication {m['medication']} found.")
                            found = True
                            selected = m["ID"]  # <-- 3. mancava nel caso del farmaco unico
                            break
                    if nfound > 1:
                        n = 1
                        for m in matches:
                            print(f"{m["ID"]}. {m["medication"]} - Expiry: {m["expiry"]} - Quantity: {m["quantity"]}")
                            n = n + 1
                        chosenID = input("Type the ID of the product to select: ")
                        for m in matches:
                            if str(m["ID"]) == chosenID:
                                print(f"Medication {m['medication']} (ID {m['ID']}) found.")
                                found = True
                                selected = m["ID"]
                                break
                    if found == False:
                        print(f"Medication {answer} not found. Try again.")
                    else:  # <-- 4. il salvataggio è qui dentro
                        for m in medications:
                            if m["ID"] == selected:
                                m["opened"] = datetime.date.today().strftime("%d/%m/%Y")
                        print(f"Opening date added ({datetime.datetime.today().strftime("%d/%m/%Y")})")
        elif choice == 6:
            exit("Goodbye!")
        else:
            print("Choice is not valid. (1-5)")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

