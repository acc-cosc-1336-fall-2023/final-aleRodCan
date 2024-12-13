#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history_history(stock_dict):
    print("\nStock Purchase History:")
    print(f"{'Symbol':<10}{'Company Name':<20}")
    print("_" * 30)
    for symbol, company_name in stock_dict.items():
        print(f"{symbol:,10}{company_name:,20}")
