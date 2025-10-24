# All Data in Python is Object

print(type(10))        # <class 'int'>  Integer
print(type(100))       # <class 'int'>  Integer
print(type(-50))        # <class 'int'>  Integer

print(type(100.0))     # <class 'float'>  Floating Point Number
print(type(1.95050))   # <class 'float'>  Floating Point Number
print(type(-100.9595)) # <class 'float'>  Floating Point Number

print(type("Hello Python"))  # <class 'str'>  String
print(type("Hello Python"))  # <class 'str'>  => String

print(type([1, 2, 3, 4, 5]))  # <class 'list'> => List

print(type((1, 2, 3, 4, 5)))  # <class 'tuple'> => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # <class 'dict'> => Dictionary

print(type(2 == 2))  # <class 'bool'> => Boolean

#________________________________________________________________________________________

# -------------------------------
# -- Variables --
# -------------------------------
#
# Syntax => [Variable Name] [Assignment Operator] [Value]
# -- Name Convention and Rules:

# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot With Num Or Special Characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------------

name = "Mohamed Ramy"       # Single Word => Normal
myName = "Mohamed Ramy"     # Two Words => camelCase style
_my_name = "Mohamed Ramy"   # Two Words => snake_case (leading underscore allowed)

print(name)
print(myName)
print(_my_name)
#________________________________________________________________________________________

#Source Code : Original Code You Write it in Computer
#Translation : Converting Source Code Into Machine Language
#Compilation : Translate Code Before Run Time
#Run-Time : Period App Take To Executing Commands
#Interpreted : Code Translated On The Fly During Execution
# --------------------------------------------------------------

x = 10
x = "Hello"

print(x)

#________________________________________________________________________________________

#Reserved Words

help("keywords")

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

#________________________________________________________________________________________

#-----------------------------
#Escape Sequences Characters
#\b => Back Space
#\newline => Escape New Line + \
#\ => Escape Back Slash
#' => Escape Single Quotes
#" => Escape Double Quotes
#\n => Line Feed
#\r => Carriage Return
#\t => Horizontal Tab
#\xhh => Character Hex Value
#-----------------------------

print("Hello\bworld") # Will Remove o

#Escape New Line + Back Slash
print("Hello \
I Love \
Python")

#Escape Back Slash

print("I Love Back Slash \\")

#Escape Single Quote
print('I Love Single Quote \'Test\' ')

#Escape Double Quotes
print("I Love Double Quotes \"Test\" ")

#Line Feed
print("Hello World\nSecond Line")

#Escape Double Quotes
print("I Love Double Quotes \"Test\" ")

#Line Feed
print("Hello World\nSecond Line")

#Carriage Return
print("123456\rAbcd")

#Horizontal Tab
print("Hello\tPython")

#Character Hex Value
print("\x4F\x73")

#________________________________________________________________________________________

# -----------------
# Concatenation --
# -----------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

full = msg + " " + lang
print(full)

a = "First \
Second \
Third"

b = "A \
B \
C"

print(a + "\n" + b)
print("Hello " + 1)
#________________________________________________________________________________________

#-----------------
#-- Strings --
#-----------------

#-------------------------------------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''
myStringSix = """First
Second "Test" \\ 'Test'
Third"""

print(myStringFive)

#________________________________________________________________________________________

# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# -----------------------------------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"
print(myString)
# -----------------------------------------------------------
#________________________________________________________________________________________

# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "  I Love Python  "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "######I Love Python###"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@@@#@#I Love Python@@@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# -----------------------------------------------------------

# title()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# -----------------------------------------------------------

# capitalize()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# -----------------------------------------------------------

# zfill

c, d, e = "1", "11", "111"

print(c)
print(d)
print(e)

print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))

# -----------------------------------------------------------

# upper()

g = "osama"

print(g.upper())

#________________________________________________________________________________________

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 2))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 2))

# -----------------------------------------------------------

# center()

