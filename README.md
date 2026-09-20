# Banking-System

A lightweight MVC web application for managing bank accounts and transactions.

![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&style=flat-square)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5&style=flat-square)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3&style=flat-square)

## Overview

Banking-System is a simple web-based application for managing accounts and processing transactions. It features a clear separation between the frontend (HTML/CSS/JavaScript) and the backend (Python), using a JSON file for data storage. The app allows users to create, update, and delete bank accounts, as well as perform and review transactions, all through an intuitive browser interface.

## Tech Stack

- **Backend:** Python (Flask or similar minimal web server)
- **Frontend:** 
  - HTML5
  - CSS3
  - JavaScript (ES6)
- **Data Storage:** JSON file (`accounts.json`)
- **Architecture:** MVC (Model-View-Controller) Web App

## Prerequisites

- Python 3.x installed on your system
- Web browser (Chrome, Firefox, Edge, etc.)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shankar-uxcloud/Banking-System.git
   cd Banking-System
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **No additional dependencies are required.**

## Usage

1. **Run the backend Python application**
   
   You can start either `app.py` or `banking_system.py` (depending on your preference):

   ```bash
   python app.py
   ```
   or
   ```bash
   python banking_system.py
   ```

   The backend will listen for HTTP requests locally.

2. **Open the frontend**

   Open `frontend/index.html` in your web browser:

   - You can double-click the file or open it via the browser's "Open File" dialog.

3. **Interact with the application**

   - Use the frontend interface to view, add, update, or delete accounts.
   - Perform transactions and view transaction history.
   - All data changes are saved to `accounts.json`.

## Project Structure

```
Banking-System/
├── .gitignore
├── README.md
├── accounts.json           # Data storage for accounts and transactions
├── app.py                  # Backend server logic
├── banking_system.py       # Core banking logic (can also act as entry point)
└── frontend/
    ├── index.html          # Main user interface
    ├── script.js           # Frontend JavaScript logic
    └── style.css           # Frontend styles
```

## API Endpoints

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | `/accounts`           | Retrieve account information   |
| POST   | `/accounts`           | Create a new account           |
| PUT    | `/accounts/:id`       | Update account details         |
| DELETE | `/accounts/:id`       | Delete an account              |
| GET    | `/transactions`       | List all transactions          |
| POST   | `/transactions`       | Create a new transaction       |

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** this repository
2. **Create** a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes and push to your fork
4. **Open a Pull Request** describing your changes

## License

License not specified. Please contact the repository owner for information regarding usage and distribution.

---
[![README powered by ReadmeAI](https://img.shields.io/badge/README-powered%20by%20ReadmeAI-4c9be8?style=flat-square&logo=markdown)](https://www.readmeai.in)
