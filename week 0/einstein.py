def main():
    # Prompt the user for mass
    mass = int(input("Enter mass (in kilograms): "))

    # Calculate the equivalent number of Joules
    c = 300000000  # Speed of light in m/s
    energy = mass * c**2

    # Print the result
    print(energy)

main()
