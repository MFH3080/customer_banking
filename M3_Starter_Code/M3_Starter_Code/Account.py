""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance
        return self.balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest
        return self.interest
    
    def get_balance(self):
        """Gets the balance of the account"""
        return self.balance
    
    def get_interest(self):
        """Gets the interest of the account"""
        return self.interest
