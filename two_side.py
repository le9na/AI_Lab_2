# On two sides

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

# Smart hoover logic
def smart_hoover(rooms):
    for i, room in enumerate(rooms):
        print(f"Hoover is in Room {i+1} | {room}")

        # If the room is dirty, clean it
        if room.condition == "Dirty":
            print("Room is dirty. Cleaning the room...")
            room.condition = "Clean"
        
        # Move logic based on the side
        if room.side == "Left":
            next_direction = "right"
        else:
            next_direction = "left"
        
        print(f"Room is clean. Moving {next_direction}.")
        
        print('-' * 30)  # Separator for clarity

# Example usage
num_rooms = int(input("Enter the number of rooms to generate: "))
generated_rooms = generate_rooms(num_rooms)

# Start the hoover
smart_hoover(generated_rooms)

# Output the final state of rooms
print("\nFinal state of rooms:")
for room in generated_rooms:
    print(room)
