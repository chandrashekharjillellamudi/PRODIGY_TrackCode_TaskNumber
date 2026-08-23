
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


def main():
    print("Temperature Converter")
    print("Supported units: C (Celsius), F (Fahrenheit), K (Kelvin)\n")

    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid number. Please enter a numeric temperature value.")
        return

    unit = input("Enter the original unit (C/F/K): ").strip().upper()

    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"\n{value}°C is equal to:")
        print(f"  {fahrenheit:.2f}°F")
        print(f"  {kelvin:.2f}K")

    elif unit == "F":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"\n{value}°F is equal to:")
        print(f"  {celsius:.2f}°C")
        print(f"  {kelvin:.2f}K")

    elif unit == "K":
        if value < 0:
            print("Error: Kelvin temperature cannot be negative.")
            return
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"\n{value}K is equal to:")
        print(f"  {celsius:.2f}°C")
        print(f"  {fahrenheit:.2f}°F")

    else:
        print("Invalid unit entered. Please use C, F, or K.")


if __name__ == "__main__":
    main()