class BankAcc:
    def __init__(self, initial_amount, Acc_name):
        self.balance = initial_amount
        self.name = Acc_name
        print(
            f"\n Account '{self.name}' created \n Balance amount : {self.balance:.2f} $ "
        )

    # def getBalance(self):

