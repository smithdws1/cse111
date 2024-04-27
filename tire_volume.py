import math
import datetime

# Get the Tire Dimensions
tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = int(input("Enter the diameter of the tire in inches (ex 15): "))

# Calculate the tire volume
volume_liters = (math.pi * tire_width**2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * tire_diameter)) / 10000000000
print(f"\nThe approximate volume is {volume_liters:.2f} liters")

# Ask if they want to buy tires
buy_tires = input("Do you want to buy tires with the dimensions you entered? (yes/no): ").strip().lower()

# Get the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Open a text file called volumes.txt for appending
with open("volumes.txt", "a") as file:
    data_to_write = f"{current_date}, {tire_width}, {aspect_ratio}, {tire_diameter}, {volume_liters:.2f}"
    if buy_tires == "yes":
        phone_number = input("Please enter your phone number: ")
        data_to_write += f", {phone_number}"
    data_to_write += "\n"
    file.write(data_to_write)

print("Data has been recorded to volumes.txt")
