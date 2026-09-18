#Simple dictionary example

country_capitals = {
    "Germany": {"capital": "Berlin", "population": 83783942},
    "Canada": {"capital": "Ottawa", "population": 40097761},
    "France": {"capital": "Paris", "population": 68042500}
}

print("country Capitals:", country_capitals)
print(country_capitals["Canada"]["capital"])

country_capitals["England"] = {"capital": "London", "population": 56000000}
print(country_capitals["England"])

print("Germany" in country_capitals)
print("Spain" not in country_capitals)