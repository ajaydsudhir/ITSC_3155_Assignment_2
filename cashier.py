# cashier.py
class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        large_dollars = int(input("How many large dollars? : "))
        half_dollars = int(input("How many half dollars?  : "))
        quarters = int(input("How many quarters?      : "))
        nickels = int(input("How many nickels?       : "))
        total = float(large_dollars + (half_dollars / 2) + (quarters / 4) + (nickels / 20))
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if (coins >= cost):
            return True
        else:
            return False