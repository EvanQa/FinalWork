#Write a python program that gets user input (use input() function for this).
#The first input will be the user full name
#Second input will be the user age
#Third input will be the user email
#Write validation for each input provided by the user and allow the user to try
#again in case the user provided invalid input.

def validate_name(name):
    name_parts = name.split()
    if len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        return True
    return False


def validate_age(age):
    if age.isdigit():
        age_int = int(age)
        if 1 <= age_int <= 130:
            return True
    return False


def validate_email(email):
   if '@' in email:
       return True
   return False


def get_user_input():
    while True:
        full_name = input("Enter your full name (first and last name): ")
        if validate_name(full_name):
            break
        else:
            print("Invalid input. Please enter exactly two words (first and last name).")


    while True:
        age = input("Enter your age: ")
        if validate_age(age):
            break
        else:
            print("Invalid input. Age must be an integer between 1 and 130. Please try again.")


    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        else:
            print("Invalid input. Please enter a valid email with '@'. Please try again.")

    return full_name, age, email


def main():
    print("Welcome! Please provide the following information:")

    full_name, age, email = get_user_input()

    print("\nThank you for providing your information!")
    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")


if __name__ == "__main__":
    main()
