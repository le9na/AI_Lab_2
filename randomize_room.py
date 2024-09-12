import random

# Define the Room class
class Room:
    def __init__(self, condition, side):
        self.condition = condition
        self.side = side

    def __repr__(self):
        return f"Room(condition='{self.condition}', side='{self.side}')"

# Method to generate random rooms
def generate_rooms(num_rooms):
    rooms = []
    for _ in range(num_rooms):
        condition = random.choice(["Clean", "Dirty"])
        side = random.choice(["Left", "Right"])
        room = Room(condition, side)
        rooms.append(room)
    return rooms

# Example usage
num_rooms = int(input("Enter the number of rooms to generate: "))
generated_rooms = generate_rooms(num_rooms)

# Output the generated rooms
for room in generated_rooms:
    print(room)
