print("Amount Due: 50")

amount_due = 50
coins_added = 0

while True:
    coin_inputted = int(input("Insert Coin: "))
    if coin_inputted in [25, 10, 5]:
        amount_due -= coin_inputted
        coins_added += coin_inputted

    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
        break
    else:
        print(f"Amount Due: {amount_due}")