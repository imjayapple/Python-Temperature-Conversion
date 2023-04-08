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

    # If-Else block, pass the user input to the proper function, print the result

    if unit == 'C':
        converted_value = celsius_to_fahrenheit(temp_value)
        print(f"\n{temp_value}° Celsius is equal to {converted_value:.2f}° Fahrenheit.")
    else:
        converted_value = fahrenheit_to_celsius(temp_value)
        print(f"\n{temp_value}° Fahrenheit is equal to {converted_value:.2f}° Celsius.")

if __name__ == "__main__":
    main()