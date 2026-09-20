# Simple Dictionary Example
# Professor Laney


# Create a dictionary of country codes and country names
countries = {
    "CA": "Canada",
    "US": "United States",
    "MX": "Mexico",
    "FR": "France",
    "JP": "Japan"
}

# Print the whole dictionary
print("Countries dictionary:")
print(countries)

print()

# Access values using keys
print("CA =", countries["CA"])
print("US =", countries["US"])

print()

# Add a new country
countries["DE"] = "Germany"

print("Updated dictionary:")
print(countries)

print()

# Loop through the dictionary
print("Country list:")

for code, country in countries.items():
    print(code, "-", country)
