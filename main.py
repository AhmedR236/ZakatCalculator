from calculator import get_nisab, calculateZakat, get_user_inputs, display_results

def main():
    
    nisab = get_nisab()
    print(f"Nisab threshold (current): {nisab:.2f}")

    cash, gold, silver, investments, liabilities = get_user_inputs()

    assets, zakat_wealth, zakat = calculateZakat(cash, gold, silver, investments, liabilities, nisab)

    display_results(assets, zakat_wealth, zakat)

if __name__ == "__main__":
    main()
