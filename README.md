# Banking System

A Python-based Banking System mini project that simulates basic banking operations through a menu-driven terminal application and a web-based interface.

The project allows users to create accounts, log in using an account number and PIN, check balances, deposit money, withdraw money, transfer money between accounts, view transaction history, and change their PIN.

The project includes both:

- A **Python Terminal Application**
- A **Web Application using Flask, HTML, CSS, and JavaScript**

---

## Project Overview

The Banking System is developed as a mini project to demonstrate Python programming concepts through a real-world banking application.

The system provides basic account management and transaction functionality.

Users can:

- Create a bank account
- Receive a unique account number
- Login using Account Number and PIN
- Check account balance
- Deposit money
- Withdraw money
- Transfer money
- View transaction history
- Change PIN
- Logout

Account information and transaction history are stored in a JSON file so that the data can remain available after restarting the application.

---

## Features

### Account Management

- Create a new bank account
- Enter customer name
- Enter phone number
- Create a 4-digit PIN
- Generate a unique 6-digit account number

### Login

- Login using Account Number
- Authenticate using PIN
- Display the logged-in user's account information

### Banking Operations

- Check Balance
- Deposit Money
- Withdraw Money
- Transfer Money
- View Transaction History
- Change PIN
- Logout

### Transaction Management

The system records:

- Deposits
- Withdrawals
- Transfers
- Transaction date
- Transaction time
- Transaction details

### Data Persistence

Account information is stored in:

```text
accounts.json
```

This allows account data to remain available even after closing and restarting the program.

### Web Interface

The project also provides a web interface with:

- Login
- Create Account
- Dashboard
- Check Balance
- Deposit
- Withdraw
- Transfer
- Transaction History
- Change PIN
- Logout

---

# Technologies Used

## Backend

- Python
- Flask
- JSON

## Frontend

- HTML5
- CSS3
- JavaScript

## Development Tools

- Visual Studio Code / Any Code Editor
- PowerShell / Command Prompt
- Git
- GitHub
- Web Browser

---

# Python Modules Used

The project uses the following Python modules:

### random

Used to generate unique account numbers.

### datetime

Used to record transaction date and time.

### json

Used to save and load account information from `accounts.json`.

### Flask

Used to create the web server and connect the frontend with the Python banking system.

---

# Python Concepts Used

This project demonstrates:

- Variables
- Data Types
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- String Operations
- Modules
- File Handling
- JSON
- Date and Time
- User Input
- Input Validation

---

# Project Structure

```text
Banking-System/
│
├── banking_system.py
│       Main Python banking system
│
├── app.py
│       Flask web application
│
├── accounts.json
│       Account and transaction data
│
├── README.md
│       Project documentation
│
├── .gitignore
│       Git ignored files
│
└── frontend/
        │
        ├── index.html
        │       Web interface
        │
        ├── style.css
        │       Website styling
        │
        └── script.js
                Frontend JavaScript
```

---

# Requirements

Before running the project, install the following:

- Python 3.x
- Flask
- Git
- A web browser

Git is only required if you want to clone the project from GitHub.

---

# Check Python Installation

Open PowerShell or Command Prompt.

Run:

```powershell
py --version
```

Example:

```text
Python 3.x.x
```

If the `py` command is not available, try:

```powershell
python --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

On Windows, enable the option to add Python to PATH during installation.

---

# Clone the Project from GitHub

If you want to download the project from GitHub, run:

```bash
git clone https://github.com/shankar-uxcloud/Banking-System.git
```

Then enter the project directory:

```bash
cd Banking-System
```

Check the project files:

```bash
dir
```

You should see files such as:

```text
banking_system.py
app.py
accounts.json
README.md
frontend
```

---

# Install Flask

The terminal version does not require Flask.

The web version requires Flask.

Install Flask using:

```powershell
py -m pip install flask
```

If `py` does not work, use:

```powershell
python -m pip install flask
```

Verify Flask installation:

```powershell
py -m pip show flask
```

---

# Run the Terminal Version

The terminal version runs directly using Python.

Make sure the terminal is inside the project folder.

Run:

```powershell
py banking_system.py
```

If the `py` command is not available:

```powershell
python banking_system.py
```

---

# Terminal Main Menu

After running the program, the main menu will appear.

```text
=================================
        BANKING SYSTEM
