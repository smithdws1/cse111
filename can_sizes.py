import math

# List with can data
can_sizes = [
    ("#1 Picnic", 6.83, 10.16, 0.28),
    ("#1 Tall", 7.78, 11.91, 0.43),
    ("#2", 8.73, 11.59, 0.45),
    ("#2.5", 10.32, 11.91, 0.61),
    ("#3 Cylinder", 10.79, 17.78, 0.86),
    ("#5", 13.02, 14.29, 0.83),
    ("#6Z", 5.40, 8.89, 0.22),
    ("#8Z short", 6.83, 7.62, 0.26),
    ("#10", 15.72, 17.78, 1.53),
    ("#211", 6.83, 12.38, 0.34),
    ("#300", 7.62, 11.27, 0.38),
    ("#303", 8.10, 11.11, 0.42)
]

# Functions
def calculate_volume(radius, height):
    return math.pi * (radius ** 2) * height

def calculate_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def calculate_storage_efficiency(volume, surface_area):
    return volume / surface_area

def calculate_cost_efficiency(volume, cost):
    return volume / cost

# Main
def main():
    max_storage_efficiency = 0
    max_cost_efficiency = 0
    best_storage_can = ""
    best_cost_can = ""

    for name, radius, height, cost in can_sizes:
        volume = calculate_volume(radius, height)
        surface_area = calculate_surface_area(radius, height)
        storage_efficiency = calculate_storage_efficiency(volume, surface_area)
        cost_efficiency = calculate_cost_efficiency(volume, cost)

        print(f"{name}: Volume = {volume} cubic cm's, Surface Area = {surface_area} square cm's, "
              f"Storage Efficiency = {storage_efficiency:.2f}, Cost Efficiency = {cost_efficiency:.0f}")

        if storage_efficiency > max_storage_efficiency:
            max_storage_efficiency = storage_efficiency
            best_storage_can = name

        if cost_efficiency > max_cost_efficiency:
            max_cost_efficiency = cost_efficiency
            best_cost_can = name

    print(f"\nThe can with the highest storage efficiency is {best_storage_can}.")
    print(f"The can with the highest cost efficiency is {best_cost_can}.")

if __name__ == "__main__":
    main()
