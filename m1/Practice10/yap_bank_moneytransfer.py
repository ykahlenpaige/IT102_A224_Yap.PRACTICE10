import yap_bank_transactions


def transfer_money(
    account,
    recipient_account,
    amount
):

    if recipient_account == "":
        return {
            "success": False,
            "message":
                "Please enter a recipient account number."
        }


    if amount <= 0:
        return {
            "success": False,
            "message":
                "Transfer amount must be greater than ₱0."
        }


    if recipient_account == account.account_number:
        return {
            "success": False,
            "message":
                "You cannot transfer money to your own account."
        }


    if amount > account.check_balance():
        return {
            "success": False,
            "message":
                "Insufficient balance."
        }


    account._balance -= amount


    yap_bank_transactions.add_transaction(
        account_number=account.account_number,
        transaction="Transfer",
        amount=amount
    )


    return {
        "success": True,

        "message":
            f"Successfully transferred "
            f"₱{amount:,.2f} to account "
            f"{recipient_account}.",

        "recipient_account":
            recipient_account,

        "amount":
            amount,

        "remaining_balance":
            account.check_balance()
    }
```
