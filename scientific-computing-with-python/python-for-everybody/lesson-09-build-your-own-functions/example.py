x = 5
print('Hello')

def print_lyrics():
    print("Ah, ah, ah, you didn't say the magic word")
    print("I'm gonna carve you up")

print("Hey")

# This calls the function
print_lyrics()

x = x + 2
print(x)

"""
Hello
Ah, ah, ah, you didn't say the magic word
I'm gonna carve you up
Hey
7
"""

# Function with argument
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

"""
greet('en')
Hello

greet('es')
Hola

greet('fr')
Bonjour
"""