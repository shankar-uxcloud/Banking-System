// ========================================
// BANKING SYSTEM FRONTEND
// ========================================


// ================================
// ELEMENTS
// ================================

const loginPage =
    document.getElementById("loginPage");

const createAccountPage =
    document.getElementById("createAccountPage");

const dashboardPage =
    document.getElementById("dashboardPage");

const loginForm =
    document.getElementById("loginForm");

const createAccountForm =
    document.getElementById("createAccountForm");

const showCreateAccount =
    document.getElementById("showCreateAccount");

const backToLogin =
    document.getElementById("backToLogin");

const logoutButton =
    document.getElementById("logoutButton");

const navButtons =
    document.querySelectorAll(".nav-button");


// ================================
// CURRENT USER
// ================================

let currentUser = null;

let currentAccountNumber = null;


// ================================
// SHOW CREATE ACCOUNT
// ================================

showCreateAccount.addEventListener(
    "click",
    function () {

        loginPage.classList.add("hidden");

        createAccountPage.classList.remove(
            "hidden"
        );

    }
);


// ================================
// BACK TO LOGIN
// ================================

backToLogin.addEventListener(
    "click",
    function () {

        createAccountPage.classList.add(
            "hidden"
        );

        loginPage.classList.remove(
            "hidden"
        );

    }
);


// ================================
// LOGIN
// ================================

loginForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();

        const accountNumber =
            document
                .getElementById("accountNumber")
                .value
                .trim();

        const pin =
            document
                .getElementById("loginPin")
                .value
                .trim();

        const loginMessage =
            document.getElementById(
                "loginMessage"
            );


        try {

            const response = await fetch(
                "/api/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        accountNumber:
                            accountNumber,

                        pin: pin
                    })
                }
            );


            const data =
                await response.json();


            if (!response.ok) {

                showMessage(
                    loginMessage,
                    "error",
                    data.message
                );

                return;
            }


            currentAccountNumber =
                data.accountNumber;

            currentUser =
                data.account;


            showMessage(
                loginMessage,
                "success",
                "Login successful!"
            );


            setTimeout(
                function () {

                    loginPage.classList.add(
                        "hidden"
                    );

                    dashboardPage.classList.remove(
                        "hidden"
                    );

                    loadDashboard();

                },
                500
            );


        } catch (error) {

            showMessage(
                loginMessage,
                "error",
                "Unable to connect to Python server."
            );

        }

    }
);


// ================================
// CREATE ACCOUNT
// ================================

createAccountForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const name =
            document
                .getElementById("accountName")
                .value
                .trim();


        const phone =
            document
                .getElementById("phoneNumber")
                .value
                .trim();


        const pin =
            document
                .getElementById("createPin")
                .value
                .trim();


        const confirmPin =
            document
                .getElementById("confirmPin")
                .value
                .trim();


        const createMessage =
            document.getElementById(
                "createMessage"
            );


        if (!/^\d{4}$/.test(pin)) {

            showMessage(
                createMessage,
                "error",
                "PIN must contain exactly 4 digits."
            );

            return;
        }


        if (pin !== confirmPin) {

            showMessage(
                createMessage,
                "error",
                "PINs do not match."
            );

            return;
        }


        try {

            const response = await fetch(
                "/api/create-account",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        name: name,

                        phone: phone,

                        pin: pin

                    })
                }
            );


            const data =
                await response.json();


            if (!response.ok) {

                showMessage(
                    createMessage,
                    "error",
                    data.message
                );

                return;
            }


            // Display the REAL account number
            createMessage.className =
                "message success";

            createMessage.innerHTML = `
                <strong>
                    Account created successfully!
                </strong>

                <br><br>

                Your Account Number:

                <br>

                <strong class="account-number-display">
                    ${data.accountNumber}
                </strong>

                <br><br>

                Please remember your Account Number and PIN.
            `;


            // Clear form
            createAccountForm.reset();


        } catch (error) {

            showMessage(
                createMessage,
                "error",
                "Unable to connect to Python server."
            );

        }

    }
);


// ================================
// LOAD DASHBOARD
// ================================

function loadDashboard() {

    if (!currentUser) {
        return;
    }


    document.getElementById(
        "userName"
    ).textContent =
        currentUser.name;


    document.getElementById(
        "dashboardName"
    ).textContent =
        currentUser.name;


    document.getElementById(
        "cardUserName"
    ).textContent =
        currentUser.name;


    document.getElementById(
        "userAccount"
    ).textContent =
        "Account: " +
        currentAccountNumber;


    document.getElementById(
        "cardAccountNumber"
    ).textContent =
        currentAccountNumber;


    document.getElementById(
        "userAvatar"
    ).textContent =
        currentUser.name
            .charAt(0)
            .toUpperCase();


    updateBalance();

    displayRecentTransactions();

}


// ================================
// UPDATE USER DATA
// ================================

function updateUserData(account) {

    currentUser = account;

    updateBalance();

    displayRecentTransactions();

}


