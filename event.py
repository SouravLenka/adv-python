# Room Allotment System using Dictionary in Python
room={
    101:None,
    102:None,
    103:None,
    104:None
}
print("choose the operation you want to do:")
print("1=allot the room")
print("2=vacate the room")
print("3=display the room info")
print("4=exit")
ch=0

while ch!=4:
    ch=int(input("Enter the choice:"))   
    if ch==1:
        roomno=int(input("Enter the room no:"))
        name=input("Enter the name of the person:")
        if room[roomno]==None:
            room[roomno]=name
            print("Room alloted successfully")
        else:
            print("Room is already alloted")
    elif ch==2:
        roomno=int(input("Enter the room no:"))
        if room[roomno]!=None:
            room[roomno]=None
            print("Room vacated successfully")
        else:
            print("Room is already vacant")
    elif ch==3:
        for rno,name in room.items():
            if name!=None:
                print(f"Room no: {rno}, Occupant: {name}")
            else:
                print(f"Room no: {rno} is vacant")
    elif ch==4:
        print("Thank you for using the Room Allotment System. Goodbye!")
    else:
        print("Invalid choice. Please try again.")