# Two functions for the conversion for C to F, and F to C
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# While loop to obtain a valid termperature value from the user
def main():
    print("Welcome to the Temperature Converter!")

    while True:
        try:
            temp_value = float(input("\nEnter a temperature value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # While loop to obtain the value unit of temp from the user
    while True:
        unit = input("Enter the unit of the temperature value (C for Celsius or F for Fahrenheit): ").upper()
        if unit == 'C' or unit == 'F':
            break
        else:
            print("Invalid input. Please enter either 'C' or 'F'.")