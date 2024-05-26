import csv
import re

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
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            value = row[1 - key_column_index]
            dictionary[key] = value
    return dictionary

def main():
    filename = 'students.csv'
    key_column_index = 0 
    students_dict = read_dictionary(filename, key_column_index)

    inumber = input("Please enter an I-Number: ").strip()
    inumber = re.sub(r'\D', '', inumber) 

    if not inumber.isdigit():
        print("Invalid I-Number")
    elif len(inumber) < 9:
        print("Invalid I-Number: too few digits")
    elif len(inumber) > 9:
        print("Invalid I-Number: too many digits")
    else:
        if inumber in students_dict:
            print(f"Student Name: {students_dict[inumber]}")
        else:
            print("No such student")

if __name__ == "__main__":
    main()