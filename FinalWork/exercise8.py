#1- Write a function that prints all the student data (each student property should be printed in a new line).
#2- Write a function that receives the student object and a hobby, the function
#should add the hobby to the student's hobbies array if it’s not exist already.
# 3- Use the function that you wrote in ex 1 to print the data of the student and
# check that the new hobby has been added.
# 4- Write a function that receives an object of a student and hobby, the
# function should delete the hobby from the student's hobbies.
# 5- Use the function that you wrote in ex 1 to print the data student and check
# that the hobby has been deleted from the object student.
# 6- Add to the object student new property: family_name and add a value.



def print_all_property_of_student(student):
    for i in student:
        for key, value in student.items():
            print(f"{key}: {value}")
        return

def add_hobbies(student,hobby):

    student.setdefault("hobbies",[])
    if hobby not in student["hobbies"]:
        student["hobbies"].append(hobby)
        print(f"Hobby {hobby} added into the list of hobbies")
    else:
        print(f"Hobby {hobby}, already exists")

def delete_hobby_in_hobbies(student,hobby):
    if hobby in student.get("hobbies", []):
        student["hobbies"].remove(hobby)


student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}

print_all_property_of_student(student)
print()
add_hobbies(student,"basketball")
add_hobbies(student,"basketball")
print()
print_all_property_of_student(student)
print()
student["Famaly_name"] = "Travonta"
print_all_property_of_student(student)
print()
delete_hobby_in_hobbies(student,"basketball")
print_all_property_of_student(student)
print()
print(f"After removing a hobby basketball: {student}")