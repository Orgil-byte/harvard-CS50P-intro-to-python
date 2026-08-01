distances = {
    "japan": "1000",
    "korea": "680",
    "america": "2000"
}

def main():
    for distance in distances.values():
        print(f"{distance}km is {convert(distance)}m  from mongolia")

    for country in distances.keys():
        print(f"{country} is {distances[country]}km")  

    for keys, values in distances.items():
        print(f"{keys} is {values}km")  


def convert(value):
    return int(value) * 1000


main()