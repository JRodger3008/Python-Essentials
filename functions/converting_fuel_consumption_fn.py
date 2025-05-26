# 4.3.8 LAB - Converting fuel consumption.

# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.
# The functions:
#   - Are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
#   - Take one argument (the value corresponding to their names)

# Constants
MILE_IN_METERS = 1609.344       # 1 Mile in Meters
GALLON_IN_LITERS = 3.785411784  # 1 Gallon in Liters

def liters_100km_to_miles_gallon(liters):
    """
    Convert fuel consumption from liters per 100 km (L/100km) to miles per gallon (MPG).

    Args:
        liters (float): fuel consumption in liters per 100 km (L/100km).

    Returns:
        float: Equivalent fuel consumption in miles per gallon (MPG).
    """
    gallons = liters / GALLON_IN_LITERS  # Convert liters to gallons
    miles = 100 * 1000 / MILE_IN_METERS  # Convert 100 kilometers to miles
    return miles / gallons               # return MPG



def miles_gallon_to_liters_100km(miles):
    """
    Converts miles per gallon (MPG) to liters per 100 km (L/100km).
    
    Args:
        miles (float): fuel efficiency in miles per gallon (MPG).
    
    Returns:
        float: Equivalent fuel consumption in liters per 100 km (L/100km).
    """
    km_100 = miles * MILE_IN_METERS / 1000 / 100 # Convert miles to 100km
    return GALLON_IN_LITERS / km_100                       # Return L/100km


# Test cases to verify accuracy of conversions
print(liters_100km_to_miles_gallon(3.9))  # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # 7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # 10.009131205673757