e = "Osama"
print(e.center(9)) # Spaces
print(e.center(9, "#")) # Hashes
print(e.center(15, "@")) # @

# -----------------------------------------------------------

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP")) # 2 PHP wOrds
print(f.count("PHP", 0, 25)) # Only One PHP Word

# -----------------------------------------------------------

# StartsWith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# -----------------------------------------------------------

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# -----------------------------------------------------------

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P")) # Index Number 7
print(a.index("P", 0, 10)) # Index Number 7
print(a.index("P", 0, 5)) # Through Error

# -----------------------------------------------------------

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P"))
print(a.index("P", 0, 10))
print(b.find("P", 0, 5)) # -1

# -----------------------------------------------------------

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

# -----------------------------------------------------------

# splitlines()

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# -----------------------------------------------------------

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""

print(three.isspace())
print(four.isspace())
five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

# -----------------------------------------------------------

# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# -----------------------------------------------------------

# join(Iterable)

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

# -----------------------------------------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age) # Type Error

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# -----------------------------------------------------------

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# -----------------------------------------------------------

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# -----------------------------------------------------------

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# -----------------------------------------------------------

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# -----------------------------------------------------------

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c)) # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c)) # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c)) # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# -----------------------------------------------------------

# Format in Version 3.6+

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}".format(myName=myName, myAge=myAge))
print(f"My Name is : {myName} and My Age is : {myAge}")

#________________________________________________________________________________________

# -----------
# -- Numbers --
# -----------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# -----------------------------------------------------------

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# -----------------------------------------------------------

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print("Real Part Is: {}".format(myComplexNumber.real))
print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
print(int(10+9j))

#________________________________________________________________________________________

# -----------
# -- Arithmetic Operators --
# -----------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# -----------------------------------------------------------

# Addition

print(10 + 30) # 40
print(-10 + 20) # 10
print(1 + 2.66) # 3.66
print(1.2 + 1.2) # 2.4

# -----------------------------------------------------------

# Subtraction

print(60 - 30) # 30
print(-30 - 20) # -50
print(-30 - -20) # -10
print(5.66 - 3.44) # 2.22

# -----------------------------------------------------------

# Multiplication

print(10 * 3) # 30
print(5 + 10 * 100) # 1005
print((5 + 10) * 100) # 1500

# -----------------------------------------------------------

# Division

print(100 / 20) # 5.0
print(int(100 / 20)) # 5

# -----------------------------------------------------------

# Modulus

print(8 % 2) # 0
print(9 % 2) # 1
print(20 % 5) # 0
print(22 % 5) # 2

# -----------------------------------------------------------

# Exponent

print(2 ** 5) # 32
print(2 * 2 * 2 * 2 * 2) # 32
print(5 ** 4) # 625
print(5 * 5 * 5 * 5) # 625

# -----------------------------------------------------------

# Floor Division

print(100 // 20) # 5
print(119 // 20) # 5
print(120 // 20) # 6

#________________________________________________________________________________________

# --------------------
# -- Lists --
# --------------------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# --------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList) # Whole List
print(type(myAwesomeList[1])) # "One"
print(myAwesomeList[-1]) # True
print(myAwesomeList[-3]) # 1

print(myAwesomeList[1:4]) # ['Two', 'One', 1]
print(myAwesomeList[:4]) # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:]) # ['Two', 'One', 1, 100.5, True]

# -----------------------------------------------------------

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A"]
print(myAwesomeList)

# -----------------------------------------------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)

print(myFriends)

# -----------------------------------------------------------

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# -----------------------------------------------------------

# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# -----------------------------------------------------------

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

# -----------------------------------------------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b) # Main List
print(c) # Copied List
b.append(5)

print(b) # Main List
print(c) # Copied List

# -----------------------------------------------------------

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# -----------------------------------------------------------

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# -----------------------------------------------------------

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
# f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# -----------------------------------------------------------

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))

#________________________________________________________________________________________

# --------------------
# -- Tuple --
# --------------------

# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# --------------------

# Tuple Syntax & Type Test

myAwesomeTupleOne = ("Osama", "Ahmed")
myAwesomeTupleTwo = "Osama", "Ahmed"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# -----------------------------------------------------------

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# -----------------------------------------------------------

# Tuple Assign Values

myAwesomeTupleFour = (1, 2, 3, 4, 5)
myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour) # 'tuple' object does not support item assignment

