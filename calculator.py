def get_nisab():
    
    gold_price = 60.0  # Example value in your currency, update as needed
    gold_weight = 87.48  # Nisab weight for gold in grams
    return gold_price * gold_weight


def calculateZakat (cash, gold, silver, investments, liabilities, nisab):
#The parameters are all in floats

    assets = cash + gold + silver + investments
    zakat_wealth = assets - liabilities
   
    zakat = 0
   
    if zakat_wealth >= nisab:
        zakat = zakat_wealth * 0.025
    return assets, zakat_wealth, zakat

def get_user_inputs():
    
    print("Enter your financial details for Zakat calculation:")
   
    cash = float(input("Cash (in your currency): "))
    gold = float(input("Gold value (in your currency): "))
    silver = float(input("Silver value (in your currency): "))
    investments = float(input("Investments (in your currency): "))
    liabilities = float(input("Liabilities (in your currency): "))
   
    return cash, gold, silver, investments, liabilities


def display_results(assets, zakat_wealth, zakat):
    
    print("\nZakat Calculation Results:")
    print(f"Assets: {assets:.2f}")
    print(f"Zakatable Wealth: {zakat_wealth:.2f}")
   
    if zakat > 0:
        print(f"Zakat (2.5%): {zakat:.2f}")
    else:
        print("Zakat is not obligatory.")
