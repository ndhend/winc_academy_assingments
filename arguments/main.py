# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

''' Define a function greet -> def greet()
    Takes the following arguments in these order:
    A name (str) -> def greet(name)
    A greeting template (str): template: 'Hello, <name>!'-> 
    def greet(name, template='Hello, <name>!' )
    greet should return a string where <name> in the
    greeting template is replaced by the name given ->
    How to replace a string within a string?
    print(dir('Hello, <name>!')) to look for maybe a method replace
'''

#  print(dir('Hello, <name>!')) 


def greet(name, greeting_template='Hello, <name>!'):  # template
    greet = greeting_template.replace('<name>', name)  # kwam ik zelf niet op, heb code van Slack
    # maar had de opdracht niet echt begrepen -> GOED LEZEN EN STAP VOOR STAP WERKEN!
    return greet


# print(greet('Bob', "What's up, <name>!"))

''' Write a function force that takes two arguments:
    def force()
    arg1 -> mass(float)
    def force(mass)
    arg2 -> body(str) -> with 'earth' as default
    def force(mass, body = 'earth)
    implementation should support all bodies in reference
    in lowercase 
    def force(mass, body = 'earth'):
    .lower(body)
    if body.lower in gravity_factor:
    key = body.lower
    f = mass.key
    return f
    
    make sure you process these bodies with the correlated 
    gravity factor in a dictionary:
    gravity_factor =
    {'mercury': 3.7,
      'venus': 8.9,
      'earth' : 9.8,
      'moon' : 1.6,
      'mars': 3.7,
      'jupiter': 23.1,
      'saturn': 9.0,
      'uranus' : 8.7,
      'neptune': 11.0,
      'pluto': 0.7
      }

      
        
        
    force should return the force that is exerted given the mass and body:
    force = ma
    a = 9.8'''

# make sure you process these bodies with the correlated 
# gravity factor in a dictionary:


gravity_factor = {
    'mercury': 3.7,
    'venus': 8.9,
    'earth': 9.8,
    'moon': 1.6,
    'mars': 3.7,
    'jupiter': 23.1,
    'saturn': 9.0,
    'uranus': 8.7,
    'neptune': 11.0,
    'pluto': 0.7,
    'sun': 247
}


def force(mass, body='earth'):
    if body.lower() in gravity_factor:
        gravity = gravity_factor[body.lower()]
        f = mass * gravity
        return f
    
# print(force(6)) # Output: 58.800000000000004 ben het nagegaan en klopt.

'''Write a function pull that takes three arguments:

m1 An object's mass in kg (float)
m2 Another object's mass in kg (float)
d Their distance in meters (float)

def pull(m1,m2,d) # m1 and m2 in kg, d in meters

pull should return the gravitional pull that these two objects have on each other
return G*((m1*m2)/d**2)


I'm only missing G:
G = 6.674×10-11 -> 10-11 = 6.674*(1/10**11)'''


def pull(m1, m2, d):   # m1 and m2 in kg, d in meters
    G = 6.674*(1/10**11)
    return G*((m1*m2)/d**2)


#  print(pull(800, 1500, 3))


print(pull(0.1, 5.972*10**24, 6.371*10**6))
