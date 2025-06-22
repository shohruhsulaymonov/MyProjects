class Account:


    def __init__(self, account_number: int, account_holder_name: str, balance: float):

        self.account_number = account_number
        self.holder_name = account_holder_name.capitalize()
        self.balance = balance


    def __str__(self):

        return f"\n'{self.account_number}' account holder '{self.holder_name}' has ${self.balance}"
    

    def deposit(self, amount):

        self.balance += amount*0.9 # 1% Interest rate
        print(f"\n${amount} has been successfully deposited to {self.account_number}.")


    def withdraw(self, amount):
        if self.balance < amount:
            ans = input('\nThe user has less money in his balance than you want to withdraw. Are you sure you want to carry out the withdrawal? (Y/N): ')
            if ans == 'Y':
                self.balance -= amount
                print(f"\n${amount} has been successfully withdrawn from {self.account_number}.")
                print(f"\nThe user now owes ${self.balance*(-1)} to the Bank")
            elif ans == 'N':
                print('\nThe withdrawal was cancelled')
                return
            
            else:
                print("\nPlease, enter either 'Y' or 'N'")
                return
        else:
            self.balance -= amount
            print(f"\n${amount} has been successfully withdrawn from {self.account_number}.")
        


    def check_balance(self):
        return self.balance



class Bank:


    dict_of_accounts = dict()

    def __init__(self):
        pass


    def add_account(self, new_account: Account):
        if new_account.account_number not in self.dict_of_accounts.keys():
            self.dict_of_accounts[new_account.account_number] = new_account
            print(f"\nAccount {new_account.account_number} added.")
        else:
            print("T\nhere's already a user with this number. Please choose another one")

    
    def get_account(self, account_number):
        return self.dict_of_accounts.get(account_number)

    def list_all(self):
        for account in self.dict_of_accounts.values():
            print(account)


    def check_balance(self, account_num):
        
        account = self.get_account(account_num)
        if account:
            print(f"\nAccount {account_num} has ${account.check_balance()} in balance.")
        else:
            print(f"\nAccount {account_num} not found.")


    def deposit_money(self, account_num, amount):

        account = self.get_account(account_num)
        if account:
            account.deposit(amount)
        else:
            print(f"\nAccount {account_num} not found.")
            

    def withdraw_money(self, account_num, amount):

        account = self.get_account(account_num)
        if account:
            account.withdraw(amount)
        else:
            print(f"\nAccount{account_num} not found.")

    
    def transfer(self, from_account, to_account, amount):
        sender = self.get_account(from_account)
        receiver = self.get_account(to_account)
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
        else:
            ans = input(f"\nThe sender has less money in his balance than you want to withdraw. Are you sure you want to carry out the withdrawal? (Y/N): ")
            if ans == 'Y':
                sender.balance -= amount
                receiver.balance += amount
                print(f"\nThe tansfer was successfully carried out")
                print(f"\nThe sender now owes ${sender.balance*(-1)} to the Bank")


            elif ans == 'N':
                print('\nThe withdrawal was cancelled')
                return
        
            else:
                print("\nPlease, enter either 'Y' or 'N'")
                return


    def account_details(self, account_number):
        account = self.get_account(account_number)
        print(account)

def print_menu():
    print('\n1. Add an account.')
    print('2. Check balance.')
    print('3. Deposit money.')
    print('4. Withdraw money.')
    print('5. List all account holders.')
    print('6. Transfer money.')
    print('7. See account details.')
    print('8. Exit.')


def main():

    acc = Account(1, 'Shohruh', 1000)
    bnk = Bank()
    bnk.add_account(acc)

    while True:
        
        print_menu()
        choice = input('\nPlease, enter your option (1-8): ')

        if choice == '1':
            
            try:
                id = int(input("\nPlease, enter the account number: "))
                if bnk.get_account(id):
                    print(f'\nThere is already an account with this number. Please, choose another one')
                    continue
                user = input("\nPlease, enter the name of the user: ")
                balance = float(input("\nPlease, enter the balance: "))
                new_account = Account(id, user, balance)
                bnk.add_account(new_account)
            except ValueError:
                print('\nInvalid input. Please enter valid values')
                continue

        elif choice == '2':
            try:
                number = int(input("\nPlease, enter the account number you want to see the balance of: "))
                bnk.check_balance(number)
            except ValueError:
                print('\nPlease, enter a positive integer')

        elif choice == '3':
            try:
                number = int(input("\nPlease, enter the account number you want to deposit money to: "))
                if not bnk.get_account(number):
                    print(f'\nAccount {number} not found')
                    continue
                amount = float(input('\nPlease, enter the amount you want to deposit: '))
                bnk.deposit_money(number, amount)
            except ValueError:
                print('\nPlease, enter valid numbers')

        elif choice == '4':
            try:
                number = int(input("\nPlease, enter the account number you want to withdraw money from: "))
                amount = float(input('\nPlease, enter the amount you want to withdraw: '))
                bnk.withdraw_money(number, amount)
            except ValueError:
                print('\nPlease, enter valid numbers')

        elif choice == '5':
            bnk.list_all()

        elif choice == '6':
            try:
                send = int(input('\nPlease enter the account number of the sender: '))
                if not bnk.get_account(send):
                    print(f'\nAccount {send} not found')
                    continue
                receive = int(input('\nPlease enter the account number of the receiver: '))
                if not bnk.get_account(receive):
                    print(f'\nAccount {receive} not found')
                    continue
                if send == receive:
                    print('\nWhat is the point of transferring money to yourself, bro?')
                    continue
                amount = float(input('\nPlease, enter the amount you want to transfer: '))

                bnk.transfer(send, receive, amount)
            except ValueError:
                print('\nPlease, enter valid values')


        elif choice == '7':
            try:
                acc_num = int(input('\nPlease enter the account number: '))
                if not bnk.get_account(acc_num):
                    print(f'\nAccount {acc_num} not found')
                    continue
                bnk.account_details(acc_num)
            except ValueError:
                print('\nPlease, enter a valid account number')

        elif choice == '8':
            print('\nGoodbye👋\n')
            break

        else:
            print("\nPlease, enter a valid number(1-8)")

    
if __name__ == '__main__':
    main()
