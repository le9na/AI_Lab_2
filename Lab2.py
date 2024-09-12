# This is my implementation of a smart hoover that can use four directions to move in rooms
# 1. Class room creates an object for room with two attributes: condition & 
# 2. Generating rooms method: generate a room with random condition and random side
# 3. Cleaning process where the method decides where next side is and whether it should clean or not

import random

# Define the Room class
class Room:
    def __init__(self, condition, side):
        self.condition = condition
        self.side = side


# Method to generate random rooms
def generate_rooms(num):
    rooms = []
    for k in range(num):
        condition = random.choice(["Clean", "Dirty"])
        side = random.choice(["Left", "Right", "Up", "Down"])
        room = Room(condition, side)
        rooms.append(room)
    return rooms

def cleaning_process(rooms):
    for i, room in enumerate(rooms):
        print(f"Hoover is in Room {i+1} | {room.condition}, {room.side}")

        # If the room is dirty, clean it
        if room.condition == "Dirty":
            print("Room is dirty. Cleaning the room...")
            room.condition = "Clean"
        
        # Move logic based on the side
        if room.side == "Left":
            next_direction = "right"
        elif room.side == "Right":
            next_direction = "left"
        elif room.side == "Up":
            next_direction = "down"
        elif room.side == "Down":
            next_direction = "up"
        
        print(f"Room is clean. Going {next_direction}.")
        
        print('------------------------------------------')  

# to get user input:
# i = int(input("number of rooms: "))
i = 5
rooms = generate_rooms(i)

# Print rooms before the process
for room in rooms:
    print(f'Room 1, Condition: {room.condition}, Side: {room.side}')
print()
print('------------------------------------------')  

# Start the hoover
cleaning_process(rooms)

# Output the final state of rooms
print("\nFinal state of rooms:")
for room in rooms:
    print(f'Room 1, Condition: {room.condition}, Side: {room.side}')
print('------------------------------------------')