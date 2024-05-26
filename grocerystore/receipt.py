# I added a request for a survey at the end of the receipt. 

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return dictionary

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        
        request_dict = {}
        with open('request.csv', mode='r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                
                if product_number in request_dict:
                    request_dict[product_number] += quantity
                else:
                    request_dict[product_number] = quantity
        
        print("Welcome to David Emporium!")
        print("---------------------------------\n")
        
        subtotal = 0.0
        total_items = 0
        print("\nCustomer Receipt:")
        for product_number, quantity in request_dict.items():
            if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = float(product_info[2])
                item_total = product_price * quantity
                subtotal += item_total
                total_items += quantity
                
                print(f"{product_name}: {quantity} @ ${product_price:.2f} each = ${item_total:.2f}")
            else:
                print(f"Product number {product_number} not found in products.csv")
        
        sales_tax = subtotal * 0.0625
        total = subtotal + sales_tax

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        
        print("\nThank you for shopping with us!")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A %I:%M %p}")
        
        print("\nWe value your feedback!")
        print("Please complete our online survey at:")
        print("www.trackmyeverypurchase.com/survey")
    
    except FileNotFoundError:
        print("Error: The request.csv file was not found.")
    except PermissionError:
        print("Error: Permission denied for the request.csv file.")
    except KeyError as e:
        print(f"Error: Missing key {e} in the products dictionary.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
