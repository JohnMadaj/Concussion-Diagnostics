import math


def calculate_impact_velocity(mass, length, angle_degrees):
    g = 9.81  # Acceleration due to gravity in m/s^2
    angle_radians = math.radians(angle_degrees)
    height = length * (1 - math.cos(angle_radians))
    impact_velocity = math.sqrt(2 * g * height)
    return impact_velocity


def estimate_impact_force(mass, impact_velocity, impact_duration):
    force = mass * impact_velocity / impact_duration
    return force


def force_to_g_force(force, mass):
    g = 9.81  # Acceleration due to gravity in m/s^2
    g_force = force / (mass * g)
    return g_force


if __name__ == '__main__':
    mass = 10  # Mass of the hammer part in pounds
    mass_kg = mass * 0.453592  # Convert mass to kilograms
    length = 34  # Length of the sledgehammer in inches
    length_m = length * 0.0254  # Convert length to meters

    while True:
        angle_degrees = float(input("Enter the angle in degrees (0 to 90): "))
        impact_duration_ms = float(input("Enter the estimated impact duration in milliseconds (enter value between 2-6): "))
        impact_duration_s = impact_duration_ms / 1000  # Convert impact duration to seconds

        if 0 <= angle_degrees <= 90:
            impact_velocity = calculate_impact_velocity(mass_kg, length_m, angle_degrees)
            impact_force = estimate_impact_force(mass_kg, impact_velocity, impact_duration_s)
            g_force = force_to_g_force(impact_force, mass_kg)
            print(f"Angle: {angle_degrees}°, Impact Force: {impact_force:.2f} N, G-Force: {g_force:.2f} g")
        else:
            print("Invalid angle. Please enter an angle between 0 and 90 degrees.")

        user_input = input("Enter 'q' to quit or any other key to enter another angle: ")
        if user_input.lower() == 'q':
            break
