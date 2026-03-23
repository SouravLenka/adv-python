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

#5. Connect to a MySQL database, execute queries to retrieve and manipulate data, and handle exceptions.
if question==5:
    import mysql.connector

    connection=mysql.connector.connect(
    user='root',
    password='prem@8260',
    host='localhost',
    port='3306',)
    cur=connection.cursor()
    try:
        cur.execute("use tnp")
        print("Database selected")
        cur.execute("select Name,Address from giet;")
        names=cur.fetchall()
        print("Names and Addresses of students in GIET:")
        for name in names:
            print("Name=",name[0],": Address=",name[1])
    except mysql.connector.Error as err:
        print("Error:",err)
    finally:
        connection.close()