class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        bread = ingredients["bread"] <= self.machine_resources["bread"]
        if (not bread):
            print("Sorry there is not enough bread.")
            return False
        ham = ingredients["ham"] <= self.machine_resources["ham"]
        if (not ham):
            print("Sorry there is not enough ham.")
            return False
        cheese = ingredients["cheese"] <= self.machine_resources["cheese"]
        if (not cheese):
            print("Sorry there is not enough cheese.")
            return False
        if (bread and ham and cheese):
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the machine's resources."""
        self.machine_resources["bread"] -= order_ingredients[sandwich_size]["ingredients"]["bread"]
        self.machine_resources["ham"] -= order_ingredients[sandwich_size]["ingredients"]["ham"]
        self.machine_resources["cheese"] -= order_ingredients[sandwich_size]["ingredients"]["cheese"]