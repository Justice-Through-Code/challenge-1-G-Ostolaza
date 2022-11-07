
def convert_100_to_celsius():
    #converting fahrenheit to celsius
    celsius_100 = (100 - 32)*5/9
    print(celsius_100)
    print('float')

def convert_0_to_celsius():
    #converting fahrenheit to celsius
    celsius_0 = (0 - 32)*5/9
    print(celsius_0)

def convert_34_2_to_celsius():
    #converting fahrenheit to celsius in print statement
    print((34.2 - 32) * 5/9)

def convert_5_to_fahrenheit():
    #conerting from celsius to fahrenheit
    fahrenheit_conversion = (5 * 9/5) + 32
    print(fahrenheit_conversion)

def hotter_temp():
    #converting celsius to fahrenheit
    fahrenheit_conversion = (30.2 * 9/5) + 32
    fahrenheit = 85.1
    #checking the two fahrenheits against each other to find greater value
    if fahrenheit_conversion > fahrenheit:
        print('30.2 degrees celsius')
    else: print('85.1 degrees fahrenheit')

# Function to convert fahrenheit to Celsius
def convert_fahrenheit_to_celsius(num):
    celsius = float(num - 32) * 5 / 9
    return celsius

# Function to convert Celsius to fahrenheit
def convert_celsius_to_fahrenheit(num):
    fahrenheit = (float(num) * 9 / 5 + 32)
    return fahrenheit
    