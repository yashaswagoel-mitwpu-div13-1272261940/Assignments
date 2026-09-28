import re
txt=input("Enter string: ")
if re.fullmatch(r"[a-z]+",txt):
    print("All lowercase")
elif re.fullmatch(r"[A-Z]+",txt):
    print("All uppercase")
elif re.fullmatch(r"[0-9]+",txt):
    print("All digits")
else:
    print("NA")