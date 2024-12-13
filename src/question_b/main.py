#add import
from question_b import create_multiplication_table, display_multiplication_table

def main():
    while True:
        print("\nMenu:")
        print("1 - Display Multiplication Table")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table = create_multiplication_table()
            display_multiplication_table(table)
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

    if __name__ == "__main__":
        main()