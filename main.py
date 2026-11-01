import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

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
class symbols:
    DOT = '\u2022'

warning = 0  # TEST
choice = 0
expired = []
almostExpired = []

medications = [
    {"ID":1, "medication":"Enterogermina", "expiry":"10/10/2026", "quantity":30, "opened": "-"},
    {"ID":2, "medication":"Ibuprofen", "expiry":"01/12/2029", "quantity":10, "opened": "-"}
]
avvisi = []

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
    for m in medications:
        expirydate = datetime.datetime.strptime(m["expiry"], "%d/%m/%Y").date()
        medicationname = m["medication"]
        if (today >= expirydate):
            expired.append({"medication": medicationname, "days": (today - expirydate).days})
        elif ((expirydate - datetime.timedelta(days=10)) <= today):
            almostExpired.append(
                {"medication": medicationname, "expiry": m["expiry"], "daysUntil": (expirydate - today).days})
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

def clear(frame):
    for w in frame.winfo_children():
        w.destroy()

def addProduct():
    global qualeProd
    global qualeExp
    global qualeQuant
    global qualeOpen
    global optVar
    global avvisiVar
    global condText
    avvisiVar = tk.StringVar()
    condText = tk.StringVar()

    clear(answer)
    action.set("Add product")
    tk.Label(answer, textvariable=action, justify="left").pack(anchor="nw")
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    tk.Label(answer, text="Insert product name:", justify="left").pack(anchor="nw")
    qualeProd = tk.Entry(answer)
    qualeProd.pack(fill="x", anchor="nw")
    tk.Label(answer, text="Insert expiry date (DD/MM/YYYY):", justify="left").pack(anchor="nw")
    qualeExp = Calendar(answer,
                font="Arial 14", selectmode='day', cursor="hand1", date_pattern="dd/mm/yyyy")
    qualeExp.pack(fill="x", anchor="nw")
    tk.Label(answer, text="Insert quantity:", justify="left").pack(anchor="nw")
    qualeQuant = tk.Entry(answer)
    qualeQuant.pack(fill="x", anchor="nw")
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    optVar = tk.BooleanVar()
    optValues = tk.Checkbutton(answer, text=" Optional values", justify="left", variable=optVar)
    optValues.pack(anchor="nw")
    tk.Label(answer, text="Add an opening date:", justify="left").pack(anchor="nw")
    qualeOpen = Calendar(answer,
                font="Arial 14", selectmode='day', cursor="hand1", date_pattern="dd/mm/yyyy")
    qualeOpen.pack(fill="x", anchor="nw")
    qualeExp.selection_clear()
    qualeOpen.selection_clear()
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    tk.Button(answer, text="Save", command=save1).pack(anchor="nw")

    tk.Label(answer, text="").pack(anchor="nw")
    tk.Label(answer, textvariable=condText, justify="left").pack(anchor="nw")
    tk.Label(answer, textvariable=avvisiVar, justify="left").pack(anchor="nw")

def save1():
    avvisi.clear()
    saveProd()
    saveExp()
    saveQuant()
    saveOpen()
    if avvisi:
        condText.set("Please correct the errors below.")
        avvisiVar.set("\n".join(avvisi))
    else:
        avvisiVar.set("")
        ID = str(max((int(m["ID"]) for m in medications), default=0) + 1)
        medications.append({"ID": ID, "medication": savedProd, "expiry": savedExp, "quantity": savedQuant, "usedFor": "-", "opened": savedOpen})
        condText.set("Product saved.")
        qualeProd.delete(0, tk.END)
        qualeQuant.delete(0, tk.END)
        qualeExp.selection_clear()
        qualeOpen.selection_clear()

        root.after(3000, condClear)

def saveProd():
    global savedProd
    savedProd = None
    savedProd = qualeProd.get()
    if savedProd == None or savedProd == "":
        avvisi.append("Add a product name.")
def saveExp():
    global savedExp
    savedExp = None
    savedExp = qualeExp.get_date()
    if savedExp == None or savedExp == "":
        avvisi.append("Insert an expiry date.")
def saveQuant():
    global savedQuant
    savedQuant = qualeQuant.get()
    if savedQuant == None or savedQuant.isdigit() == False:
        avvisi.append("Quantity is blank or not a number.")
def saveOpen():
    global savedOpen
    if saveOptional():
        savedOpen = qualeOpen.get_date()
    else:
        savedOpen = "-"
    return savedOpen
def saveOptional():
    savedOpt = optVar.get()
    return savedOpt
def condClear():
    condText.set("")

