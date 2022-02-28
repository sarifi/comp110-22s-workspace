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
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print