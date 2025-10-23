# Count all chars, digits and symbols in a string
str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0 

for ch in str1:
    if ch.isalpha():
        chars +=1
    elif ch.isdigit():
        digits +=1
    else :
        symbols +=1

print("chars = ", chars)
print("digits = ", digits)
print("symbols = ", symbols)
