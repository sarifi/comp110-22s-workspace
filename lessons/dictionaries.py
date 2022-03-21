"""Demonstration of dictionary capabilities."""


# Declare the type of dictionary 
school: dict[str, int] 

# Initilaize to an empty dictionary 
schools = dict() 

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150


# Print a dictionary literal representation 
print(schools) 

# Acess a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value by its key -- "lookup"
# by its key. 
schools.pop("Duke")


# Test for the existance of a key
if "Duke" in schools: 
    print("Found the key 'Duke' in schools")
else: 
    print("No key 'Duke' in schools") 

# Update / Reassign a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] +=  200 

# print(schools["UNCC"])

schools = {} 
print(schools)

schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# print(schools["UNCC"])

for school in schools: 
    print(f"key: [school] -> Value: {schools[school]}") 