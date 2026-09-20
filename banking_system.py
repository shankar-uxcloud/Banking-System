import random
import json
from datetime import datetime


# ============================================
# FILE SETTINGS
# ============================================

DATA_FILE = "accounts.json"

accounts = {}


# ============================================
# LOAD ACCOUNTS
# ============================================

def load_accounts():

    global accounts

    try:

        with open(DATA_FILE, "r") as file:
            accounts = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        accounts = {}


# ============================================
# SAVE ACCOUNTS
# ============================================

def save_accounts():

    with open(DATA_FILE, "w") as file:

        json.dump(
            accounts,
            file,
            indent=4
        )


# ============================================
# GENERATE ACCOUNT NUMBER
# ============================================

def generate_account_number():

    while True:

        account_number = str(
            random.randint(100000, 999999)
        )

        if account_number not in accounts:

            return account_number


# ============================================
# ADD TRANSACTION
# ============================================

def add_transaction(
    account_number,
    transaction_type,
    amount,
    details
):

    transaction = {

        "type": transaction_type,

        "amount": amount,

        "date": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        ),

        "details": details
    }


    accounts[account_number][
        "transactions"
    ].append(transaction)


# ============================================
# CREATE ACCOUNT
# ============================================

def create_account(
    name,
    phone,
    pin
):

    if not name:

        return None, "Name is required."


    if not phone:

        return None, "Phone number is required."


    if not pin.isdigit() or len(pin) != 4:

        return (
            None,
            "PIN must contain exactly 4 digits."
        )


    account_number = generate_account_number()


    accounts[account_number] = {

        "name": name,

        "phone": phone,

        "pin": pin,

        "balance": 0.0,

        "transactions": []

    }


    save_accounts()


    return (
        account_number,
        "Account created successfully."
    )


# ============================================
# LOGIN
# ============================================

def login_account(
    account_number,
    pin
):

    if account_number not in accounts:

        return (
            False,
            "Account not found."
        )


    if accounts[account_number]["pin"] != pin:

        return (
            False,
            "Incorrect PIN."
        )


    return (
        True,
        "Login successful."
    )


# ============================================
# GET ACCOUNT
# ============================================

def get_account(account_number):

    if account_number not in accounts:

        return None


    return accounts[account_number]


# ============================================
# DEPOSIT
# ============================================

def deposit_money(
    account_number,
    amount
):

    if account_number not in accounts:

        return (
            False,
            "Account not found."
        )


    if amount <= 0:

        return (
            False,
            "Please enter a valid amount."
        )


    accounts[account_number][
        "balance"
    ] += amount


    add_transaction(

        account_number,

        "Deposit",

        amount,

        "Money deposited into account"

    )


    save_accounts()


    return (
        True,
        "Money deposited successfully."
    )


# ============================================
# WITHDRAW
# ============================================

def withdraw_money(
    account_number,
    amount
):

    if account_number not in accounts:

        return (
            False,
            "Account not found."
        )


    if amount <= 0:

        return (
            False,
            "Please enter a valid amount."
        )


    if amount > accounts[account_number][
        "balance"
    ]:

        return (
            False,
            "Insufficient balance."
        )


    accounts[account_number][
        "balance"
    ] -= amount


    add_transaction(

        account_number,

        "Withdrawal",

        amount,

        "Money withdrawn from account"

    )


    save_accounts()


    return (
        True,
        "Money withdrawn successfully."
    )


# ============================================
# TRANSFER
# ============================================

def transfer_money(
    sender_account,
    receiver_account,
    amount
):

    if sender_account not in accounts:

        return (
            False,
            "Sender account not found."
        )


    if receiver_account not in accounts:

        return (
            False,
            "Receiver account not found."
        )


    if sender_account == receiver_account:

        return (
            False,
            "You cannot transfer money to your own account."
        )


    if amount <= 0:

        return (
            False,
            "Please enter a valid amount."
        )


    if amount > accounts[sender_account][
        "balance"
    ]:

        return (
            False,
            "Insufficient balance."
        )


    # Deduct from sender

    accounts[sender_account][
        "balance"
    ] -= amount


    # Add to receiver

    accounts[receiver_account][
        "balance"
    ] += amount


    # Sender transaction

    add_transaction(

        sender_account,

        "Transfer",

        amount,

        "Transferred to account "
        + receiver_account

    )


    # Receiver transaction

    add_transaction(

        receiver_account,

        "Transfer",

        amount,

        "Received from account "
        + sender_account

    )


    save_accounts()


    return (
        True,
        "Money transferred successfully."
    )


# ============================================
# CHANGE PIN
# ============================================

def change_pin(
    account_number,
    old_pin,
    new_pin
):

    if account_number not in accounts:

        return (
            False,
            "Account not found."
        )


    if accounts[account_number][
        "pin"
    ] != old_pin:

        return (
            False,
            "Incorrect old PIN."
        )


    if not new_pin.isdigit() or len(new_pin) != 4:

        return (
            False,
            "New PIN must contain exactly 4 digits."
        )


    accounts[account_number][
        "pin"
    ] = new_pin


    save_accounts()


    return (
        True,
        "PIN changed successfully."
    )


# ============================================
# GET TRANSACTIONS
# ============================================

def get_transactions(
    account_number
):

    if account_number not in accounts:

        return []


    return accounts[account_number][
        "transactions"
    ]


# ============================================
# ACCOUNT MENU
# ============================================

