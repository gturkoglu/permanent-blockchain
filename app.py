from arweave import Transaction, Wallet

wallet = Wallet("wallet.json")

with open('index.html', 'r') as mypdf:
    pdf_string_data = mypdf.read()
    transaction = Transaction(wallet, data=pdf_string_data)
    transaction.sign()
    transaction.send()
