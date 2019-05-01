dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
dict[10] = "ten"

var = dict.get(4)
print(var)

var = dict.items()
print(var)

var = dict.keys()
print(var)

var = dict.values()
print(var)

dict.update({11: "eleven", 12: "twelve"})
print(var)

for key in dict:
	print(key, dict[key])

for key, value in dict.items():
	print(key, value)
#########################################################
monthConversions = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may":"may",
    "jun":"june",
    "jul":"july",
    "aug":"august",
    "sep":"september",
    "oct":"october",
    "nov":"november",
    "dec":"december"
}
print(monthConversions["nov"])
print(monthConversions.get("dec"))
print(monthConversions.get("luv", "Not a valid key")) #this line has a default value
