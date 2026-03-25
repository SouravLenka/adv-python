import regex as re
q=int(input("enter the number to execute: "))

if q==1:
    pattern=("python")
    search=re.search(pattern,"python is a programming language")
    if search:
        print("pattern found")
    else:
        print("pattern not found")

elif q==2:
    pattern="^a...s$"
    result=re.match(pattern,"abyss")
    print(result)
    
elif q==3:
    string="hello 12 hi 89.Howdy 34"    
    result=re.findall("\d+",string)
    print(result)

elif q==4:
    pattern="sourav"
    data="sourav is a good boy,sourav is a good player"
    result=re.finditer(pattern,data)
    print(result)
    for r in result:
        print(r)