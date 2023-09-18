def km_to_miles(dist):
    if "km" in dist:
        mph = dist * 1.60934
        print(f'{dist} km motsvarar {mph} miles')
    else:
        return None


def miles_to_km(dist):
    if "mph" in dist:
        kph = dist * 0.621371
        print(f'{dist} miles motsvarar {kph} km')
    else:
        return None