# -----------------------------------------------------------

# Tuple Items

myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])

# -----------------------------------------------------------

# Tuple With One Element

myTuple1 = ("Osama",)
myTuple2 = "Osama",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

# -----------------------------------------------------------

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

# -----------------------------------------------------------

# Tuple, List, String Repeat (*)

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# -----------------------------------------------------------

# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7)) # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# -----------------------------------------------------------

print("The Position of Index Is: " + b.index(7)) # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct

a = ("A", "B", 4 , "C")

x, y, z = "A", "B", "C"

print(x)
print(y)
print(z)

#________________________________________________________________________________________
# -----------
# -- Set --
# -----------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------

# Not Ordered And Not Indexed

mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
print(mySetTwo[0:3])

# print(mySetOne[0])

# -----------------------------------------------------------

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# -----------------------------------------------------------

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)

# -----------------------------------------------------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# -----------------------------------------------------------

# union()

b = {"One", "Two", "Three"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# -----------------------------------------------------------

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# -----------------------------------------------------------

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# -----------------------------------------------------------

 # g.remove(7)
print(g)

# -----------------------------------------------------------

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# -----------------------------------------------------------

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# -----------------------------------------------------------

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)

# -----------------------------------------------------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b)) # a - b
print(a)

print("=" * 40) # Separator

# -----------------------------------------------------------

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d) # c - d
print(c)

print("=" * 40) # Separator

# -----------------------------------------------------------

# intersection()

e = {1, 2, 3, 4, "X" , "osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f)) # e & f
print(e)
print("=" * 40) # Separator

# -----------------------------------------------------------

# intersection_update()

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h) # g & h
print(g)

# -----------------------------------------------------------

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i)

print("=" * 40) # Separator

# -----------------------------------------------------------

# issubset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b)) # True
print(a.issuperset(c)) # False

# -----------------------------------------------------------

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h)) # False
print(g.isdisjoint(i)) # True

#________________________________________________________________________________________

# ---------------------
# # -- Dictionary Methods --
# # ---------------------

# clear()

user = {
    "name": "Osama"
}
user.clear()
print(user)

print("=" * 50)

# update()

member = {
    "name": "Osama"
}

# -----------------------------------------------------------

# popitem()

member = {
"name": "Osama",
"skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

# -----------------------------------------------------------

# items()

view = {
"name": "Osama",
"skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# -----------------------------------------------------------

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))

#________________________________________________________________________________________
# ---------
# -- Boolean --
# ---------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------

name = ""
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# -----------------------------------------------------------

# True Values

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# -----------------------------------------------------------

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))

#________________________________________________________________________________________

age = 36
country = "Egypt"
rank = 10

# print(age > 16 and country == "Egypt" and rank > 0) # True
# print(age > 16 and country == "KSA" and rank > 0) # False   

print(age > 16) # True
print(not age > 16) # Not True = False

#________________________________________________________________________________________
# ---------
# -- Assignment Operators --
# ---------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# ---------

x = 10 # Var One
y = 20 # Var Two

# Var One = Self [Operator +] Var Two
# Var One [Operator +=] Var Two

# x = x + y

x += y
x -= y # x -= y

print(x)

#________________________________________________________________________________________

# ---------
# -- Comparison Operators --
# ---------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# ---------

# Equal + Not Equal

print(100 == 100)
print(100 == 200)
print(100 == 100.00)

print("#" * 50)

print(100 != 100)
print(100 != 200)
print(100 != 100.00)

print("#" * 50)

