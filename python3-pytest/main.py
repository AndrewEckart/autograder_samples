"""
Name: <project title>
Author: <your name here>
Due Date: <due date>
Course: <coursenumber-section>

Briefly explain what this program does, and important points from
your solution to the problem being solved.
"""
from math import pi

def main():
    """
    Program starts here.
    """
    name = "Darth Vader"
    flavor = "black licorice"
    tub_diameter = 9.5
    tub_radius = tub_diameter/2
    tub_height = 11
    scoop_diameter = 2
    scoop_radius = scoop_diameter/2

    tub_volume = tub_height * pi * tub_radius**2
    scoop_volume = (4/3) * pi * scoop_radius**3
    servings = tub_volume/scoop_volume
    data = f'''Name: {name}
Flavor: {flavor}
Tub: {tub_volume}
Sphere: {scoop_volume}
Servings: {servings}
'''
    print(data)


if __name__ == "__main__":
    main()
