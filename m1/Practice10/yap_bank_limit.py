import yap_bank_transactions


DAILY_WITHDRAWAL_LIMIT = 10000.00


def get_daily_withdrawal(account):

    transactions = yap_bank_transactions.get_transactions()

    total_withdrawal = 0.0

    for transaction in transactions:

        if (
            transaction.get("account_number")
            == account.account_number
            and transaction.get("transaction")
            == "Withdraw"
        ):

            total_withdrawal += float(
                transaction.get("amount", 0.0)
            )

    return total_withdrawal


def check_withdrawal_limit(account, amount):

    daily_withdrawal = get_daily_withdrawal(account)

    remaining_limit = (
        DAILY_WITHDRAWAL_LIMIT
        - daily_withdrawal
    )

    if amount > remaining_limit:

        return {
            "success": False,

            "message":
                f"Daily withdrawal limit exceeded. "
                f"You can only withdraw "
                f"₱{remaining_limit:,.2f} more today.",

            "remaining_limit":
                remaining_limit
        }

    return {
        "success": True,

        "message":
            "Withdrawal is within the daily limit.",

        "remaining_limit":
            remaining_limit - amount
    }