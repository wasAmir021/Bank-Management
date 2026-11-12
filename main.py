# Bank
def show_balance(balance):
    print(balance)


def deposit(balance):
    amount = int(input("enter the amount : "))
    while True:
        if amount > 0:
            break
        else:
            amount = int(input("enter positive number : "))
    balance = balance+amount
    return balance


def withdraw(balance):
    bardasht = int(input("enter your bardasht : "))
    while True:
        if bardasht > 0 and bardasht <= balance:
            balance = balance-bardasht
            break
        elif bardasht <= 0:
            bardasht = int(input("enter positive : "))
        elif bardasht > balance:
            bardasht = int(input("enter bardasht<balance : "))
    return balance


def main():
    balance = 1000
    while True:
        print("**********Menu************")
        print("1.mojodi\n2.variz\n3.bardasht\n4.exit")
        choice = input("enter your choice : ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance = deposit(balance)
            print(balance)

        elif choice == "3":
            balance = withdraw(balance)
            print(balance)

        else:
            print("sickkkktirrrr")
        ques = input("Do you want to continue? (yes/no) ")
        if ques == "no":
            break


main()
