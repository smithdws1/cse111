#   Calculates the height of the water column.
def water_column_height(tower_height, tank_height):

    return tower_height + (3 * tank_height) / 4

#   Calculates the pressure gain from the water height.
def pressure_gain_from_water_height(height):
    density_of_water = 998.2 
    gravity = 9.80665
    # Convert to kilopascals
    pressure = (density_of_water * gravity * height) / 1000
    return pressure

#   Calculates the pressure loss in a pipe due to friction.
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_of_water = 998.2
    pressure_loss = -(friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss
