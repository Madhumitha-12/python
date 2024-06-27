n=int(input("enter the number of parking slot:"))
parking_slots = [None] * n

def park_vehicle():
    slot = int(input("Enter parking slot (1-n): "))
    if parking_slots[slot-1] is None:
        vehicle_number = input("Enter vehicle number: ")
        parking_slots[slot-1] = vehicle_number
        print("Vehicle parked successfully!")
    else:
        print("Slot not available. Please select a different slot.")

def exit_vehicle():
    vehicle_number = input("Enter vehicle number to exit: ")
    if vehicle_number in parking_slots:
        slot = parking_slots.index(vehicle_number) + 1
        parking_slots[slot-1] = None
        print(f"Vehicle exited from slot {slot}.")
    else:
        print("Vehicle not found in the parking.")

while True:
    choice = input("Do you want to park or exit? (park/exit): ")
    if choice.lower() == "park":
        park_vehicle()
    elif choice.lower() == "exit":
        exit_vehicle()
    else:
        print("Invalid choice. Please enter 'park' or 'exit'.")