// ================================
// UPDATE BALANCE
// ================================

function updateBalance() {

    if (!currentUser) {
        return;
    }


    const formattedBalance =
        "₹ " +
        Number(
            currentUser.balance
        ).toFixed(2);


    document.getElementById(
        "balanceAmount"
    ).textContent =
        formattedBalance;


    document.getElementById(
        "balancePageAmount"
    ).textContent =
        formattedBalance;

}


// ================================
// RECENT TRANSACTIONS
// ================================

function displayRecentTransactions() {

    if (!currentUser) {
        return;
    }


    const container =
        document.getElementById(
            "recentTransactions"
        );


    const transactions =
        currentUser.transactions || [];


    if (transactions.length === 0) {

        container.innerHTML =
            '<p class="empty-message">No transactions yet.</p>';

        return;
    }


    container.innerHTML = "";


    transactions
        .slice(-5)
        .reverse()
        .forEach(
            function (transaction) {

                const item =
                    document.createElement(
                        "div"
                    );


                item.className =
                    "transaction-item";


                item.innerHTML = `

                    <div class="transaction-left">

                        <div class="transaction-icon">
                            ${getTransactionIcon(
                                transaction.type
                            )}
                        </div>

                        <div class="transaction-details">

                            <strong>
                                ${transaction.type}
                            </strong>

                            <small>
                                ${transaction.date}
                            </small>

                        </div>

                    </div>


                    <div class="transaction-amount">

                        ₹ ${Number(
                            transaction.amount
                        ).toFixed(2)}

                    </div>

                `;


                container.appendChild(item);

            }
        );

}


// ================================
// TRANSACTION ICON
// ================================

function getTransactionIcon(type) {

    if (type === "Deposit") {
        return "➕";
    }

    if (type === "Withdrawal") {
        return "➖";
    }

    if (type === "Transfer") {
        return "↔️";
    }

    return "💰";

}


// ================================
// NAVIGATION
// ================================

navButtons.forEach(
    function (button) {

        button.addEventListener(
            "click",
            function () {

                const section =
                    button.getAttribute(
                        "data-section"
                    );

                showSection(section);

            }
        );

    }
);


// ================================
// SHOW SECTION
// ================================

function showSection(section) {

    const sections =
        document.querySelectorAll(
            ".content-section"
        );


    sections.forEach(
        function (item) {

            item.classList.remove(
                "active-section"
            );

        }
    );


    navButtons.forEach(
        function (button) {

            button.classList.remove(
                "active"
            );

        }
    );


    const targetSection =
        document.getElementById(
            section + "Section"
        );


    if (targetSection) {

        targetSection.classList.add(
            "active-section"
        );

    }


    const activeButton =
        document.querySelector(
            `.nav-button[data-section="${section}"]`
        );


    if (activeButton) {

        activeButton.classList.add(
            "active"
        );

    }


    const titles = {

        dashboard:
            "Dashboard",

        balance:
            "Check Balance",

        deposit:
            "Deposit Money",

        withdraw:
            "Withdraw Money",

        transfer:
            "Transfer Money",

        history:
            "Transaction History",

        changePin:
            "Change PIN"

    };


    document.getElementById(
        "pageTitle"
    ).textContent =
        titles[section] ||
        "Dashboard";


    if (section === "history") {

        displayTransactionHistory();

    }

}


// ================================
// DEPOSIT
// ================================

document.getElementById(
    "depositForm"
).addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const amount =
            Number(
                document.getElementById(
                    "depositAmount"
                ).value
            );


        const message =
            document.getElementById(
                "depositMessage"
            );


        if (amount <= 0) {

            showMessage(
                message,
                "error",
                "Please enter a valid amount."
            );

            return;
        }


        try {

            const response =
                await fetch(
                    "/api/deposit",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            accountNumber:
                                currentAccountNumber,

                            amount:
                                amount

                        })
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                showMessage(
                    message,
                    "error",
                    data.message
                );

                return;
            }


            updateUserData(
                data.account
            );


            document.getElementById(
                "depositAmount"
            ).value = "";


            showMessage(
                message,
                "success",
                "₹ " +
                amount.toFixed(2) +
                " deposited successfully."
            );


        } catch (error) {

            showMessage(
                message,
                "error",
                "Unable to connect to server."
            );

        }

    }
);


// ================================
// WITHDRAW
// ================================

document.getElementById(
    "withdrawForm"
).addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const amount =
            Number(
                document.getElementById(
                    "withdrawAmount"
                ).value
            );


        const message =
            document.getElementById(
                "withdrawMessage"
            );


        if (amount <= 0) {

            showMessage(
                message,
                "error",
                "Please enter a valid amount."
            );

            return;
        }


        try {

            const response =
                await fetch(
                    "/api/withdraw",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            accountNumber:
                                currentAccountNumber,

                            amount:
                                amount

                        })
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                showMessage(
                    message,
                    "error",
                    data.message
                );

                return;
            }


            updateUserData(
                data.account
            );


            document.getElementById(
                "withdrawAmount"
            ).value = "";


            showMessage(
                message,
                "success",
                "₹ " +
                amount.toFixed(2) +
                " withdrawn successfully."
            );


        } catch (error) {

            showMessage(
                message,
                "error",
                "Unable to connect to server."
            );

        }

    }
);


