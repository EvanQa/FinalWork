#Write a function that gets an array of strings as parameter and returns a new
#array containing all the values from the provided array in the same order but
#without any duplicated values. In your solution use only while loops.




def remove_duplicates(strings):
    unique = []
    i = 0
    while i < len(strings):
        string = strings[i]

        j = 0
        found = False
        while j < len(unique):
            if unique[j] == string:
                found = True
                break
            j += 1
        if not found:
            unique.append(string)
        i += 1

    return unique


names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris','Kevin']
print(remove_duplicates(names))