=================================

1. Create Account
2. Login
3. Exit
```

---

# Create Account

Select:

```text
1. Create Account
```

Enter:

- Name
- Phone Number
- 4-digit PIN

The system generates a unique account number.

Example:

```text
Account created successfully!
Your Account Number: 123456
```

Save the account number because it is required for login.

---

# Login

Select:

```text
2. Login
```

Enter:

- Account Number
- PIN

Example:

```text
Account Number: 123456
PIN: 1234
```

After successful authentication, the account menu will appear.

---

# Account Menu

After login:

```text
=================================
        ACCOUNT MENU
=================================

1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Transaction History
6. Change PIN
7. Logout
```

---

# 1. Check Balance

Select:

```text
1. Check Balance
```

The system displays the current account balance.

Example:

```text
Current Balance: ₹5000
```

---

# 2. Deposit Money

Select:

```text
2. Deposit
```

Enter the amount to deposit.

Example:

```text
Enter amount: 2000
```

The account balance is updated and the deposit is added to the transaction history.

---

# 3. Withdraw Money

Select:

```text
3. Withdraw
```

Enter the withdrawal amount.

Example:

```text
Enter amount: 1000
```

The system checks the available balance before completing the withdrawal.

If the account does not have enough balance, the transaction is rejected.

---

# 4. Transfer Money

Select:

```text
4. Transfer
```

Enter:

- Receiver Account Number
- Amount

Example:

```text
Receiver Account Number: 456789
Amount: 500
```

The system transfers the amount from the sender account to the receiver account.

The transfer is recorded in the transaction history.

---

# 5. Transaction History

Select:

```text
5. Transaction History
```

The system displays previous transactions.

Transactions can include:

- Deposits
- Withdrawals
- Transfers

Each transaction contains information such as:

- Transaction type
- Amount
- Date
- Time
- Transaction details

---

# 6. Change PIN

Select:

```text
6. Change PIN
```

Enter:

1. Old PIN
2. New PIN
3. Confirm New PIN

The PIN is changed after successful verification.

---

# 7. Logout

Select:

```text
7. Logout
```

The user is logged out and returned to the main menu.

---

# Run the Web Version

The project also contains a web interface.

The web application uses:

```text
HTML + CSS + JavaScript
             ↓
           Flask
             ↓
    banking_system.py
             ↓
       accounts.json
```

---

# Step 1: Install Flask

Run:

```powershell
py -m pip install flask
```

---

# Step 2: Start the Flask Server

Make sure you are inside the Banking-System project folder.

Run:

```powershell
py app.py
```

If `py` is not available:

```powershell
python app.py
```

The Flask server will start.

---

# Step 3: Open the Web Application

Open a web browser.

Go to:

```text
http://127.0.0.1:5000
```

The Banking System web interface will open.

---

# Web Application Features

The web interface provides:

- Login
- Create Account
- Dashboard
- Check Balance
- Deposit
- Withdraw
- Transfer
- Transaction History
- Change PIN
- Logout

---

# Important Web Application Instruction

When using the web version, keep the Flask terminal running.

Do not close the terminal while using the website.

The server must remain active:

```powershell
py app.py
```

To stop the Flask server:

```text
Ctrl + C
```

---

# Flask API Endpoints

The web frontend communicates with the Flask backend through the following API endpoints.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/create-account` | Create a new account |
| POST | `/api/login` | Login using account number and PIN |
| GET | `/api/account/<account_number>` | Get account information |
| POST | `/api/deposit` | Deposit money |
| POST | `/api/withdraw` | Withdraw money |
| POST | `/api/transfer` | Transfer money |
| POST | `/api/change-pin` | Change account PIN |
| GET | `/api/transactions/<account_number>` | Get transaction history |

---

# API Flow

## Create Account

