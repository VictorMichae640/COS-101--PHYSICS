
def speed():
    distance = float(input("Enter distance in metres: "))
    time = float(input("Enter time in seconds: "))
    result = distance / time
    print("Speed =", result, "m/s")


def force():
    mass = float(input("Enter mass in kg: "))
    acceleration = float(input("Enter acceleration: "))
    result = mass * acceleration
    print("Force =", result, "N")


def kinetic_energy():
    mass = float(input("Enter mass in kg: "))
    velocity = float(input("Enter velocity: "))
    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "J")


def potential_energy():
    mass = float(input("Enter mass in kg: "))
    height = float(input("Enter height in metres: "))
    result = mass * 9.8 * height
    print("Potential Energy =", result, "J")


def density():
    mass = float(input("Enter mass in kg: "))
    volume = float(input("Enter volume in cubic metres: "))
    result = mass / volume
    print("Density =", result, "kg/m3")


while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Kinetic Energy")
    print("4. Potential Energy")
    print("5. Density")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        kinetic_energy()
    elif choice == "4":
        potential_energy()
    elif choice == "5":
        density()
    else:
        print("Invalid choice. Please select 1-5.")

    again = input("Would you like to continue? (yes/no): ")

    if again.lower() == "no":
        print("Thank you for using the Physics Calculator!")
        break
