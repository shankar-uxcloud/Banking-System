from flask import Flask, request, jsonify, send_from_directory
import banking_system


app = Flask(__name__, static_folder="frontend")


# ================================
# FRONTEND
# ================================

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")


@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory("frontend", filename)


# ================================
# CREATE ACCOUNT
# ================================

@app.route("/api/create-account", methods=["POST"])
def create_account():

    data = request.get_json()

    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    pin = data.get("pin", "").strip()

    account_number, message = banking_system.create_account(
        name,
        phone,
        pin
    )

    if account_number is None:

        return jsonify({
            "success": False,
            "message": message
        }), 400

    return jsonify({
        "success": True,
        "message": message,
        "accountNumber": account_number
    })


# ================================
# LOGIN
# ================================

@app.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    account_number = data.get(
        "accountNumber",
        ""
    ).strip()

    pin = data.get(
        "pin",
        ""
    ).strip()

    success, message = banking_system.login_account(
        account_number,
        pin
    )

    if not success:

        return jsonify({
            "success": False,
            "message": message
        }), 401

    account = banking_system.get_account(
        account_number
    )

    return jsonify({
        "success": True,
        "message": message,
        "accountNumber": account_number,
        "account": account
    })


# ================================
# GET ACCOUNT
# ================================

@app.route("/api/account/<account_number>", methods=["GET"])
def get_account(account_number):

    account = banking_system.get_account(
        account_number
    )

    if account is None:

        return jsonify({
            "success": False,
            "message": "Account not found."
        }), 404

    return jsonify({
        "success": True,
        "accountNumber": account_number,
        "account": account
    })


# ================================
# DEPOSIT
# ================================

@app.route("/api/deposit", methods=["POST"])
def deposit():

    data = request.get_json()

    account_number = data.get(
        "accountNumber",
        ""
    ).strip()

    try:
        amount = float(data.get("amount", 0))
    except (ValueError, TypeError):
        amount = 0

    success, message = banking_system.deposit_money(
        account_number,
        amount
    )

    if not success:

        return jsonify({
            "success": False,
            "message": message
        }), 400

    account = banking_system.get_account(
        account_number
    )

    return jsonify({
        "success": True,
        "message": message,
        "account": account
    })


# ================================
# WITHDRAW
# ================================

@app.route("/api/withdraw", methods=["POST"])
def withdraw():

    data = request.get_json()

    account_number = data.get(
        "accountNumber",
        ""
    ).strip()

    try:
        amount = float(data.get("amount", 0))
    except (ValueError, TypeError):
        amount = 0

    success, message = banking_system.withdraw_money(
        account_number,
        amount
    )

    if not success:

        return jsonify({
            "success": False,
            "message": message
        }), 400

    account = banking_system.get_account(
        account_number
    )

    return jsonify({
        "success": True,
        "message": message,
        "account": account
    })


# ================================
# TRANSFER
# ================================

@app.route("/api/transfer", methods=["POST"])
def transfer():

    data = request.get_json()

    sender_account = data.get(
        "senderAccount",
        ""
    ).strip()

    receiver_account = data.get(
        "receiverAccount",
        ""
    ).strip()

    try:
        amount = float(data.get("amount", 0))
    except (ValueError, TypeError):
        amount = 0

    success, message = banking_system.transfer_money(
        sender_account,
        receiver_account,
        amount
    )

    if not success:

        return jsonify({
            "success": False,
            "message": message
        }), 400

    account = banking_system.get_account(
        sender_account
    )

    return jsonify({
        "success": True,
        "message": message,
        "account": account
    })


# ================================
# CHANGE PIN
# ================================

@app.route("/api/change-pin", methods=["POST"])
def change_pin():

    data = request.get_json()

    account_number = data.get(
        "accountNumber",
        ""
    ).strip()

    old_pin = data.get(
        "oldPin",
        ""
    ).strip()

    new_pin = data.get(
        "newPin",
        ""
    ).strip()

    success, message = banking_system.change_pin(
        account_number,
        old_pin,
        new_pin
    )

    if not success:

        return jsonify({
            "success": False,
            "message": message
        }), 400

    return jsonify({
        "success": True,
        "message": message
    })


# ================================
# TRANSACTION HISTORY
# ================================

@app.route("/api/transactions/<account_number>", methods=["GET"])
def transactions(account_number):

    transactions = banking_system.get_transactions(
        account_number
    )

    return jsonify({
        "success": True,
        "transactions": transactions
    })


# ================================
# RUN SERVER
# ================================

if __name__ == "__main__":

    print("\n====================================")
    print("       BANKING SYSTEM WEB APP")
    print("====================================")
    print("Open: http://127.0.0.1:5000")
    print("====================================\n")

    app.run(debug=True)