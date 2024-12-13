#write functions here, don't add input('') statements here!

def create_multiplication_table():
    """
    Creates a multiplication table and returns it as a list of lists.
    """
    table = []
    for i in range(1,6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    """
    Display the multiplication table.
    """
    print("\nMultiplication Table:")
    for row in table:
        print(" ".join(f"{value:3}" for value in row ))