# Write a function that gets an array of strings as parameter and returns a new array containing
# all the values that appear more than once. In your solution
#use only while loops.


def find_duplicates(strings):
    counts = {}
    i = 0
    while i < len(strings):
        string = strings[i]
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
        i += 1


    duplicates = []
    keys = list(counts.keys())
    i = 0

    while i < len(keys):
        if counts[keys[i]] > 1:
            duplicates.append(keys[i])
        i += 1

    return duplicates


if __name__ == '__main__':
    array = ["Apple", "Banana", "Orange", "Peach", "Apple", "Grape", "Grape"]
    print(find_duplicates(array))