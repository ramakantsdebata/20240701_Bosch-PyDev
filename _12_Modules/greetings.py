__all__ = ['greet', 'greetName', 'greetInteractive']

def greet():
    print("Hi there!")

def greetName(name):
    greeting = "Hello"
    finalGreeting = prepareGreeting(greeting, name)
    print(finalGreeting)

def greetInteractive():
    greeting = "Hello"
    name = input("Enter your name: ")
    finalGreeting = prepareGreeting(greeting, name)
    print(finalGreeting)

def prepareGreeting(greeting, name):
    final = greeting + " " + name + "!"
    return final

def Test():
    greet()
    greetName("John")

if __name__ == '__main__':
    Test()

# print(__name__)