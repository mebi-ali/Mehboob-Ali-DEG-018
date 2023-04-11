# Imports
from dataclasses import dataclass

@dataclass  
## Creating Class
class Mountain:
    name : str
    elevation : float 

## Creating Object
mountain = Mountain(name="K2", elevation=8000)

mountain = str(mountain)
print("\nObject Data:\n", mountain)
print("Type of Object : ", type(mountain))


