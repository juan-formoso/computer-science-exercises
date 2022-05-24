lista_dois = ["dois", "two", "dos", "2"]

lista_dois.sort()

for item in lista_dois:
  print(int(item))

"""
ValueError: invalid literal for int() with base 10 occurs when you convert the string or decimal or characters values not formatted as an integer. To solve the error, you can use the float() method to convert entered decimal input and then use the int() method to convert your number to an integer.
"""