
def main():
    amount = input("Please input a number: ")
    if amount.isdigit():
        amount = int(amount)
        if amount % 2 == 0:
            print(f"{amount} is even.")
        else:
            print(f"{amount} is odd.")
    else:
        print("Please input a number.")

main()