# Write a function that receives an array of objects.
 #Each object should represent a student with the properties:
 #● id
 #● first name
 #● last name
 #● age
 #● country
 #In addition, the function should receive a property to change.\
#1- The function should check for each property in each object in the array if
# the given property exists and if it does, the function should delete it from the object.
# 2- Write a function that prints each property of each object in the given array.
#3- Write a function that sorts the array by the students age from the oldest to
# the youngest and return the sorted array.

def update_students_value(students,property,new_value):
    for student in students:
        if property in student:
            student[property] = new_value
        else:
            print(f"Property {property} not found, try again")

#
def delete_property_from_students(students, property_name):
     for student in students:
        if property_name in student:
            del student[property_name]

def print_students_properties(students):
     for student in students:
      print(students)
      for key,value in student.items():
       print(f"{key}: {value}")
       return
def sorted_students_by_age(students):

    return sorted(students, key=lambda student: ["age"],reverse=True)

if __name__ == '__main__':


    students = [
    {"id": 1, "name": "Ivan", "second name": "Hristoforov", "age": 23, "country": "Israel", "city": "Ramat Gan"},
    {"id": 2, "name": "Yoav", "second name": "Avi", "age": 21, "country": "Israel", "city": "Gyvataim"},
    {"id": 3, "name": "Beni", "second name": "Zbeta", "age": 25, "country": "Israel", "city": "Rishon Lezion"},
]
print(students)
print()
update_students_value(students,"country"," USA ")
print(f"After update a property country: {students}")
print()
delete_property_from_students(students,"country")
print(f"After removing a property country: {students}")
print()
print("Property of each student")
print_students_properties(students)
print()
sorted_students = sorted_students_by_age(students)
print("After sorted list of student by age ")
print_students_properties(sorted_students)
