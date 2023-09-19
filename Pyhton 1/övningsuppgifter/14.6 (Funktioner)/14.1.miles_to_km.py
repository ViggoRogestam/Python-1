def km_to_miles(dist):
    if "km" in dist.lower():
        formatted_string = dist.lower().replace('km', '')
        miles = float(formatted_string) * 0.621371
        print(f'{formatted_string.strip()} km motsvarar {miles:.2f} miles')
    else:
        return print('Error: no unit of distance in argument')


def miles_to_km(dist):
    if "miles" in dist.lower():
        formatted_string = dist.lower().replace('miles', '')
        km = float(formatted_string) * 1.60934
        print(f'{formatted_string.strip()} miles motsvarar {km:.2f} km')
    else:
        return print('Error: no unit of distance in argument')


indata = input("Ange distans > ")
if "km" in indata.lower():
    km_to_miles(indata)
elif "miles" in indata.lower():
    miles_to_km(indata)
else:
    print("Error: no valid unit of distance in input")