// ================================
// TRANSFER
// ================================

document.getElementById(
    "transferForm"
).addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const receiver =
            document.getElementById(
                "receiverAccount"
            ).value.trim();


        const amount =
            Number(
                document.getElementById(
                    "transferAmount"
                ).value
            );


        const message =
            document.getElementById(
                "transferMessage"
            );


        if (amount <= 0) {

            showMessage(
                message,
                "error",
                "Please enter a valid amount."
            );

            return;
        }


        try {

            const response =
                await fetch(
                    "/api/transfer",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            senderAccount:
                                currentAccountNumber,

                            receiverAccount:
                                receiver,

                            amount:
                                amount

                        })
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                showMessage(
                    message,
                    "error",
                    data.message
                );

                return;
            }


            updateUserData(
                data.account
            );


            document.getElementById(
                "receiverAccount"
            ).value = "";


            document.getElementById(
                "transferAmount"
            ).value = "";


            showMessage(
                message,
                "success",
                "₹ " +
                amount.toFixed(2) +
                " transferred successfully."
            );


        } catch (error) {

            showMessage(
                message,
                "error",
                "Unable to connect to server."
            );

        }

    }
);


// ================================
// TRANSACTION HISTORY
// ================================

function displayTransactionHistory() {

    if (!currentUser) {
        return;
    }


    const container =
        document.getElementById(
            "transactionHistory"
        );


    const transactions =
        currentUser.transactions || [];


    if (transactions.length === 0) {

        container.innerHTML =
            '<p class="empty-message">No transactions found.</p>';

        return;
    }


    container.innerHTML = "";


    transactions
        .slice()
        .reverse()
        .forEach(
            function (transaction) {

                const item =
                    document.createElement(
                        "div"
                    );


                item.className =
                    "transaction-item";


                item.innerHTML = `

                    <div class="transaction-left">

                        <div class="transaction-icon">
                            ${getTransactionIcon(
                                transaction.type
                            )}
                        </div>

                        <div class="transaction-details">

                            <strong>
                                ${transaction.type}
                            </strong>

                            <small>
                                ${transaction.date}
                            </small>

                            <small>
                                ${transaction.details}
                            </small>

                        </div>

                    </div>


                    <div class="transaction-amount">

                        ₹ ${Number(
                            transaction.amount
                        ).toFixed(2)}

                    </div>

                `;


                container.appendChild(item);

            }
        );

}


// ================================
// CHANGE PIN
// ================================

document.getElementById(
    "changePinForm"
).addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const oldPin =
            document.getElementById(
                "oldPin"
            ).value.trim();


        const newPin =
            document.getElementById(
                "newPin"
            ).value.trim();


        const confirmPin =
            document.getElementById(
                "confirmNewPin"
            ).value.trim();


        const message =
            document.getElementById(
                "pinMessage"
            );


        if (!/^\d{4}$/.test(newPin)) {

            showMessage(
                message,
                "error",
                "New PIN must contain exactly 4 digits."
            );

            return;
        }


        if (newPin !== confirmPin) {

            showMessage(
                message,
                "error",
                "PINs do not match."
            );

            return;
        }


        try {

            const response =
                await fetch(
                    "/api/change-pin",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            accountNumber:
                                currentAccountNumber,

                            oldPin:
                                oldPin,

                            newPin:
                                newPin

                        })
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                showMessage(
                    message,
                    "error",
                    data.message
                );

                return;
            }


            showMessage(
                message,
                "success",
                data.message
            );


            document.getElementById(
                "changePinForm"
            ).reset();


        } catch (error) {

            showMessage(
                message,
                "error",
                "Unable to connect to server."
            );

        }

    }
);


// ================================
// LOGOUT
// ================================

logoutButton.addEventListener(
    "click",
    function () {

        currentUser = null;

        currentAccountNumber = null;


        dashboardPage.classList.add(
            "hidden"
        );

        loginPage.classList.remove(
            "hidden"
        );


        loginForm.reset();

        createAccountForm.reset();


        document.getElementById(
            "loginMessage"
        ).className =
            "message";

    }
);


// ================================
// MESSAGE
// ================================

function showMessage(
    element,
    type,
    text
) {

    element.className =
        "message " + type;

    element.textContent =
        text;

}


// ================================
// VIEW ALL
// ================================

document
    .querySelectorAll(
        '[data-section="history"]'
    )
    .forEach(
        function (button) {

            button.addEventListener(
                "click",
                function () {

                    showSection(
                        "history"
                    );

                }
            );

        }
    );