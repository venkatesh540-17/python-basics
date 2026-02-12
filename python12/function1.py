def printname(name):
    print(f"hello,{name}!")

printname("venkat")
printname("harry")


#functions with return value
def addnumbers(a,b):
    result = a+b
    return result

sum1=addnumbers(4,5)
print(sum1)

sum2=addnumbers(3,4)
print(sum2)

#function with arguements and paramaters
def login(username,password):
    if username=="venkat"and  password=="harry":
        return"login successfull"
    else:
         return "login-unsuccessfull"

result=login("venkat","harry")
print(result)

#string methods
data ="venkatesh"
data.isalpha()
print('yes')
print(data.replace("venk","knev"))


text = "hello world"
print(text.upper())

text = "HELLO WORLD"
print(text.lower())

text = "hello world"
print(text.capitalize())

text = "welcome to python"
print(text.title())

text = "PyThOn"
print(text.swapcase())

text = "python programming"
print(text.find("pro"))
# print(text[6].isspace())

text = "hello hello"
print(text.rfind("hello"))
print(text.find("hello"))

text = "banana"
print(text.count("a"))

text = "I like apples"
print(text.replace("apples", "oranges"))

text = "   hello   "
print(text.strip())

text = "   hello   "
print(text.lstrip())
print(text.rstrip())

text = "python"
print(text.startswith("py"))

text = "example.txt"
print(text.endswith(".txt"))

text = "abc123"
print(text.isalnum())

text = "hello"
print(text.isalpha())

text = "1234"
print(text.isdigit())

text = "python"
print(text.islower())
print(text.isupper())

text = "   "
print(text.isspace())

text = "Hello World"
print(text.istitle())

text = "apple,banana,orange"
print(text.split(","))

text = "one two three"
print(text.rsplit(" ", 1))

text = "Hello\nWorld"
t="""Hello
World
"""
print(t.splitlines())
print(text.splitlines())

words = ["I", "love", "Python"]
print(" ".join(words))

text = "Python"
print(text.center(50, '*'))

text = "Python"
print(text.ljust(10, '-'))
print(text.rjust(10, ' '))

text = "42"
print(text.zfill(5))

text = "My name is {} and I am {} years old."
print(text.format("venkat", 21))
name="venkat"
age=21
print(f"My name is {name} and I am {age} years old.")

text = "email@domain.com"
print(text.partition("@"))