# -----------------------------------------------------------

# Greater Than + Less Than

print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 40)

print("#" * 50)

print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print(100 < 40)

print("#" * 50)

# -----------------------------------------------------------

# Greater Than or Equal + Less Than or Equal

print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
print(100 >= 40)

print("#" * 50)

print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)
print(100 <= 40)

print("#" * 50)

#________________________________________________________________________________________
# ---------
# -- Type Conversion --
# ---------

# str()

a = 10
print(type(a))
print(type(str(a)))

# -----------------------------------------------------------

# tuple()

c = "Osama" # String
d = [1, 2, 3, 4, 5] # List
e = {"A", "B", "C"} # Set
f = {"A": 1, "B": 2} # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

# -----------------------------------------------------------

# list()

c = "Osama" # String
d = (1, 2, 3, 4, 5) # Tuple
e = {"A", "B", "C"} # Set
f = {"A": 1, "B": 2} # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("#" * 50)

# -----------------------------------------------------------

# set()

c = "Osama" # String
d = (1, 2, 3, 4, 5) # Tuple
e = ["A", "B", "C"] # List
f = {"A": 1, "B": 2} # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

# -----------------------------------------------------------

# dict()

d = (("A", 1), ("B", 2), ("C", 3)) # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]] # List

print(dict(d))
print(dict(e))

#________________________________________________________________________________________

# ---------
# -- User Input --
# ---------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')

# fName = fName.strip()
# mName = mName.strip()
# lName = lName.strip()

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName} {lName} Happy To See You.")

#________________________________________________________________________________________

# ---------
# -- Practical Slice Email --
# ---------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()

theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "medo@elostora.org"
# print(email[:email.index("@")])

#________________________________________________________________________________________

# ---------
# -- Practical Your Age Full Details --
# ---------

# Input Age
age = int(input('What\'s Your Age ?').strip())

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You Lived For:')

print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")

#________________________________________________________________________________________

# ---------
# -- Control Flow --
# -- If, Elif, Else --
# -- Make Decisions --
# ---------

uName = "Osama"
uCountry = "KSA"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

#________________________________________________________________________________________

# -----------------------------------------------------------
# ---------
# -- Nested If --
# ---------

uName = "Osama"
isStudent = "Yes"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

 if isStudent == "Yes":

    print(f"Hi {uName} Because U R From {uCountry} And Student")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

 
else:

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

# -----------------------------------------------------------
# ---------
# -- Ternary Conditional Operator --
# ---------

country = "A"

if country == "Egypt": print(f"The Weather in {country} Is 15")
elif country == "KSA": print(f"The Weather in {country} Is 30")
else: print("Country is Not in The List")

# Short If

movieRate = 18
age = 16

if age < movieRate :

    print("Movie S Not Good 4U") # Condition If True

else :

    print("Movie S Good 4U And Happy Watching")

print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False

#________________________________________________________________________________________

# ---------
# -- Calculate Age Advanced Version and Training --
# ---------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)

# Collect Age Data
age = input("Please Write Your Age").strip()

# -----------------------------------------------------------

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days.").strip().lower()

# -----------------------------------------------------------

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months':

    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

    print("You Choosed The Unit Days")
    print(f"You Lived For {days:,} Days.")

#________________________________________________________________________________________

# -----------------------------
# -- Membership Operators --
# -----------------------------
# in
# not in
# -----------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# -----------------------------------------------------------

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# -----------------------------------------------------------

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Egypt"

if myCountry in countriesOne:
    print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")
elif myCountry in countriesTwo:
    print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")
else:
    print("You Have No Discount")

#________________________________________________________________________________________

# ------------------------------------
# -- Practical Membership Control --
# ------------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

    # print(admins)
    # admins[admins.index("Osama")] = "Elzero"
    # print(admins)

# Login
name = input("Please Type Your Name ").strip().capitalize()


