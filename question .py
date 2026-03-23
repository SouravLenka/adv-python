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

#8. Create a contact book using a dictionary with options to add, search, delete, and list contacts.

#9. Employee Attendance System
#Build a loop-based menu system to add, remove, and display employee names stored in a dictionary. Use conditions and loops to control program flow.


#10. Student Record Manager
#Create a system where a user can enter multiple student records (name, roll number, marks). Use loops to add records and conditions to filter students based on pass/fail criteria. Store data using dictionaries and lists.

#11. Restaurant Billing System
#Display a menu with prices and allow users to order multiple items. Calculate the total bill with tax. Use loops for ordering, dictionaries for storing menu, and conditionals for bill logic.

#12. Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations in O(1) time.

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