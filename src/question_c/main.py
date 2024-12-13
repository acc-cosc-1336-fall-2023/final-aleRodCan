#add import
from question_c import Stock, get_stock_list

def main():
    while True:
        print("\nMenu:")
        print("1 - Display Stock List")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_list = get_stock_list()
            if stock_list:
                print("\nStock Purchase History:")
                print(f"{'Symbol':<10}{'Company Name'}")
                print("-" * 30)
                for stock in stock_list:
                    print(f"{stock.get_symbol():<10}{stock.get_company_name()}")
            else:
                print("No stocks available to display.")
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

    if __name__ == "__main__":
        main()