def removeProduct():
    global productname
    global medAvailable
    global saveButt
    global feedback
    global products
    feedback = tk.StringVar()
    medAvailable = tk.StringVar()
    productVar = tk.StringVar()
    products = [
        f"{m['medication']} - Expiry: {m['expiry']}"
        for m in medications
    ]

    clear(answer)
    action.set("Remove product")
    tk.Label(answer, textvariable=action, justify="left").pack(anchor="nw")
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    productname = ttk.Combobox(answer, textvariable=productVar, values=products, state="readonly")
    productname.pack(anchor="nw", fill="x")
    tk.Label(answer, textvariable=medAvailable, justify="left").pack(anchor="nw")
    saveButt = tk.Button(answer, text="Confirm", command=save2)
    saveButt.pack(anchor="nw")
    tk.Label(answer, textvariable=feedback, justify="left").pack(anchor="nw")

    if not medications:
        productname.config(state="disabled")
        medAvailable.set("No products available.")
        saveButt.config(state="disabled")
    else:
        productname.config(state="readonly")
        medAvailable.set("")
        saveButt.config(state="normal")

def save2():
    global productname
    selected = productname.current()
    if selected == -1:
        feedback.set("Please select a product.")
    else:
        m = medications[selected]
        medications.remove(m)
        feedback.set("Product removed.")
        if not medications:
            productname.config(state="disabled")
            medAvailable.set("No products available.")
            saveButt.config(state="disabled")
        else:
            productname.config(state="readonly")
            medAvailable.set("")
            saveButt.config(state="normal")
        productname.config(value = [
            f"{m['medication']} - Expiry: {m['expiry']}"
            for m in medications
        ])
        productname.set("")
        root.after(3000, feedbackClear)
def feedbackClear():
    feedback.set("")

def listProducts():
    clear(answer)
    action.set("List products")
    tk.Label(answer, textvariable=action, justify="left").pack(anchor="nw")
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    for m in medications:
        tk.Label(answer, text=f"|{m["medication"]}   Quantity: {m["quantity"]}   Expiry: {m["expiry"]}   Opened: {m["opened"]}", justify="left", font=("Arial", 14), wraplength=350).pack(anchor="nw")

def readWarnings():
    warning, expiring = checkWarnings()

    clear(answer)
    action.set("Read warnings")
    tk.Label(answer, textvariable=action, justify="left").pack(anchor="nw")
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    tk.Label(answer, text="Expired:", justify="left").pack(anchor="nw")
    for e in expired:
        tk.Label(answer, text=f"The medication {e["medication"]} is expired. It expired {e["days"]} days ago.", justify="left", wraplength=350).pack(anchor="nw")
    if not expired:
        tk.Label(answer, text="There are no expired products.", justify="left", wraplength=350).pack(anchor="nw")
    tk.Label(answer, text="", justify="left").pack(anchor="nw")
    tk.Label(answer, text="Expiring soon:", justify="left").pack(anchor="nw")
    for a in almostExpired:
        tk.Label(answer, text=f"The medication {a["medication"]} is expiring soon. It will expire in {a["daysUntil"]} days.", justify="left", wraplength=350).pack(anchor="nw")
    if not almostExpired:
        tk.Label(answer, text="There are no products that are almost expired.", justify="left", wraplength=350).pack(anchor="nw")

def goodbye():
    clear(answer)
    action.set("Exit")
    exit(9)


if __name__ == '__main__':
    MODE = input("Do you want to start Tkinter Medvault? WIP, may contain bugs (Y/N): ")
    if MODE.lower() == "y":
        saved = ""
        root = tk.Tk()
        root.title("MedVault")
        root.geometry("560x650")
        root.resizable(False, False)
        action = tk.StringVar()

        buttons = tk.Frame(root, pady=20, padx=20)
        buttons.pack(side="left", fill="y")

        answer = tk.Frame(root, pady=20, padx=20)
        answer.pack(side="left", fill="both", expand=True)

        tk.Label(buttons, text="Welcome to MedVault", bg="red").pack(ipadx=5, ipady=5, pady=10)
        tk.Button(buttons, text="Add product", command=addProduct).pack(fill="x")
        tk.Button(buttons, text="Remove product", command=removeProduct).pack(fill="x")
        tk.Button(buttons, text="List products", command=listProducts).pack(fill="x")
        tk.Button(buttons, text="Read warnings", command=readWarnings).pack(fill="x")
        tk.Button(buttons, text="Exit", command=goodbye).pack(fill="x")

        root.mainloop()
        exit("Tkinter closed.")
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
            ID = str(max((int(m["ID"]) for m in medications), default=0) + 1)
            name = input("Insert the product name here or type 'back' to return: ")
            if name.lower() == "back":
                continue
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
            print(f"Medication {name} added to the software.")
            medications.append({"ID": ID, "medication": name, "expiry": expiry, "quantity": quantity, "usedFor": answer,
                                "opened": "-"})
        elif choice == 2:
            print("")
            if debug:
                print("[DEBUG] Remove a product")
            while True:
                found = 0
                answer = input(
                    "Insert the product name here or type 'list' to view all products, type 'back' to return: ")
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
