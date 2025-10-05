import requests
import json
import pprint
import math
from asteroid_methods import *


response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-09-03&end_date=2025-09-3&api_key=AcOgXPIkITkvzvGku5zbqPDs3UapXRhUR7rW5Q43")
asteroids: dict = response.json()

# pprint.pprint(asteroids["near_earth_objects"])

a = [1,2,3,4]
for i in range(asteroids['element_count']):
    #pprint.pprint(asteroids['near_earth_objects']['2025-09-03'][i]['absolute_magnitude_h'])
    ...








def kE(astData) -> float:
    
    v_impact = (float(astData["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]) ** 2 + 11.2 ** 2) ** 0.5
    
    return 0.5 * mass(astData) * v_impact**2


def convert_to_TNT(kE: float) -> float : 
    return kE/(4.184*10**9)



def mass(astData)-> float :
    d=(astData["estimated_diameter"]["meters"]["estimated_diameter_min"]+astData["estimated_diameter"]["meters"]["estimated_diameter_max"])/2
    r=d/2
    v=(4/3)*math.pi*r**3
    return 3300*v



# calculate tsunamis and earthkaque





pprint.pprint(mass(asteroids['near_earth_objects']['2025-09-03'][0]))
pprint.pprint(kE(asteroids['near_earth_objects']['2025-09-03'][0]))