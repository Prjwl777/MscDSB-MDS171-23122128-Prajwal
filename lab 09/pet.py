from petstore import PetStore

def main():
    # Create a PetStore instance.
    pet_store = PetStore()

    while True:
        print("\nPet Store Menu:")
        print("1. Admin Menu")
        print("2. View Pets")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Go to the admin menu.
            admin_menu(pet_store)
        elif choice == "2":
            # View available pets.
            view_pets(pet_store)
        elif choice == "3":
            # Exit the program.
            print("Exiting the Pet Store program. Goodbye!")
            break
        else:
            # Handle invalid input.
            print("Invalid choice. Please try again.")

def admin_menu(pet_store):
    while True:
        print("\nAdmin Menu:")
        print("1. Add a pet")
        print("2. Sell a pet")
        print("3. List all pets")
        print("4. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Add a new pet to the store.
            add_pet(pet_store)
        elif choice == "2":
            # Sell a pet from the store.
            sell_pet(pet_store)
        elif choice == "3":
            # List all pets in the store.
            list_all_pets(pet_store)
        elif choice == "4":
            # Return to the main menu.
            break
        else:
            # Handle invalid input.
            print("Invalid choice. Please try again.")

def add_pet(pet_store):
    print("\nAdd a Pet:")
    pet_type = input("Enter the type of pet (e.g., dogs, cats, rabbits, parrots): ")
    breed = input("Enter the breed: ")
    age = input("Enter the age: ")

    # Add the pet to the store.
    pet_store.collectPet(pet_type, breed, age)

def sell_pet(pet_store):
    print("\nSell a Pet:")
    pet_type = input("Enter the type of pet to sell (e.g., dogs, cats, rabbits, parrots): ")
    
    # Sell a pet from the store.
    pet_store.sellPet(pet_type)

def list_all_pets(pet_store):
    print("\nList of All Pets:")
    # List all pets in the store.
    pet_store.listAllPets()

def view_pets(pet_store):
    print("\nView Pets Menu:")
    breed = input("Enter the breed you want to search for: ")
    
    # Search for and view pets of a specific breed.
    pet_store.searchPets(breed)

if __name__ == "__main__":
    main()
