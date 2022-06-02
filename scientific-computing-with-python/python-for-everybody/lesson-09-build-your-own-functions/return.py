def greet():
    return "Hello"

print(greet(), "Juan")
print(greet(), "Negan")

def greetings(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greetings("es"), "Juan")
print(greetings("fr"), "Negan")
print(greetings("en"), "Rick")