if name in admins :
    print(f"Hello {name} Welcome Back")

    option = input("Delete Or Update Your Name ?").strip().capitalize()

    if option == 'Update':

        theNewName = input("Your New Name Please ").strip().capitalize()
           

else:
    print("You Are Not Admin")

#________________________________________________________________________________________

# --------------------
# -- Loop => While --
# --------------------
# while condition_is_true
# Code Will Run

a = 0

while a < 15:
    print(a)
    a += 1 # a = a + 1

print("Loop is Done") # True Become False

# while False:
#
#     print("Will Not Print")

# -----------------------------------------------------------

# ------------------------------
# -- Loop => While Training --
# ------------------------------
# while condition_is_true
# Code Will Run Until Condition Become False
#

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF)) # List Length [10]

a = 0

while a < len(myF): # a < 10
    print(f"#{str(a + 1).zfill(3)} {myF[a]}")

    a += 1 # a = a + 1

else:
    print("All Friends Printed To Screen.")

print(myF[0])
print(myF[1])
print(myF[2])
print(myF[3])
print(myF[4])
print(myF[5])
print(myF[6])
print(myF[7])
print(myF[8])
print(myF[9])

# -----------------------------------------------------------

# ------------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ------------------------------

# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:

    # Input The New Website
    web = input("Website Name Without https:// ")

    # Add The New Website To The List
    myFavouriteWebs.append(f"https://{web.strip().lower()}")

    # Decrease One Number From Allowed Websites
    maximumWebs -= 1 # maximumWebs = maximumWebs - 1

    # Print The Add Message
    print(f"Website Added, {maximumWebs} Places Left")
    # Print The List
    print(myFavouriteWebs)

else:

    print("Bookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:

    # Sort The List
    myFavouriteWebs.sort()

index = 0

print("Printing The List Of Websites in Your Bookmark")

while index < len(myFavouriteWebs):

    print(myFavouriteWebs[index])

    index += 1 # index = index + 1

# -----------------------------------------------------------

# ------------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ------------------------------

tries = 4

mainPassword = "Osama@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword: # True

    tries -= 1 # tries = tries - 1

    print(f"Wrong Password, {'Last' if tries == 0 else tries } Chance Left")

    inputPassword = input("Write Your Password: ")

    if tries == 0:

        print("All Tries Is Finished.")

        break

        print("Will Not Print")
else:

    print("Correct Password")

#________________________________________________________________________________________

# --------------------
# -- Loop => For --
# --------------------
# for item in iterable_object :
# Do Something With Item
# --------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:

    # print(number * 17)

    if number % 2 == 0: # Even

        print(f"The Number {number} Is Even.")

    else :
        print(f"The Number {number} Is Odd.")

myName = "ELOSTORA"

for letter in myName:

    print(f"[ {letter.upper()} ]")

# ---------------------------------------------------------------------------------------

# --------------------
# -- Loop => For --
# -- Trainings --
# --------------------

# Range

# myRange = range(1, 101)

# for number in myRange:
#
#     print(number)

# Dictionary

mySkills = {
    "Html": "90%",
    "Css": "60%",
    "PHP": "70%",
    "JS": "80%",
    "Python": "90%",
}

print(mySkills['JS'])
print(mySkills.get("Python"))

for skill in mySkills:

    # print(skill)

    print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}")

# ---------------------------------------------------------------------------------------

# --------------------
# -- Loop => For --
# -- Nested Loop --
# --------------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples: # Outer Loop

    print(f"{name} Skills Is: ")

    for skill in skills: # Inner Loop

        print(f"- {skill}")

peoples = {
    "Osama": {
        "Html": "70%",
        "Css": "80%",
        "Js": "70%"
    },
    "Ahmed": {
        "Html": "90%",
        "Css": "80%",
        "Js": "90%"
    },
    "Sayed": {
        "Html": "70%",
        "Css": "60%",
        "Js": "90%"
    }
}

# print(peoples["Osama"])
# print(peoples["Ahmed"])
# print(peoples["Sayed"])

