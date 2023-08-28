def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def ounces_to_grams(ounces):
    return ounces * 28.3495

def grams_to_ounces(grams):
    return grams / 28.3495

def gallons_to_liters(gallons):
    return gallons * 3.78541

def liters_to_gallons(liters):
    return liters / 3.78541

def cubic_inches_to_cubic_cm(cubic_inches):
    return cubic_inches * 16.387

def cubic_cm_to_cubic_inches(cubic_cm):
    return cubic_cm / 16.387

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes * 60

def days_to_hours(days):
    return days * 24

def weeks_to_days(weeks):
    return weeks * 7

def main():
    print("Bienvenido al conversor universal!")
    print("Categorías disponibles:")
    print("1. Conversiones de temperatura")
    print("2. Conversiones de longitud")
    print("3. Conversiones de peso/masa")
    print("4. Conversiones de volumen")
    print("5. Conversiones de tiempo")

    category = input("Seleccione una categoría: ")

    if category == "1":
        # ... (código anterior de conversiones de temperatura)
    elif category == "2":
        # ... (código anterior de conversiones de longitud)
    elif category == "3":
        # ... (código anterior de conversiones de peso/masa)
    elif category == "4":
        # ... (código anterior de conversiones de volumen)
    elif category == "5":
        print("Tipos de conversión de tiempo:")
        print("1. Horas a minutos")
        print("2. Minutos a segundos")
        print("3. Días a horas")
        print("4. Semanas a días")

        conversion_type = input("Seleccione un tipo de conversión: ")

        if conversion_type == "1":
            hours = float(input("Ingrese la cantidad de horas: "))
            minutes = hours_to_minutes(hours)
            print(f"{hours} horas son {minutes} minutos.")
        elif conversion_type == "2":
            minutes = float(input("Ingrese la cantidad de minutos: "))
            seconds = minutes_to_seconds(minutes)
            print(f"{minutes} minutos son {seconds} segundos.")
        elif conversion_type == "3":
            days = float(input("Ingrese la cantidad de días: "))
            hours = days_to_hours(days)
            print(f"{days} días son {hours} horas.")
        elif conversion_type == "4":
            weeks = float(input("Ingrese la cantidad de semanas: "))
            days = weeks_to_days(weeks)
            print(f"{weeks} semanas son {days} días.")
        else:
            print("Selección no válida.")
    else:
        print("Categoría no válida.")

if __name__ == "__main__":
    main()
