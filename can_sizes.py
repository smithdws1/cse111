import math

# Define the can sizes data
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

def compute_volume(radius, height):
    """ Compute the volume of a cylinder. """
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    """ Compute the surface area of a cylinder. """
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    """ Compute storage efficiency of a cylinder. """
    return volume / surface_area

def compute_cost_efficiency(volume, cost):
    """ Compute cost efficiency of a can. """
    return volume / cost

def main():
    max_storage_efficiency = 0
    max_cost_efficiency = 0
    best_storage_can = ""
    best_cost_can = ""
    
    for name, radius, height, cost in can_sizes:
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, cost)

        # Output the results
        print(f"{name}: Volume = {volume:.2f} cm^3, Surface Area = {surface_area:.2f} cm^2, Storage Efficiency = {storage_efficiency:.4f}, Cost Efficiency = {cost_efficiency:.4f}")

        # Find the can with the highest storage and cost efficiencies
        if storage_efficiency > max_storage_efficiency:
            max_storage_efficiency = storage_efficiency
            best_storage_can = name
        
        if cost_efficiency > max_cost_efficiency:
            max_cost_efficiency = cost_efficiency
            best_cost_can = name

    # Print the results for the best efficiencies
    print(f"\nThe can with the highest storage efficiency is {best_storage_can}.")
    print(f"The can with the highest cost efficiency is {best_cost_can}.")

if __name__ == "__main__":
    main()
