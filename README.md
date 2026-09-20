# Banking System

A Python-based Banking System mini project that allows users to create and manage bank accounts through a menu-driven terminal application and a simple web interface.

## Project Description

This project is developed using Python to demonstrate basic programming concepts through a real-world banking application.

Users can create an account, log in using their account number and PIN, check their balance, deposit and withdraw money, transfer money, view transaction history, and change their PIN.

The project also includes a simple web interface built using HTML, CSS, JavaScript, and Flask.

## Features

- Create a new bank account
- Generate a unique account number
- Login using Account Number and PIN
- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts
- View transaction history
- Change PIN
- Logout
- Save account data using JSON
- Terminal-based interface
- Web-based interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- JSON

## Python Concepts Used

- Variables and Data Types
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

## Python Modules Used

- `random` - Used to generate account numbers
- `datetime` - Used to record transaction date and time
- `json` - Used to store account information
- `Flask` - Used to connect the Python banking system with the web interface

## Project Structure

```text
Banking-System/
│
├── banking_system.py
├── app.py
├── accounts.json
├── README.md
├── .gitignore
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js

How to Run the Terminal Version
1. Open the project folder

Open PowerShell or Command Prompt inside the project folder.

2. Run the Python program
py banking_system.py

The terminal menu will appear.

Main Menu
1. Create Account
2. Login
3. Exit

After logging in, users can access the account menu.

Account Menu
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Transaction History
6. Change PIN
7. Logout
How to Run the Web Version
1. Install Flask
py -m pip install flask
2. Start the Flask server
py app.py
3. Open the website

Open the following address in your browser:

http://127.0.0.1:5000

The web interface provides the same main banking operations through a graphical interface.

Data Storage

Account information and transaction history are stored in:

accounts.json

This allows account data to remain available after the program is closed and started again.

Project Flow
Create Account
       ↓
Account Number + PIN
       ↓
Login
       ↓
Account Menu
       ↓
Banking Operations
       ↓
Logout
       ↓
Main Menu
Real-World Application

This project demonstrates how programming concepts can be applied to a simple banking system.

It covers:

Account management
User authentication
Money transactions
Transaction records
PIN management
Data storage
Future Improvements
Add a database such as MySQL or PostgreSQL
Improve authentication and security
Add password/PIN hashing
Add an admin dashboard
Add better input validation
Deploy the web application online

Author

P SHANKAR

GitHub: https://github.com/shankar-uxcloud

    
