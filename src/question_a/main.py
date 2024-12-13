#add import 
from question_a import Stock, stock_purchase_history

def main():
    #Stock Objects
    stock_aapl = Stock("AAPL", "Apple Inc")
    stock_cat = Stock("CAT", "Caterpillar")
    stock_ek = Stock("EK", "Eastman Kodak")
    stock_goog = Stock("GOOG", "Google")
    stock_msft = Stock("MSFT", "Microsoft")

    #Stock Dictionary
    stocks = {
        stock_aapl.get_symbol(): stock_aapl.get_company_name(),
        stock_cat.get_symbol(): stock_cat.get_company_name(),
        stock_ek.get_symbol(): stock_ek.get_company_name(),
        stock_goog.get_symbol(): stock_goog.get_company_name(),
        stock_msft.get_symbol(): stock_msft.get_company_name(),
    }

    #Program Menu
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_purchase_history(stocks)
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
    if __name__ == "__main__":
        main()
