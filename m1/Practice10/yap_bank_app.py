import streamlit as st

import yap_bank_auth
import yap_bank_storage
import yap_bank_transactions
import yap_bank_analysis
import yap_bank_utils


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="✪ YAP ✪ Bank",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "account" not in st.session_state:

    st.session_state.account = None


st.title("✪ YAP ✪ BANK")

st.caption(
    "Secure Digital Banking System"
)


if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    with login_tab:

        st.subheader(
            "Welcome Back"
        )

        account_number = st.text_input(
            "Account Number",
            key="login_account"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="login_pin"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            account, message = (
                yap_bank_auth
                .login_account(
                    account_number,
                    pin
                )
            )

            if account is not None:

                st.session_state.logged_in = True

                st.session_state.account = (
                    account
                )

                st.success(message)

                st.rerun()

            else:

                st.error(message)

    with register_tab:

        st.subheader(
            "Create Your ✪ YAP ✪ Bank Account"
        )

        name = st.text_input(
            "Full Name",
            key="register_name"
        )

        account_number = st.text_input(
            "Account Number",
            key="register_account"
        )

        pin = st.text_input(
            "Create 4-Digit PIN",
            type="password",
            key="register_pin"
        )

        confirm_pin = st.text_input(
            "Confirm PIN",
            type="password",
            key="register_confirm_pin"
        )

        account_type = st.selectbox(
            "Account Type",
            [
                "Savings Account",
                "Student Account"
            ]
        )

        starting_balance = st.number_input(
            "Starting Balance",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            account, message = (
                yap_bank_auth
                .register_account(
                    name,
                    account_number,
                    pin,
                    confirm_pin,
                    account_type,
                    starting_balance
                )
            )

            if account is not None:

                st.success(message)

                st.info(
                    "Your account has been created. "
                    "Please use the Login tab."
                )

            else:

                st.error(message)

else:

    account = (
        st.session_state.account
    )


    st.sidebar.title(
        "✪ YAP ✪ BANK"
    )

    st.sidebar.write(
        f"**{account.account_name}**"
    )

    st.sidebar.caption(
        account.get_account_type()
    )

    st.sidebar.write(
        f"Account: "
        f"{account.account_number}"
    )

    st.sidebar.divider()

    # Slightly added styling for the banking menu
    st.markdown("""
    <style>
    /* Clean containers for the sidebar menu */
    [data-testid="stSidebar"] [role="radiogroup"] label {
        background-color: #30333d;
        border: 1px solid #454955;
        border-radius: 8px;
        padding: 10px 12px;
        margin-bottom: 6px;
        color: #f1f5f9;
        width: 100%;
        min-height: 44px;
        box-sizing: border-box;
        justify-content: center;
        text-align: center;
        transition: all 0.2s ease;
    }

    /* Keep all menu text centered */
    [data-testid="stSidebar"] [role="radiogroup"] label > div:last-child {
        width: 100%;
        justify-content: center;
        text-align: center;
    }

    /* Style the radio indicator to match the blue theme */
    [data-testid="stSidebar"] [role="radiogroup"] input[type="radio"] {
        accent-color: #93c5fd;
    }

    /* Make the selected indicator a soft blue instead of red */
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) input[type="radio"] {
        accent-color: #dbeafe;
    }

    /* Professional blue highlight when selected */
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background-color: #2563eb;
        border-color: #2563eb;
        color: #ffffff;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(37, 99, 235, 0.25);
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background-color: #3b4252;
        border-color: #60a5fa;
        color: #ffffff;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked):hover {
        background-color: #1d4ed8;
        border-color: #1d4ed8;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

    menu = st.sidebar.radio(
        "BANKING MENU",
        [
            "Dashboard",
            "Deposit",
            "Withdraw",
            "Transaction History",
            "Transaction Analysis"
        ]
    )


    st.sidebar.divider()


    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.account = None

        st.rerun()

    if menu == "Dashboard":

        st.header(
            f"Welcome, {account.account_name}"
        )

        st.subheader(
            "Account Overview"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Current Balance",
            yap_bank_utils
            .format_currency(
                account.check_balance()
            )
        )


        col2.metric(
            "Account Type",
            account.get_account_type()
        )


        col3.metric(
            "Account Number",
            account.account_number
        )


        st.divider()


        st.info(
            "Select a banking service from "
            "the menu on the left."
        )

    elif menu == "Deposit":

        st.header(
            "Deposit Money"
        )

        st.write(
            f"Current Balance: "
            f"**{yap_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "Confirm Deposit",
            use_container_width=True
        ):

            if not yap_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "Invalid deposit amount."
                )

            else:

                success = account.deposit(
                    amount
                )

                if success:

                    yap_bank_storage.update_account(
                        account
                    )

                    yap_bank_transactions.record_transaction(
                        account,
                        "Deposit",
                        amount
                    )

                    st.success(
                        "Deposit successful."
                    )

                    st.metric(
                        "New Balance",
                        yap_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    elif menu == "Withdraw":

        st.header(
            "Withdraw Money"
        )

        st.write(
            f"Available Balance: "
            f"**{yap_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "Confirm Withdrawal",
            use_container_width=True
        ):

            if not yap_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "Invalid withdrawal amount."
                )

            elif amount > account.check_balance():

                st.error(
                    "Insufficient balance."
                )

            else:

                success = account.withdraw(
                    amount
                )

                if success:

                    yap_bank_storage.update_account(
                        account
                    )

                    yap_bank_transactions.record_transaction(
                        account,
                        "Withdraw",
                        amount
                    )

                    st.success(
                        "Withdrawal successful."
                    )

                    st.metric(
                        "New Balance",
                        yap_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    elif menu == "Transaction History":

        st.header(
            "Transaction History"
        )

        transactions = (
            yap_bank_transactions
            .get_transactions()
        )

        transactions = [
            transaction
            for transaction in transactions
            if transaction.get(
                "account_number"
            ) == account.account_number
        ]


        if transactions:

            display_data = []

            for transaction in transactions:

                display_data.append({

                    "Timestamp":
                        transaction.get(
                            "timestamp",
                            "N/A"
                        ),

                    "Transaction":
                        transaction.get(
                            "transaction",
                            "N/A"
                        ),

                    "Amount":
                        yap_bank_utils
                        .format_currency(
                            transaction.get(
                                "amount",
                                0
                            )
                        ),

                    "Balance After":
                        yap_bank_utils
                        .format_currency(
                            transaction.get(
                                "balance_after",
                                0
                            )
                        )
                })


            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No transaction history available."
            )



    elif menu == "Transaction Analysis":

        st.header(
            "Transaction Analysis"
        )

        result = (
            yap_bank_analysis
            .analyze_transactions(
                account.account_number
            )
        )


        st.subheader(
            "1. Transaction Summary"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Transactions",
            result[
                "total_transactions"
            ]
        )


        col2.metric(
            "Deposits",
            result[
                "deposits"
            ]
        )


        col3.metric(
            "Withdrawals",
            result[
                "withdrawals"
            ]
        )


        st.divider()

        st.subheader(
            "2. Money Flow Analysis"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Deposited",
            yap_bank_utils
            .format_currency(
                result[
                    "total_deposited"
                ]
            )
        )


        col2.metric(
            "Total Withdrawn",
            yap_bank_utils
            .format_currency(
                result[
                    "total_withdrawn"
                ]
            )
        )


        col3.metric(
            "Net Cash Flow",
            yap_bank_utils
            .format_currency(
                result[
                    "net_cash_flow"
                ]
            )
        )


        st.divider()

        st.subheader(
            "3. Account Activity Analysis"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Largest Transaction",
            yap_bank_utils
            .format_currency(
                result[
                    "largest_transaction"
                ]
            )
        )


        col2.metric(
            "Average Transaction",
            yap_bank_utils
            .format_currency(
                result[
                    "average_transaction"
                ]
            )
        )


        col3.metric(
            "Latest Transaction",
            result[
                "latest_transaction"
            ]
        )


        st.caption(
            f"Latest Activity: "
            f"{result['latest_timestamp']}"
        )