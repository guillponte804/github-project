import math

def calculate_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

radius = 3.5  # Example value
height = 4.0  # Example value
volume = calculate_volume(radius, height)
print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume}")
