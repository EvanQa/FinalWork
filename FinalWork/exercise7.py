#1 - Write a function that receives the array shown above and prints only animalType: cat.
#2 - Write a function that receives the array shown above and the animal type. The function
#should print all names of that animal type if this type exists in the object.
#3- Write a function that that receives the array shown above and animal name
# The function should add the specified animal name to each ‘names’ array in
# each animal_type if that name does not exist in the ‘names’ array.



def recive_list_from_dictionary(array):
   for item in array:
       if item.get("animal_type") == "cat":
           print(item)


def print_animal_names(array,animal_type):
    for item in array:
        if item.get("animal_type") == animal_type and item.get("names"):
            item.get("names")
        return
    else:
        print(f"Not found this type of {animal_type}, animal")


if __name__ == '__main__':

    our_pets = [
    {
    "animal_type": "cat",
    "names": [
    "Meowzer",
    "Fluffy",
    "Kit-Cat"
    ]
    },
    {
    "animal_type": "dog",
    "names": [
    "Spot",
    "Bowser",
    "Frankie"
 ]
    }
]

recive_list_from_dictionary(our_pets)
print_animal_names(our_pets,"cat")
print_animal_names(our_pets,"dog")
print(our_pets)
