#Write a function that gets an array of strings as parameter and returns a new
#array containing all the values from the provided array in the same order but without any duplicated values.
#If the string ‘pete’ is a value inside the array your function should skip it and
#not copy it to the new array. In your solution use only while loops.

def remove_duplicates_and_pete(names):
    unique = []
    i = 0
    while i < len(names):
        name = names[i]
        if name == "Pete":
            i += 1
            continue

        j = 0
        found = False
        while j < len(unique):
            if unique[j] == name:
                found = True
                break
            j += 1

        if not found:
            unique.append(name)

        i += 1
    return unique



names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(remove_duplicates_and_pete(names))
