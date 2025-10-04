import requests
import json
import pprint

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-09-03&end_date=2025-09-3&api_key=AcOgXPIkITkvzvGku5zbqPDs3UapXRhUR7rW5Q43")
asteroids: dict = response.json()

# pprint.pprint(asteroids["near_earth_objects"])

a = [1,2,3,4]
for i in range(asteroids['element_count']):
    pprint.pprint(asteroids['near_earth_objects']['2025-09-03'][i]['absolute_magnitude_h'])


dictionary = {
    "python": 1,
    "css": 1,
    "java": 1
}
