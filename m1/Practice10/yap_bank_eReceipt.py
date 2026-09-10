def create_receipt(
    account,
    transaction_type,
    amount
):

    balance_after = (
        account.check_balance()
    )


    receipt = {

        "account_name":
            account.account_name,

        "account_number":
            account.account_number,

        "transaction":
            transaction_type,

        "amount":
            amount,

        "balance_after":
            balance_after,

        "status":
            "SUCCESS"
    }


    return receipt


def format_receipt(
    receipt
):

    return f"""
================================
          ✪ YAP BANK
        E-RECEIPT
================================

Account Name:
{receipt["account_name"]}

Account Number:
{receipt["account_number"]}

Transaction:
{receipt["transaction"]}

Amount:
₱{receipt["amount"]:,.2f}

Balance After:
₱{receipt["balance_after"]:,.2f}

Status:
{receipt["status"]}

================================
       Thank you for banking
          with YAP Bank!
================================
"""