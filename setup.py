from setuptools import setup
from typing import List

HYPEN_DOT_E = "-e ."

def find_packages(file_path)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [line.replace("\n","") for line in requirements]
    if HYPEN_DOT_E  in  requirements:
        requirements.remove(HYPEN_DOT_E)
        
setup(
    name = "Zomato Bangalore Restaurants",
    author = "Ayush Mehra",
    version= "0.0.0",
    packages = find_packages("requiurements.txt")
)