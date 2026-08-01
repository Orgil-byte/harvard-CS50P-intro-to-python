def main():
    spacecraft={
        "name":"Voyager1", "distance":163,
    }

    spacecraft.update({"country": "America"})

    print(print_spacecraft(spacecraft))


def print_spacecraft(datas):
    return f"""
==========================================================  
name: {datas.get("name", "Unknown")}
distance: {datas.get("distance", "Unknown")}
country: {datas.get("country", "Unknown")}
==========================================================
        """

main()