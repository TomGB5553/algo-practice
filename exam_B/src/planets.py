# Exercise 3 : write your functions here
import csv

def load_planets(path):
    planets=[]
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            planets.apend({
                "Name":row["Name"],
                "Year": int(row["Year"]),
                "Distance_ly": float(row["Distance_ly"]),
                "Mass_earth": float(row["Mass_earth"]),
                "Method": row["Method"],  
            })
    return planets

def count_by_methods(planets):
    out={}
    for planet in planets:
        if planet["Method"] in out:
            out[planet] += 1
        else:
            out[planet] = 1
    return out