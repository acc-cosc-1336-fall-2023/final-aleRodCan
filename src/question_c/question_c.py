#write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name):

        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__company_name

def get_stock_list():
    """
    Create a list of Stock objects and returns it.
    Reads data from a file names 'stock_file.dat'.
    """
    stock_list = []
    try:
        with open("stock_file.dat", "r") as file:
            for line in file:

                symbol, company_name = line.strip().split(" ", 1)
                stock_list.append(Stock(symbol, company_name))
    except FileNotFoundError:
        print("Error: 'stock_file.dat' not found.")
    return stock_list