```text
Frontend
   ↓
POST /api/create-account
   ↓
Flask
   ↓
banking_system.py
   ↓
accounts.json
```

## Login

```text
Frontend
   ↓
POST /api/login
   ↓
Flask
   ↓
banking_system.py
   ↓
Account verification
```

## Deposit

```text
Frontend
   ↓
POST /api/deposit
   ↓
Flask
   ↓
banking_system.py
   ↓
accounts.json
```

## Withdraw

```text
Frontend
   ↓
POST /api/withdraw
   ↓
Flask
   ↓
banking_system.py
   ↓
accounts.json
```

## Transfer

```text
Frontend
   ↓
POST /api/transfer
   ↓
Flask
   ↓
banking_system.py
   ↓
accounts.json
```

---

# Terminal Version vs Web Version

## Terminal Version

Run:

```powershell
py banking_system.py
```

Architecture:

```text
User
 ↓
Terminal
 ↓
banking_system.py
 ↓
accounts.json
```

## Web Version

Run:

```powershell
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Architecture:

```text
User
 ↓
HTML + CSS + JavaScript
 ↓
Flask
 ↓
banking_system.py
 ↓
accounts.json
```

Both versions use the same banking logic and JSON data file.

---

# Data Storage

The project uses:

```text
accounts.json
```

for storing account information and transaction history.

The stored information includes:

- Account Number
- Name
- Phone Number
- PIN
- Balance
- Transactions

The JSON file provides simple data persistence for the project.

---

# Data Persistence

The project supports data persistence.

For example:

1. Create an account.
2. Deposit money.
3. Close the program.
4. Start the program again.
5. Login using the same account number and PIN.
6. The account balance and transaction history remain available.

---

# Project Flow

```text
Create Account
       ↓
Account Number + PIN
       ↓
Login
       ↓
Account Menu
       ↓
Check Balance
       ↓
Deposit / Withdraw / Transfer
       ↓
Transaction History
       ↓
Change PIN
       ↓
Logout
       ↓
Main Menu
```

---

# Complete Application Architecture

```text
                    BANKING SYSTEM
                          │
             ┌────────────┴────────────┐
             │                         │
       Terminal Version           Web Version
             │                         │
             ↓                         ↓
   banking_system.py         HTML / CSS / JavaScript
                                       │
                                       ↓
                                    Flask
                                       │
                         ┌─────────────┴─────────────┐
                         │                           │
                         ↓                           ↓
                banking_system.py              API Endpoints
                         │
                         ↓
                  accounts.json
```

---

# Testing the Project

The following operations can be tested before submitting the project.

## Test 1: Create Account

1. Run the application.
2. Select Create Account.
3. Enter name.
4. Enter phone number.
5. Enter a 4-digit PIN.
6. Verify that an account number is generated.

## Test 2: Login

1. Select Login.
2. Enter the generated account number.
3. Enter the correct PIN.
4. Verify successful login.

## Test 3: Check Balance

1. Login.
2. Select Check Balance.
3. Verify the displayed balance.

## Test 4: Deposit

1. Login.
2. Select Deposit.
3. Enter an amount.
4. Check the balance.
5. Verify that the balance increased.

## Test 5: Withdraw

1. Login.
2. Select Withdraw.
3. Enter an amount.
4. Check the balance.
5. Verify that the balance decreased.

## Test 6: Transfer

1. Create another account.
2. Login to the sender account.
3. Select Transfer.
4. Enter the receiver account number.
5. Enter the amount.
6. Verify the sender balance.
7. Verify the receiver transaction history.

## Test 7: Transaction History

Verify that the system displays:

- Deposits
- Withdrawals
- Transfers
- Transaction dates
- Transaction times

## Test 8: Change PIN

1. Login.
2. Select Change PIN.
3. Enter the old PIN.
4. Enter a new PIN.
5. Confirm the new PIN.
6. Logout.
7. Login again using the new PIN.

## Test 9: Data Persistence

1. Create an account.
2. Perform a transaction.
3. Exit the application.
4. Start the application again.
5. Login again.
6. Verify that the account data is still available.

---

# Troubleshooting

## Python Command Not Found

If:

```powershell
python --version
```

does not work, try:

```powershell
py --version
```

On Windows, the `py` command can be used to run Python.

---

## Flask Not Installed

If you receive an error related to Flask, install it using:

```powershell
py -m pip install flask
```

Then run:

```powershell
py app.py
```

---

## Website Cannot Connect to Python Server

Make sure the Flask server is running.

Run:

```powershell
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Do not use Live Server for the Flask-connected application.

