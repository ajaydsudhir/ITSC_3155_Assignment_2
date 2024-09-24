import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Load the resources and recipes from data.py
resources = data.resources
recipes = data.recipes

# Create instances of SandwichMaker and Cashier
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    on = True
    while on:
        # User input not case-sensitive
        option = input("What would you like? (small/medium/large/off/report): ").lower()

        # Case of breaking from loop and terminating program
        if option == "off":
            on = False

        # Case to display all available resources in sandwich maker to user
        elif option == "report":
            print("\nBread  : ", resources["bread"], "slice(s)")
            print("Ham    : ", resources["ham"], "slice(s)")
            print("Cheese : ", resources["cheese"], "ounce(s)\n")

        # Make sandwich based on user request
        elif option in recipes:
            # Check if resources are available
            if sandwich_maker_instance.check_resources(recipes[option]["ingredients"]):
                print("\nPlease insert coins.")
                # Calculate user payment
                coins = float(cashier_instance.process_coins())
                # Check user payment
                if cashier_instance.transaction_result(coins, recipes[option]["cost"]):
                    # Display change returned to user
                    print("\nHere is ${:.2f} in change.\n".format(coins - recipes[option]["cost"]))
                    # Making sandwich
                    sandwich_maker_instance.make_sandwich(option, recipes)
                    # Display that the sandwich is provided to the user
                    print("{} sandwich is ready. Bon appetit!\n".format(option.upper()))
                else:
                    # If money is insufficient display message
                    print("\nSorry that's not enough money. Money refunded.\n")

        # Wrong input verification
        else:
            print("\nCheck your entered option.\n")

if __name__ == "__main__":
    main()