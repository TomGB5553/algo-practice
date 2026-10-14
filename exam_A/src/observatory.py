import json
from typing import List

def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)

print(load_data("data/observatory.json"))
def count_nights(data):
    return len(data)

def get_avg_seeing(data, nights: List[int]):
   
    average=0
    count=0                 # not every night has observations so not included in AVG !
    for night in nights:
        key = str (night)   #ATTENTION STR NOT A DICT KEY !!
        if key in data:     #ignore nights that dont exist
            average+=data[key]["SEEING"]["av"]
    if count==0:            #AVoid dividing by 0 !
        return None
    return average/count

def get_extreme_seeing(data):
    min,max=None
    night_min, night_max= 0,0
    for night in data:
        if night["SEEING"]["mn"] < min:
            min=night["SEEING"]["mn"]
            night_min= int (night)
        if night["SEEING"]["mx"] < max:
            max=night["SEEING"]["mx"]
            night_max= int (night)
            
    return ((night_min, min), (night_max, max))

def count_by_moon_phase(data):
    output={}
    for night in data:
        if data[night]["Moon_phase"] in output:
            output[data[night]["Moon_phase"]] += 1
        else:
            output[data[night]["Moon_phase"]] = 1       #do not forget the new phase case !
    return output

def get_top_targets(data, top_n=3):
    out={}
    for night in data:
        for target in data[night]["TARGETS"]:
            list=[]
            if target != "longest":
                list.append(target, data[night]["TARGETS"][target]["minutes"])
        list.sort(key=lambda t: t[1], reverse=True)
        out[night]=list[:top_n]         #slice the first top n elements
    return out
        
        
def get_hours_by_type(data):
    out={}
    for night in data:
        for target in data[night]["TARGETS"]:
            if target=="longest":
                continue                        # CONTINUE is cool to ignore that iteration of the loop
            if target["type"] in out:
                out[target["type"]] += data[night]["TARGETS"][target]["minutes"]/60
            else:
                out[target["type"]] = data[night]["TARGETS"][target]["minutes"]/60
    return out