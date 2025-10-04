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
pprint.pprint(mass(asteroids['near_earth_objects']['2025-09-03'][0]))







def kE(astData) -> float:
    return 0.5*4*2


def impactForce(d: float) -> float : 
    return kE()/d

def mass(astData)-> float :
    d=(astData["estimated_diameter_min"]+astData["estimated_diameter_max"])/2
    r=d/2
    v=(4/3)*math.pi*r^3
    return 3300*v









