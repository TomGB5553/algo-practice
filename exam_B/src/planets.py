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

def heaviest_planet(planets):
    biggest=[]
    if len(planets):
        return None
    for planet in planets:
        if planet["Mass_earth"] > biggest["Mass_earth"]:
            biggest= planet
    return biggest["Name"]

def average_distance_by_method(planets):
    counts={}
    sum={}
    for planet in planets:
        method= planet["Method"]
        sum[method] = sum.get(method,0) + planet["Distance_ly"]
        counts[method] = sum.get(method, 0) + 1
    return {method: sum[method] / counts[method] for method in sum}

def planets_between(planets, first_year, last_year):
    if len(planets)==0:
        return None
    out=[]
    for planet in planets:
        if planet["Year"]<= last_year and planet["Year"] >= first_year:
            out.append(planet["Name"])
            
    return out.sort()       #attention .sort() et pas sorted(xxx)
        
        
def insertion_sort(planets, key):
    
            