# print(peoples["Osama"]['Css'])
# print(peoples["Ahmed"]['Css'])
# print(peoples["Sayed"]['Css'])

for name in peoples:

    print(f"Skills and Progress For {name} Is: ")

    for skill in peoples[name]:

        print(f"{skill.upper} => {peoples[name][skill]}")

#________________________________________________________________________________________

# -----------------------------
# -- Break, Continue, Pass --
# -----------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

    if number == 13:

        continue

    print(number)

# Break

for number in myNumbers:

    if number == 13:

        break

    print(number)

# Pass

for number in myNumbers:

    if number == 13:

        pass

    print(number)

# ---------------------------------------------------------------------------------------

# -------------------------------
# -- Advanced Dictionary Loop --
# -------------------------------

mySkills = {
    "HTML": "80%",
    "CSS": "90%",
    "JS": "70%",
    "PHP": "80%"
}

# print(mySkills.items())

# for skill in mySkills:
#
#     print(f"{skill} => {mySkills[skill]}")

for skill_key, skill_progress in mySkills.items():

    print(f"{skill_key} => {skill_progress}")

myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "80%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "70%"
    }
}

for main_key, main_value in myUltimateSkills.items():

    print(f"{main_key} Progress Is: ")

    for child_key, child_value in main_value.items():

        print(f"- {child_key} => {child_value}")

# ------------------------------
# -- Function And Return --
# ------------------------------
# [1] A Function is A Reusable Block of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ------------------------------

def function_name():
    return "Hello Python From Inside Function"

dataFromFunction = function_name()

print(dataFromFunction)

# ---------------------------------------------------------------------------------------

# ---------------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------------

a, b, c = "Osama", "Ahmed", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def                        => Function Keyword [Define]
# say_hello()                => Function Name
# name                       => Parameter
# print(f"Hello {name}")     => Task
# say_hello("Ahmed")         => Ahmed is The Argument

def say_hello(name):

    print(f"Hello {name}")

# say_hello(a)
# say_hello(b)
# say_hello(c)

# def addition(n1, n2):
#
#     print(n1 + n2)
#
# addition(100, 300)
# addition(-50, 100)

def addition(n1, n2):

    print(int(n1) + int(n2))

addition("100", 300)

def addition(n1, n2):
    if type(n1) != int or type(n2) != int: 
        print("Only Integers Allowed") 
    else: print(n1 + n2)

addition("100", "Osama")

addition(100, 500)

# ---------------------------------------------------------------------------------------

# -- Function Packing, Unpacking Arguments *Args --

print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)

def say_hello(*peoples): # n1, n2, n3, n4

    for name in peoples:

        print(f"Hello {name}")

say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")


def show_details(skill1, skill2, skill3, skill4):
    print(f"Hello Osama Your Skills Is: ")
    
    print(f"{skill1}")
    print(f"{skill2}")
    print(f"{skill3}")
    print(f"{skill4}")

show_details("Html", "CSS", "JS", "Python")

def show_details(name, *skills):
    
    print(f"Hello {name} Your Skills Is: ")
    
    for skill in skills:
        
        print(skill)

show_details("Osama", "Html", "CSS", "JS")
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")

#________________________________________________________________________________________

# ------------------------------
# -- Function Recursion --
# ------------------------------
# -----------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# -----------------------------------------------------------------

def cleanWord(word):

    if len(word) == 1:

        return word

    print(f"Print Start Function {word}")

    if word[0] == word[1]: # rrldd

        print(f"Print Before Condition {word}")

        return cleanWord(word[1:])

    print(f"Print Before Return {word}")

    return word[0] + cleanWord(word[1:])

# Stash [ World ]

print(cleanWord("WWwoooolrridd"))

#________________________________________________________________________________________

# ------------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# ------------------------------

def say_hello(name, age): return f"Hello {name} your Age Is: {age}"

hello = lambda name, age: f"Hello {name} your Age Is: {age}"

print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))