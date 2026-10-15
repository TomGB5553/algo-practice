# Exercise 1 : write your classes Duration and Playlist here
class Duration():
    
    def __init__(self, hours, minutes):
        total = 60 * hours + minutes
        self.hours= total // 60
        self.minutes=total % 60

    def total_minutes(self):
        return self.hours*60 + self.minutes
    
    def __repr__(self):
        return f"{self.hours}h{self.minutes:02d}"
    
    def __add__(self, other):
        return Duration(self.hours+other.hours, self.minutes+other.minutes)
        
    def __lt__(self, other):
        return self.total_minutes() < other.total_minutes()
    
    def __mul__(self, k):
        return Duration(0, self.total_minutes()*k)
    

class Playlist():
    def __init__(self, durations):
        self.durations=list(durations)            #USE LIST TO CREATE A COPY !!
    
    def total(self):
        total=Duration(0,0)
        for dur in self.durations:
            total += dur
        return total
    
    def longuest(self):
        if len(self.durations)==0:
            return None
        
        maxdur=self.durations[0]        #assigner le premier element de la liste
        
        for dur in self.durations:
            if dur > maxdur :
                maxdur = dur
        return maxdur  