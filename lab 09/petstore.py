class PetStore:
    def __init__(self):
        # Initialize a dictionary to store different types of pets.
        self.pets = {
            "dogs": [],
            "cats": [],
            "rabbits": [],
            "parrots": []
        }

    def collectPet(self, type, breed, age):
        # Add a new pet of a specific breed and age to the store.
        pet = {"Breed": breed, "Age": age}
        if type in self.pets:
            self.pets[type].append(pet)
            print(f"Collected a {breed} with age {age}.")

    def searchPets(self, breed):
        if breed in self.pets:
            if self.pets[breed]:
                # List pets of a particular breed if they exist.
                print(f"{breed} found:")
                for pet in self.pets[breed]:
                    print(f"Breed: {pet['Breed']}, Age: {pet['Age']}")
            else:
                # Report that there are no pets of that breed.
                print(f"No {breed} pets found in the store.")
        else:
            # Indicate that the store doesn't sell pets of that breed.
            print(f"We do not sell {breed} pets in this store.")

    def sellPet(self, breed):
        if breed in self.pets:
            if self.pets[breed]:
                # Sell the first available pet of a particular breed.
                self.pets[breed].remove(self.pets[breed][0])
                print(f"Sold a {breed}.")
            else:
                # Inform that there are no pets of that breed to sell.
                print(f"No {breed} pets available to sell.")
        else:
            # Mention that the store doesn't sell pets of that breed.
            print(f"We do not sell {breed} pets in this store.")

    def listAllPets(self):
        # Display a list of all pets in the store.
        for breed, pets_list in self.pets.items():
            for pet in pets_list:
                print(f"Type: {breed}, Breed: {pet['Breed']}, Age: {pet['Age']}")

# Sample usage
store = PetStore()

# Collecting pets
store.collectPet("dogs", "Golden Retriever", 2)
store.collectPet("cats", "Siamese", 1)

# Searching for pets
store.searchPets("dogs")
store.searchPets("rabbits")

# Selling pets
store.sellPet("cats")
store.sellPet("parrots")

# Listing all pets
store.listAllPets()
