# Exercise 3 : write your functions here
import json

def load_data(file_path):
    with open(file_path) as file:          # `with` closes the file for you
        return json.load(file)  
    
def count_days(data):
    return len(data)

def get_avg_temp(data, days):
    sum=0
    count=0
    
    for day in days:
        key = str(day)      #LIST ON INT ==> convert to str to search a Dict !
        if key in data:
            sum += data[key]["TEMP"]["av"]
            count += 1
            
    if count==0:
        return None
    return sum / count


def get_extreme_temp(data):
    mintemp, maxtemp=None, None
    minday,maxday=None, None            #initialize at NONE rather than 0 !! because here 0 is a value that it could take
    
    for day in data:
        if mintemp is None or data[day]["TEMP"]["mn"] < mintemp:    ## WTF !! check for none first otherwise program crashes on DAY 1
            mintemp = data[day]["TEMP"]["mn"]
            minday = int(day)
        if maxtemp is None or data[day]["TEMP"]["mx"] > maxtemp:
            maxtemp = data[day]["TEMP"]["mx"]
            maxday = int(day)
    return ((minday, mintemp), (maxday, maxtemp))
            
            
def count_by_weather(data):
    out={}
    for day in data:
        key = data[day]["Weather"]
        out[key] = out.get(key, 0) + 1                  #get(key, default) avoids += 1 and =1
    return out

def get_tallest_plants(data, top_n=2):
    out={}
    for day in data:
        result=[]
        for plant in data[day]["PLANTS"]:
            if data[day]["PLANTS"][plant] == "Tallest":
                continue                                            # SKIP if tallest key
            result.append({day : [data[day]["PLANTS"], data[day]["PLANTS"]["height_cm"] ]})    #value is a list in this Dict
            result.sort(key=lambda p: p[1], reverse=True)
            out[day] = result[:top_n]
    return out

def get_meters_by_family(data):
    out={}
    for day in data:
        for plant in data[day]["PLANTS"]:
            if data[day]["PLANTS"] == "Tallest":
                            continue
                        
            family = data[day]["PLANTS"][plant]["family"]
            out[family] = out.get(family, 0) + data[day]["PLANTS"]["height_cm"] / 100
    return out
    
def days_with_plant(data, plant_name):
    out=[]
    for day in data:
        if data[day]["PLANTS"] == plant_name:
            out.append(int(day))
        return sorted(out)