def account_menu(account_number):

    while True:

        account = get_account(
            account_number
        )


        print("\n====================================")
        print("          ACCOUNT MENU")
        print("====================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("====================================")


        choice = input(
            "Enter your choice: "
        ).strip()


        # ====================================
        # CHECK BALANCE
        # ====================================

        if choice == "1":

            account = get_account(
                account_number
            )


            print(
                "\n========== ACCOUNT BALANCE =========="
            )


            print(
                "Account Holder:",
                account["name"]
            )


            print(
                "Account Number:",
                account_number
            )


            print(
                "Current Balance: ₹",
                account["balance"]
            )


        # ====================================
        # DEPOSIT
        # ====================================

        elif choice == "2":

            print(
                "\n========== DEPOSIT MONEY =========="
            )


            try:

                amount = float(
                    input(
                        "Enter amount to deposit: "
                    )
                )


                success, message = deposit_money(

                    account_number,

                    amount

                )


                if success:

                    account = get_account(
                        account_number
                    )


                    print(
                        "₹",
                        amount,
                        "deposited successfully."
                    )


                    print(
                        "New Balance: ₹",
                        account["balance"]
                    )

                else:

                    print(message)


            except ValueError:

                print(
                    "Please enter a valid amount."
                )


        # ====================================
        # WITHDRAW
        # ====================================

        elif choice == "3":

            print(
                "\n========== WITHDRAW MONEY =========="
            )


            try:

                amount = float(
                    input(
                        "Enter amount to withdraw: "
                    )
                )


                success, message = withdraw_money(

                    account_number,

                    amount

                )


                if success:

                    account = get_account(
                        account_number
                    )


                    print(
                        "₹",
                        amount,
                        "withdrawn successfully."
                    )


                    print(
                        "Remaining Balance: ₹",
                        account["balance"]
                    )

                else:

                    print(message)


            except ValueError:

                print(
                    "Please enter a valid amount."
                )


        # ====================================
        # TRANSFER
        # ====================================

        elif choice == "4":

            print(
                "\n========== TRANSFER MONEY =========="
            )


            receiver_account = input(
                "Enter receiver account number: "
            ).strip()


            try:

                amount = float(
                    input(
                        "Enter amount to transfer: "
                    )
                )


                success, message = transfer_money(

                    account_number,

                    receiver_account,

                    amount

                )


                if success:

                    account = get_account(
                        account_number
                    )


                    print(
                        "₹",
                        amount,
                        "transferred successfully."
                    )


                    print(
                        "Remaining Balance: ₹",
                        account["balance"]
                    )

                else:

                    print(message)


            except ValueError:

                print(
                    "Please enter a valid amount."
                )


        # ====================================
        # TRANSACTION HISTORY
        # ====================================

        elif choice == "5":

            print(
                "\n========== TRANSACTION HISTORY =========="
            )


            transactions = get_transactions(
                account_number
            )


            if not transactions:

                print(
                    "No transactions found."
                )

            else:

                for index, transaction in enumerate(

                    transactions,

                    start=1

                ):

                    print(
                        "\nTransaction",
                        index
                    )


                    print(
                        "Type:",
                        transaction["type"]
                    )


                    print(
                        "Amount: ₹",
                        transaction["amount"]
                    )


                    print(
                        "Date:",
                        transaction["date"]
                    )


                    print(
                        "Details:",
                        transaction["details"]
                    )


        # ====================================
        # CHANGE PIN
        # ====================================

        elif choice == "6":

            print(
                "\n========== CHANGE PIN =========="
            )


            old_pin = input(
                "Enter your old PIN: "
            ).strip()


            new_pin = input(
                "Enter new 4-digit PIN: "
            ).strip()


            confirm_pin = input(
                "Confirm new PIN: "
            ).strip()


            if new_pin != confirm_pin:

                print(
                    "New PINs do not match."
                )

                continue


            success, message = change_pin(

                account_number,

                old_pin,

                new_pin

            )


            print(message)


        # ====================================
        # LOGOUT
        # ====================================

        elif choice == "7":

            print(
                "\nLogged out successfully."
            )

            break


        else:

            print(
                "Invalid choice. Please select 1-7."
            )


# ============================================
# MAIN MENU
# ============================================

def main():

    while True:

        print("\n====================================")
        print("          BANKING SYSTEM")
        print("====================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("====================================")


        choice = input(
            "Enter your choice: "
        ).strip()


        # ====================================
        # CREATE ACCOUNT
        # ====================================

        if choice == "1":

            print(
                "\n========== CREATE ACCOUNT =========="
            )


            name = input(
                "Enter your name: "
            ).strip()


            phone = input(
                "Enter your phone number: "
            ).strip()


            while True:

                pin = input(
                    "Create a 4-digit PIN: "
                ).strip()


                if pin.isdigit() and len(pin) == 4:

                    break


                print(
                    "Please enter a valid 4-digit PIN."
                )


            account_number, message = create_account(

                name,

                phone,

                pin

            )


            print(
                "\n" + message
            )


            if account_number:

                print(
                    "Your Account Number is:",
                    account_number
                )


                print(
                    "Please remember your Account Number and PIN."
                )


        # ====================================
        # LOGIN
        # ====================================

        elif choice == "2":

            print(
                "\n========== LOGIN =========="
            )


            account_number = input(
                "Enter account number: "
            ).strip()


            pin = input(
                "Enter PIN: "
            ).strip()


            success, message = login_account(

                account_number,

                pin

            )


            print(
                "\n" + message
            )


            if success:

                account = get_account(
                    account_number
                )


                print(
                    "Welcome,",
                    account["name"]
                )


                # Open account menu

                account_menu(
                    account_number
                )


        # ====================================
        # EXIT
        # ====================================

        elif choice == "3":

            print(
                "\nThank you for using the Banking System!"
            )

            break


        else:

            print(
                "Invalid choice. Please enter 1, 2 or 3."
            )


# ============================================
# LOAD SAVED ACCOUNTS
# ============================================

load_accounts()


# ============================================
# START TERMINAL APPLICATION
# ============================================

if __name__ == "__main__":

    main()