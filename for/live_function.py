def Fahrenheit_to_Celsius(Fahrenheit):
    Celsius = (Fahrenheit-32)*5/9
    return Celsius
print(Fahrenheit_to_Celsius(1))

# kan nog korter
def Fahrenheit_to_Celsius(Fahrenheit):
    return (Fahrenheit-32)*5/9

print(Fahrenheit_to_Celsius(1))

# comments, vooral multiline, liefst met '''   '''