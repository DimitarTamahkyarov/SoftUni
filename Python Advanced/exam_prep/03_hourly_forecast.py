def forecast(*args):
    locations = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for arg in args:
        locations[arg[1]].append(arg[0])

    for weather in locations:
        locations[weather] = sorted(locations[weather])

    result = ""

    for weather, cities in locations.items():
        for city in cities:
            result += f"{city} - {weather}\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))



