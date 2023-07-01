"""print(1)
print('I love \n you')
print( "hij gaat morgen weg \n\tzij komt morgen")
print('Hey!' + str(1))
print ('Jump!'*5)
print ('Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.')
print ('Shane' in 'We went out for dinner with with Anne, Samuel and Bob.')
letter_grades = 'ABCDF'
letter_grades[0]
letter_grades[3]
print (letter_grades[0] == 'A')
print (letter_grades[3] == 'D')
print (letter_grades[-1])
print (letter_grades[-2])
waltz = 'onetwothree'
print (waltz[0:3])
# We don't need to specify the 0 if we start at the beginning
print (waltz[:1])
print (waltz[0:0])
print (len (waltz ))
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
waltz[0:11:2]
answer = 42
qa = f'The answer is.. {answer}'
print (qa)
a = 20
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool(''))
print(bool(0))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print(3 % 2)
print(7 % 2)
print (True is False)
print(True or False)
print (not True)
print(not False)

nice_weather = True
going_outside = True if nice_weather else False
print(going_outside)"""

nice_weather_odds = .7
party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'
print(party_location)