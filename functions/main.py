# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
'''def greet(x):
    greet_x = 'Hello, ' + x
    return greet_x
greet_Bob = greet('Bob')
print(greet_Bob)

def add(int1,int2,int3):
    add_int = int1+int2+int3
    return add_int
x5 = add(5,3,2)
print(x5)

def positive(int):
    positive_int = True if int > 0 else False
    return positive_int
print (positive(50))
print (positive (-50))


def negative(int):
    negative_int = True if int < 0 else False
    return negative_int
print (negative(50))
print (negative(-50))
  
def greet(x):
    greet_x = 'Hello, ' + x + '!'
    return greet_x'''

def greet(x):
    greet_x = f'Hello, {x}!'
    return greet_x

print(greet('Bob'))

def add(x,y,z):
    add_num = x+y+z
    return add_num
print(add(5,3,2))

def positive (x):
    if x > 0:
        return True
    else:
        return False
    
print(positive(50))
print(positive(-50))
print(positive(0))

def negative (x):
    if x < 0:
        return True
    else:
        return False
    
print(negative(50))
print(negative(-50))
print(negative(0))


