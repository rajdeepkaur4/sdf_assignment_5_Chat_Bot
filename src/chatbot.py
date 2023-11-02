'''
Author: Rajdeep Kaur
'''
#MOCK Data
ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}

VALID_TASKS = ["balance", "deposit", "exit"]


#Required Functions
"""
get_account function will ask user for input of Account number and will validate it
"""
def get_account() -> int:

    while True:
        try:
            account = int(input("Please enter your account number: "))
            if account not in ACCOUNTS:
                print("Account number does not exist. Please try again.")
            else:
                return account
        except ValueError:
            print("Account number must be a whole number.")

"""
get_amount function will prompt user for the transaction amount and validate it
"""
def get_amount() -> float:
    while True:
        try:
            amount = float(input("Enter the transaction amount: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid amount. Amount must be numeric.")


"""
get_balance function will fetch balance of a valid account number
"""
def get_balance(account: int) -> str:
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f'Your current balance for account {account} is ${balance:.2f}.'


"""
make_deposit function will make a valid amount deposit into valid account
"""
def make_deposit(account: int, amount: float) -> str:
    """
    Update the balance of the specified account by adding the value of the amount.
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    ACCOUNTS[account]["balance"] += amount
    return f'You have made a deposit of ${amount:.2f} to account {account}.'


"""
user_Selection will ask user for operation to perform
"""
def user_selection() -> str:
    """
    Prompt the user for their selection and return it if valid.
    """
    while True:
        selection = input("What would you like to do (balance/deposit/exit)? ").strip().lower()
        if selection in VALID_TASKS:
            return selection
        else:
            print("Invalid task. Please choose balance, deposit, or exit.")

#Main Function
def chatbot():
    print("Welcome! I'm the PiXELL River Financial Chatbot! Let's get chatting!")

    while True:
        ## CALL THE user_selection FUNCTION HERE
        ## CAPTURING THE RESULTS IN A VARIABLE CALLED
        ## selection:  
        selection = user_selection()

        if selection == "balance":
            ## CALL THE get_account FUNCTION HERE
            ## CAPTURING THE RESULTS IN A VARIABLE
            ## CALLED account: 
            account = get_account()
            ## CALL THE get_balance FUNCTION HERE
            ## PASSING THE account VARIABLE DEFINED
            ## ABOVE, AND PRINT THE RESULTS: 
            print(get_balance(account))
        elif selection == "deposit":
            account = get_account()
            ## CALL THE get_amount FUNCTION HERE
            ## AND CAPTURE THE RESULTS IN A VARIABLE
            ## CALLED amount: 
            amount = get_amount()
            ## CALL THE make_deposit FUNCTION HERE PASSING THE
            ## VARIABLES account AND amount DEFINED ABOVE AND
            ## PRINT THE RESULTS:
            print(make_deposit(account, amount))
        elif selection == "exit":
            print("Thank you for banking with PiXELL River Financial.")
            break

if __name__ == "__main__":
    chatbot()
