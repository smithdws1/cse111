# provinces.py

def main():
    with open('provinces.txt', 'r') as file:
        # Read the contents of the file into a list
        provinces = file.read().splitlines()

    # Print the entire list
    print(provinces)

    # Remove the first element from the list
    if provinces:
        provinces.pop(0)

    # Remove the last element from the list
    if provinces:
        provinces.pop(-1)

    # Replace all occurrences of "AB" in the list with "Alberta"
    provinces = ["Alberta" if province == "AB" else province for province in provinces]

    # Count the number of elements that are "Alberta"
    alberta_count = provinces.count("Alberta")

    # # Print the modified list
    # print("\nModified list:")
    print(provinces)

    # Print the number of times "Alberta" appears in the list
    print("\nNumber of times 'Alberta' appears in the list:", alberta_count)

if __name__ == "__main__":
    main()
