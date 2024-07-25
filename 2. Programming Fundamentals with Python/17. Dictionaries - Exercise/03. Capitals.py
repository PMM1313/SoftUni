countries = input().split(", ")
capitals = input().split(", ")

country_capital_dict = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
