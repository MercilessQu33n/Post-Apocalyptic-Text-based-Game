# Function to show the game instructions and commands
def show_instructions():
    print("Post-Apocalyptic Survival Text Game")
    print("Collect all the critical items to escape the house and survive.")
    print("Move commands: go North, go South, go East, go West")
    print("To pick up an item: take 'item name'")
    print("Defeat 'The Ravager' and escape using the bolt cutters to win the game.")


# Function to show the player's current status
def show_status(current_room, inventory, rooms):
    print("\n--------------------")
    print(f"You are currently in the {current_room}.")

    # Show the current item in the room
    if "item" in rooms[current_room]:
        if rooms[current_room]["item"] == "The Ravager!":
            print(f"You see {rooms[current_room]['item']} here.")
        else:
            print(f"You see a {rooms[current_room]['item']} here.")
    else:
        print("There is nothing useful here.")

    # Show the player's current inventory
    print(f"Inventory: {', '.join(inventory) if inventory else 'empty'}")
    print("--------------------\n")


# Main game function with gameplay loop
def main():
    # Set the player's starting room
    current_room = 'Office/Study'

    # Initialize the player's inventory as empty
    inventory = []

    # Number of items required to win
    total_items = 6

    # Define the rooms and their items
    rooms = {
        'Office/Study': {'West': 'Kitchen'},
        'Kitchen': {'South': 'Basement', 'East': 'Office/Study', 'item': 'Canned Food'},
        'Basement': {'North': 'Kitchen', 'South': 'Garage', 'East': 'Utility Room', 'West': 'Living Room',
                     'item': 'Gas Mask'},
        'Utility Room': {'North': 'Bedroom', 'West': 'Basement', 'item': 'Flashlight'},
        'Bedroom': {'South': 'Utility Room', 'item': 'Handgun'},
        'Garage': {'North': 'Basement', 'East': 'Attic', 'item': 'Bolt Cutters'},
        'Attic': {'West': 'Garage', 'item': 'Radio'},
        'Living Room': {'East': 'Basement', 'item': 'The Ravager!'}  # villain
    }

    # Show the instructions at the beginning of the game
    show_instructions()

    # Start of the gameplay loop
    while True:
        # Show the player's current status
        show_status(current_room, inventory, rooms)

        # Get player input for their next action (move or take item)
        command = input("Enter your move: ").strip().lower()

        # Process movement commands (e.g., 'go North')
        if command.startswith("go"):
            direction = command.split()[1].capitalize()  # Extract the direction (north, south, etc.) and capitalize it

            # Check if the direction is valid for the current room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]  # Move to the new room
                print(f"You move {direction} to the {current_room}.")

                # Check if the player entered the Living Room
                if current_room == 'Living Room':
                    # Win condition: if the player has all 6 items
                    if len(inventory) == total_items:
                        print("Congratulations! You have collected all items and defeated The Ravager!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                    else:
                        # Lose condition: if the player enters without collecting all items
                        print("You've been overpowered by The Ravager... GAME OVER!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                    break  # End the game after entering the Living Room

            else:
                print("You can't go that way. Try a different direction.")

        # Process item pickup commands (e.g., 'take canned food')
        elif command.startswith("take"):
            # Extract the full item name from the command after 'take'
            item_name = ' '.join(command.split()[1:]).lower()  # Get everything after 'take'

            # Check if the item in the room matches the command
            item_in_room = rooms[current_room].get("item", "").lower()  # Make item lowercase to compare
            if item_in_room == item_name:
                print(f"You take the {rooms[current_room]['item']}.")
                inventory.append(rooms[current_room]['item'])  # Add the item to the inventory
                del rooms[current_room]["item"]  # Remove the item from the room
            else:
                print("There's no such item here to take.")

        # Invalid command handling
        else:
            print("Invalid command. Try 'go [direction]' or 'take [item]'.")


# Call the main function to start the game
if __name__ == "__main__":
    main()
