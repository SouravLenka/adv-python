# 1.Find common elements between two lists using set
l1=[1,2,3,4]
l2=[3,4,5,6]
com=set(l1) & set(l2)
print(com)

# 2.Remove duplicate words from a sentence using set
sent=str(input("Enter the sentence:"))
wor=sent.split()
uni=set(wor)
print(uni)

# 3.check if two strings are anagrams using set and logic
str1=str(input("Enter a str1:"))
str2=str(input("Enter a str2: "))
if set(str1)==set(str2) and len(str1)==len(str2):
    print("both are anaggrams")
else:
    print("not anagrams")

# 4.find the element present in first list and not in the second list
lst1=eval(input("Enter list1 :"))
lst2=eval(input("Enter list1 :"))
el=set(lst1)-set(lst2)
print(el)

# 5.check if all character in a string are unique using set
s=str(input("Enter the string :"))
if len(str)==len(set(str)):
    print("Duplicate there")
else:
    print("No duplicates there")

# 6.count number of disctinct elements in a list using set
l=eval(input("Enter the list :"))
d=set(l)
print("Number of distinct elements:",len(d))

# 7. find symmetric difference between two sets without builtin functin
set1={1,2,3}
set2={3,4,5}
result=set()
for i in set1:
    if i not in set2:
        result.add(i)
for i in set2:
    if i not in set1:
        result.add(i)
print(result)
# 8.remove common character from two strig using set
stri1=str(input("Enter a str1:"))
stri2=str(input("Enter a str2: "))
rom=set(stri1) & set(stri2)
res1=''.join([i for i in stri1 if i not in rom])
res2=''.join([i for i in stri2 if i not in rom])
print("String 1 after removing common characters:",res1)
print("String 2 after removing common characters:",res2)

# 9.check if one set is a subset of another without built in functions
setA={1,2,3,4}
setB={2,3}
issub=True
for e in setB:
    if e not in setA:
        issub=False
        break
print(issub)

# 10.find repeated elements is a list using set 
lstA=eval(input("Enter the list :"))
nrep=set()
rep=set()
for i in lstA:
    if i in nrep:
        rep.add(i)
    else:
        nrep.add(i)
print("Not repeated  :",nrep," ,Repeated :",rep)    