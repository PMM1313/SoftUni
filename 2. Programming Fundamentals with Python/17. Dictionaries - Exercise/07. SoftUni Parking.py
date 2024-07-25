n = int(input())
parking_lot = {}

for _ in range(n):
    command = input().split()

    action = command[0]
    username = command[1]

    if action == "register":
        license_plate_number = command[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")
