import regex as re
pattern=("python")
match=re.search(pattern,"python is a programming language")
if match:
    print("pattern found")
else:
    print("pattern not found")