---

## Port 5000 Already in Use

If Flask reports that port 5000 is already in use:

1. Find the terminal where Flask is already running.
2. Press:

```text
Ctrl + C
```

3. Start the server again:

```powershell
py app.py
```

---

## Account Data Not Showing

Make sure:

```text
accounts.json
```

exists in the project folder.

Also make sure you are running the program from the Banking-System project directory.

---

# Git and GitHub

Git is used for version control and GitHub is used to host the project repository.

GitHub Repository:

https://github.com/shankar-uxcloud/Banking-System

---

# Clone the Repository

```bash
git clone https://github.com/shankar-uxcloud/Banking-System.git
```

Then:

```bash
cd Banking-System
```

---

# Git Commands Used

Initialize Git:

```bash
git init
```

Check status:

```bash
git status
```

Add project files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial banking system project"
```

Connect GitHub repository:

```bash
git remote add origin https://github.com/shankar-uxcloud/Banking-System.git
```

Rename branch to main:

```bash
git branch -M main
```

Push project to GitHub:

```bash
git push -u origin main
```

---

# Updating the Project on GitHub

After making changes:

```bash
git status
```

Add the changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Update banking system"
```

Push:

```bash
git push
```

---

# Security Note

This project is an educational banking system simulation.

It is **not intended to be used as a real banking application**.

The project uses a simple JSON file for data storage and is designed for learning purposes.

A production banking application would require stronger security measures such as:

- Secure authentication
- PIN/password hashing
- Encryption
- Database security
- Secure API communication
- Session management
- Access control
- Input validation
- Logging and monitoring
- Secure secrets management

---

# Future Improvements

Possible future improvements include:

- Replace JSON storage with MySQL or PostgreSQL
- Add secure PIN/password hashing
- Add proper user sessions
- Add an admin dashboard
- Improve input validation
- Add automated tests
- Add email or SMS notifications
- Add transaction reports
- Improve responsive design
- Deploy the web application online
- Add stronger authentication
- Add database-backed transaction management

---

# Real-World Application

This project demonstrates how programming concepts can be applied to a real-world banking scenario.

It covers:

- Account management
- User authentication
- Balance management
- Money transactions
- Transaction records
- PIN management
- Data persistence
- Backend and frontend integration

---

# Learning Objectives

The main objective of this project is to combine basic Python programming concepts into a working real-world application.

The project provides practical experience with:

- Python programming
- Functions
- Conditional statements
- Loops
- Lists
- Dictionaries
- File handling
- JSON
- Python modules
- Flask
- HTML
- CSS
- JavaScript
- Git
- GitHub

---

# Quick Start

## Terminal Version

Clone the project:

```bash
git clone https://github.com/shankar-uxcloud/Banking-System.git
```

Enter the project folder:

```bash
cd Banking-System
```

Run:

```powershell
py banking_system.py
```

---

## Web Version

Clone the project:

```bash
git clone https://github.com/shankar-uxcloud/Banking-System.git
```

Enter the project folder:

```bash
cd Banking-System
```

Install Flask:

```powershell
py -m pip install flask
```

Start the server:

```powershell
py app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# Complete Command Summary

For the terminal version:

```powershell
git clone https://github.com/shankar-uxcloud/Banking-System.git
cd Banking-System
py banking_system.py
```

For the web version:

```powershell
git clone https://github.com/shankar-uxcloud/Banking-System.git
cd Banking-System
py -m pip install flask
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# Author

**P SHANKAR**

GitHub:

https://github.com/shankar-uxcloud/Banking-System

---

# License

This project is created for educational and learning purposes.
