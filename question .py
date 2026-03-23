question=int(input("Enter the question number: "))

#1. Write a program that takes two integers, computes their sum, difference, product, and division, checks if they’re even/odd, and converts one to a float.
if question==1:
    int1=int(input("Enter the first integer: "))
    int2=int(input("Enter the second integer: "))
    sum=int1+int2
    dif=int1-int2
    prod=int1*int2
    div=int1/int2
    if int1%2==0:
        print(int1,"is even")
    else:
        print(int1,"is odd")
    if int2%2==0:
        print(int2,"is even")
    else:
        print(int2,"is odd")
    float_int1=float(int1)


#2. Process a user-entered sentence: count vowels/consonants, reverse it, replace spaces with underscores, capitalize words.
if question==2:
    sen=input("Enter a sentence: ")
    vowels='aeiouAEIOU'
    vowel_count=0
    consonant_count=0
    for char in sen:
        if char in vowels:
            vowel_count+=1
        elif char.isalpha():
            consonant_count+=1
    reversed_sen=sen[::-1]
    underscore_sen=sen.replace(" ","_")
    capitalized_sen=sen.title()
    print("Vowels:",vowel_count)
    print("Consonants:",consonant_count)
    print("Reversed:",reversed_sen)
    print("Underscored:",underscore_sen)
    print("Capitalized:",capitalized_sen)


#3. Filter numeric values from a mixed-type tuple, attempt modification (handle error), and concatenate two tuples.
if question==3:
    mixed_tuple=(1,'hello',3.14,'world',5)
    numeric_values=tuple(x for x in mixed_tuple if isinstance(x,(int,float)))
    print("Numeric values:",numeric_values)
    try:
        mixed_tuple[0]=10
    except TypeError as e:
        print("Error:",e)
    tuple1=(1,2,3)
    tuple2=('a','b','c')
    concatenated_tuple=tuple1+tuple2
    print("Concatenated tuple:",concatenated_tuple)

#4. Create a student marks dictionary, then add, update, delete entries, and display keys, values, and items.
if question==4:
    marks={'Alice':85,'Bob':90,'Charlie':78}
    print("Initial marks:",marks)
    marks['David']=92
    print("After adding David:",marks)
    marks['Alice']=88
    print("After updating Alice's marks:",marks)
    del marks['Charlie']
    print("After deleting Charlie:",marks)
    print("Keys:",marks.keys())
    print("Values:",marks.values())
    print("Items:",marks.items())

#5. Sort strings by length, identify palindromes, and replace spaces with hyphens using list comprehension.
if question==5:
    strings=['hello','world','madam','python programming']
    sorted_strings=sorted(strings,key=len)
    print("Sorted by length:",sorted_strings)
    palindromes=[s for s in strings if s==s[::-1]]
    print("Palindromes:",palindromes)
    hyphenated_strings=[s.replace(" ","-") for s in strings]
    print("Hyphenated strings:",hyphenated_strings)
    
#6. Convert a mixed-type tuple to a list, remove integers less than 10, and convert back to a tuple.
if question==6:
    mixed_tuple=(1,'hello',3.14,'world',5,12)
    mixed_list=list(mixed_tuple)
    filtered_list=[x for x in mixed_list if not (isinstance(x,int) and x<10)]
    filtered_tuple=tuple(filtered_list)
    print("Filtered tuple:",filtered_tuple)

#7. Build a Student Record System using nested dictionaries/lists to add students, update marks, compute averages, and find toppers.
if question==7:
    students={
        'Alice':{'marks':[85,90,78]},
        'Bob':{'marks':[80,88,92]},
        'Charlie':{'marks':[78,82,85]}
    }
    def add_student(name, marks):
        students[name]={'marks':marks}
    def update_marks(name, marks):
        if name in students:
            students[name]['marks']=marks
    def compute_average(name):
        if name in students:
            return sum(students[name]['marks'])/len(students[name]['marks'])
    def find_topper():
        topper=None
        highest_avg=0
        for name in students:
            avg=compute_average(name)
            if avg>highest_avg:
                highest_avg=avg
                topper=name
        return topper


#8. Create a contact book using a dictionary with options to add, search, delete, and list contacts.
if question==8:
    contact_book={}
    def add_contact(name, phone):
        contact_book[name]=phone
    def search_contact(name):
        return contact_book.get(name,"Contact not found")
    def delete_contact(name):
        if name in contact_book:
            del contact_book[name]
    def list_contacts():
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")


