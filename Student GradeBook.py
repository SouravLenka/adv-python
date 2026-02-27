# Student GradeBook system using functions
# Functions for login, add marks, calculate percentage, and view report card

students = {
    "st101": {"password": "p1", "name": "Sourav", "marks": {"Python": 0, "Java": 0, "C++": 0}},
    "st102": {"password": "p2", "name": "Chiru", "marks": {"Python": 0, "Java": 0, "C++": 0}},
    "st103": {"password": "p3", "name": "Sai", "marks": {"Python": 0, "Java": 0, "C++": 0}}
}

attempts = 0
max_attempts = 3

def login(students):
    global attempts
    while attempts < max_attempts:
        sid = input("Enter Student ID: ")
        pwd = input("Enter Password: ")

        if sid in students and students[sid]["password"] == pwd:
            print(f"Login Successful! Welcome {students[sid]['name']}")
            return sid
        else:
            attempts += 1
            print("Invalid ID or Password. Attempts left:", max_attempts - attempts)

    if attempts == max_attempts:
        print("Too many wrong attempts. Login blocked.")
        return None

def add_marks(marks):
    print("\nEnter marks for the following subjects:")
    for subject in marks:
        while True:
            try:
                score = float(input(f"{subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Please enter a marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    print("Marks updated successfully!")
    return marks

def calculate_percentage(marks):
    total_marks = sum(marks.values())
    num_subjects = len(marks)
    percentage = (total_marks / (num_subjects * 100)) * 100
    return percentage

def view_report_card(name, marks):
    print(f"\n--- Report Card for {name} ---")
    for subject, score in marks.items():
        print(f"{subject}: {score}")
    
    percentage = calculate_percentage(marks)
    print(f"Total Percentage: {percentage:.2f}%")
    
    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 35:
        print("Grade: C")
    else:
        print("Grade: Fail")
    print("------------------------------")

current_student = login(students)

if current_student:
    student_data = students[current_student]
    name = student_data["name"]
    marks = student_data["marks"]

    while True:
        print(f"\nStudent Panel: {name}")
        print("1. Update Marks")
        print("2. View Report Card")
        print("3. Check Percentage")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                marks = add_marks(marks)
            elif choice == 2:
                view_report_card(name, marks)
            elif choice == 3:
                perc = calculate_percentage(marks)
                print(f"Your current percentage is: {perc:.2f}%")
            elif choice == 4:
                # Update back to the main dictionary
                students[current_student]["marks"] = marks
                print("Logging out. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
