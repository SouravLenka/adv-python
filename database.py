import mysql.connector

connection=mysql.connector.connect(
    user='root',
    password='prem@8260',
    host='localhost',
    port='3306',)

cursor=connection.cursor()
cursor.execute("use tnp")
print("Databases Selected\n")
print("TABLE GIET\n")
#cursor.execute("select * from giet")
#row=cursor.fetchall()
#for r in row:
#    print(r,"\n")

#insert_query="insert into giet values(%s,%s,%s,%s,%s,%s)"
#values=[(110,'Sourav','Rourkela','developer',100000,'M')]
#cursor.executemany(insert_query,values)
#connection.commit()

cursor.execute("select Name,Address from giet;")
names=cursor.fetchall()
print("Names and Addresses of students in GIET:")
for name in names:
    print("Name=",name[0],": Address=",name[1])

cursor.execute("select Rollno,Salary from giet")
roll_salary=cursor.fetchall()
print("\nRoll Numbers and Salaries of students in GIET:")
for roll, salary in roll_salary:
    print("Rollno=",roll,": Salary=",salary)
connection.close()