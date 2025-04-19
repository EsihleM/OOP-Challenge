import pet
import time

def loading(action, petName=""):
    """Simulate loading time for pet actions."""
    if action == "teach":
        print(f"Teaching {petName} the new trick", end="")
    else:
        print(f"{petName} is {action}ing", end="")
        for i in range(3):
            print(".", end="")
        time.sleep(1) 
        print("")

def pet_reaction(action):
    """Displays a reaction based on the action performed."""
    reactions = {
        "feed": ["That was tasty!", "Yummy! I feel full!", "Thanks for the meal!"],
        "play": ["That was fun!", "I love playing with you!", "Let's do it again!"],
        "sleep": ["I feel rested!", "Thanks for the nap!", "I feel so refreshed!"]
    }
    print(reactions.get(action, "Thanks!"))

# Main program starts here
print("==============================================")
print("Welcome to the Pet Simulator!")
print("You can create a pet and interact with it.")
print("Let's get started!")
name = input("Please enter the name of your pet: ")

userPet = pet.Pet(name)
print("==============================================")
print(f"🐶 Congratulations! You have created a pet named {userPet.name}.")
time.sleep(2)
print("Now, let's see what you can do with your pet.")
time.sleep(3)

while True:
    print("\n==============================================")
    print("Available options:")
    print("1. 🍖 Feed your pet")
    print("2. ⚽ Play with your pet")
    print("3. ✍️  Teach your pet a trick")
    print("4. 📃 Check your pet's status")
    print("5. 😴 Allow your pet to sleep")
    print("6. 📃 Display all tricks your pet knows")
    print("7. Exit")
    print("==============================================")
    
    try:
        userChoice = int(input("Please choose an option (1-7):"))
        if userChoice < 1 or userChoice > 7:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        print("==============================================")
        time.sleep(2)  # Adding a delay for better readability

    # Processing user choice
    if userChoice == 1:
        loading("feed", userPet.name)
        # Simulate feeding the pet
        userPet.eat()
        pet_reaction("feed")
        userPet.get_status()
    elif userChoice == 2:
        loading("play", userPet.name)
        # Simulate playing with the pet
        userPet.play()
        pet_reaction("play")
        userPet.get_status()
    elif userChoice == 3:
        trick = input("🎃 Please enter the trick you want to teach your pet: ")
        loading("teach", userPet.name)
        # Simulate teaching the pet a trick
        if trick == "":
            print("You didn't enter a trick. Please try again.")
            time.sleep(2)  # Adding a delay for better readability
            continue
        elif len(trick) > 20:
            print("Trick name is too long. Please keep it under 20 characters.")
            time.sleep(2)  # Adding a delay for better readability
            continue
        elif len(trick) < 3:
            print("Trick name is too short. Please provide a name with at least 3 characters.")
            time.sleep(2)  # Adding a delay for better readability
            continue
        elif not trick.isalpha():
            print("Trick name should only contain letters.")
            time.sleep(2)  # Adding a delay for better readability
            continue
        userPet.train(trick)
        userPet.get_status()
    elif userChoice == 4:
        userPet.get_status()
    elif userChoice == 5:
        loading("sleep", userPet.name)
        userPet.sleep()
        pet_reaction("sleep")
        time.sleep(2)
        userPet.get_status()
    elif userChoice == 6:
        userPet.show_tricks()
        time.sleep(2)
    elif userChoice == 7:
        print("Thank you for using the Pet Simulator!")
        break
    else:
        print("Try again.")
        print("==============================================")

# Simulate closing the simulator
print("Closing the Pet simulator", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)

# Simulate closing the simulator
print("Closing the Pet simulator", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)          