#9. Employee Attendance System
#Build a loop-based menu system to add, remove, and display employee names stored in a dictionary. Use conditions and loops to control program flow.
if question==9:
    attendance={}
    while True:
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Employees")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter employee name: ")
            attendance[name]=True
        elif choice==2:
            name=input("Enter employee name to remove: ")
            if name in attendance:
                del attendance[name]
            else:
                print("Employee not found.")
        elif choice==3:
            print("Employees present:")
            for name in attendance:
                print(name)
        elif choice==4:
            break
        else:
            print("Invalid choice. Please try again.")

#10. Student Record Manager
#Create a system where a user can enter multiple student records (name, roll number, marks). Use loops to add records and conditions to filter students based on pass/fail criteria. Store data using dictionaries and lists.
if question==10:
    student_records=[]
    while True:
        name=input("Enter student name: ")
        roll_number=input("Enter roll number: ")
        marks=int(input("Enter marks: "))
        student_records.append({'name':name,'roll_number':roll_number,'marks':marks})
        cont=input("Add another record? (y/n): ")
        if cont.lower()!='y':
            break
    print("Student Records:")
    for record in student_records:
        status="Pass" if record['marks']>=40 else "Fail"
        print(f"Name: {record['name']}, Roll Number: {record['roll_number']}, Marks: {record['marks']}, Status: {status}")

#11. Restaurant Billing System
#Display a menu with prices and allow users to order multiple items. Calculate the total bill with tax. Use loops for ordering, dictionaries for storing menu, and conditionals for bill logic.
if question==11:
    menu={
        'Burger': 5.99,
        'Pizza': 8.99,
        'Salad': 4.99,
        'Soda': 1.99
    }
    order={}
    while True:
        print("Menu:")
        for item, price in menu.items():
            print(f"{item}: ${price}")
        choice=input("Enter the item you want to order (or 'done' to finish): ")
        if choice.lower()=='done':
            break
        elif choice in menu:
            quantity=int(input(f"Enter quantity of {choice}: "))
            order[choice]=order.get(choice,0)+ quantity
        else:
            print("Item not on menu. Please try again.")
    total=0
    for item, quantity in order.items():
        total+=menu[item]*quantity
    tax=total*0.07
    final_bill=total+tax
    print(f"Total: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Final Bill: ${final_bill:.2f}")

#12. Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations in O(1) time.
if question==12:
    class LRUCache:
        def __init__(self, capacity):
            self.cache={}
            self.capacity=capacity
            self.order=[]
        
        def get(self, key):
            if key in self.cache:
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            return -1
        
        def put(self, key, value):
            if key in self.cache:
                self.order.remove(key)
            elif len(self.cache)>=self.capacity:
                lru_key=self.order.pop(0)
                del self.cache[lru_key]
            self.cache[key]=value
            self.order.append(key)

#13. Unique Character Extractor
#Input a sentence and print characters that appear only once. Ignore spaces and punctuation. Use sets and loops to identify uniqueness.


#14. Custom Power Function

#Create a function that takes base and exponent as input and returns base^exponent using loops (not using pow()).

#15. String Pattern Validator
#Input a string and check whether it’s a palindrome. Count total vowels, consonants, digits, and special characters using loops and conditions.

#16. Design a School Management System that includes classes for Student, Teacher, and Admin, each with unique behaviors.

#17. Implement a Library Management System that uses parameterized constructors to initialize books and members and destructors to log when books are removed.

#18. Design a File Logger System
#Problem: Create a class Logger that logs operations to a file. Use parameterized constructors to define the log file path.
#Implement a destructor to automatically close the file when the object is destroyed. Use method overloading to support different types of logs (info, warning, error).

#19. Vehicle Rental System
#Problem: Create a rental system with a base class Vehicle and subclasses Car, Bike, and Truck.
#Include a rental rate for each and calculate the rental fee using overridden methods. Use class variables to track total vehicles rented.


#20. Build a Mini Social Media Platform
#Problem: Design classes for User, Post, and Comment. Users can post messages, like posts, and comment.
#Use object relationships (e.g., posts have comments), class variables to count total posts, and override the string representation methods to print user-friendly content.