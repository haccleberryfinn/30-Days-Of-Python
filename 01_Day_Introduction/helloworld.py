
# Introduction
# Day 1 - 30DaysOfPython Challenge

print("Hello World!")   # print hello world

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%) - returns the remainder of the division
print(3 // 2)  # Floor division operator(//) - rounded-up division

# Checking data types 

print(int(10))                  # Int - integer; stores whole numbers
print(float(3.14))                # Float - stores decimal numbers
print(complex(1 + 3j))              # Complex - groups real and imaginary numbers

# EXAMPLES OF USING STRING
string = 'Rhizzho'

print(string)                # prints the text
print(type(string))          # shows <class 'str'>
print(len(string))           # length of the string
print(string.upper())        # RHIZZHO
print(string[0])             # first character: 'R'
print('Hello, ' + string)    # concatenation

#EXAMPLES OF USING LIST 
list = ['cheesecake', 'cookie', 'ice cream']

print(list[0])        # first item: cheesecake
print(len(list))      # number of items: 3

list.append('brownie')   # append - add item
print(list)

print(list.remove('cookie'))    # remove item
print(list)

print(list[1:])       # slice: from second item to end

#EXAMPLES OF USING DICTIONARY  
print(type({'name': 'Asabeneh'}))  # Dictionary

person = {'name': 'Rizzo', 
          'age': 18,
          'city': 'Manila',
         }
print(person)                  # entire dictionary
print(person['name'])          # access value by key
person['age'] = 19             # update value

person['email'] = 'rizzo@example.com'  # add new key/value
print(person)

#EXAMPLES OF USING TUPLE 
print(type({9.8, 3.14, 2.7}))    # Tuple - group multiple pieces in an ordered unit


tuple = (9.8, 3.14, 2.7)   

print(tuple)                      # entire tuple: (9.8, 3.14, 2.7)
print(tuple[0])                   # first item: 9.8
print(len(tuple))                 # number of items: 3
