# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using lists, dictionaries, and JSON files to work with data
# Change Log: (Who, When, What)
#   TYoung,11/19/2024,Created Script
#   
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
json_data: str = ''
file = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# Read existing data from file
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"Note: {FILE_NAME} not found. Starting with an empty list.")
except json.JSONDecodeError:
    print(f"Error: {FILE_NAME} is not a valid JSON file. Starting with an empty list.")

# Present and Process the data
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.strip():
                raise ValueError("First name cannot be empty.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.strip():
                raise ValueError("Last name cannot be empty.")

            course_name = input("Please enter the name of the course: ")
            if not course_name.strip():
                raise ValueError("Course name cannot be empty.")

            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(f"Error: {str(e)}")

    elif menu_choice == "2":
        print("\nCurrent Registrations:")
        for student in students:
            print(f"{student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")

    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=4)
            print(f"\nData has been saved to {FILE_NAME}")
            print("Saved data:")
            for student in students:
                print(f"{student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except IOError:
            print(f"Error: Unable to write to {FILE_NAME}")

    elif menu_choice == "4":
        print("\nThank you for using the Course Registration Program!")
        break

    else:
        print("\nPlease only choose option 1, 2, 3, or 4")

print("Program Ended")
