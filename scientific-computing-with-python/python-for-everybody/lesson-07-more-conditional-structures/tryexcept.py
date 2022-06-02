astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
    
print("Second", istr)

"""
When the first conversion fails - it just drops into the except: clause and the program continues.

When the second conversion succeds - it just skips the except: clause and the program continues.
"""