import numpy as np 
from dataclasses import dataclass, field
from collections import defaultdict, Counter



###################
## <= python 3.9 ##
###################



@dataclass
class Memo9:
    """
    -- You have to chose one of the methods below to calculate central tendency.
    
    methods:
        mean   the average of a data set.
        median  the middle of the set of numbers.
        mode  the most common number in a data set.
        sample_var  variance of the sample
        sample_std  standard deviation of the sample
                  
    """
    method: str
    data: list = field(default_factory=list)
    
    def calculate(self):
        if self.method == "mean":
            return np.mean(self.data)
        elif self.method == "median":
            return np.median(self.data)
        elif self.method == "mode":
            counts = Counter(self.data)
            d = defaultdict(list)
            max_v = max(counts.values())
            d["count"] = max_v
            for k,v in counts.items():
                if v == max_v:
                    d["mode"].append(k)

            return {"mode":d["mode"],"count":d["count"]}
        elif self.method == "sample_var":
            sum_ = 0
            for i in self.data:
                sq = (i-np.mean(self.data))**2
                sum_ += sq
            return sum_/(len(self.data)-1)
        elif self.method == "sample_std":
            sum_ = 0
            for i in self.data:
                sq = (i-np.mean(self.data))**2
                sum_ += sq
            return np.sqrt(sum_/(len(self.data)-1)) 
        
        else:
            print("You must enter a valid method!")

####################
## >= python 3.10 ##
####################
@dataclass
class Memo10:
    """
    -- You have to chose one of the methods below to calculate central tendency.
    
    methods:
        mean   the average of a data set.
        median  the middle of the set of numbers.
        mode  the most common number in a data set.
                  
    """
    method: str
    data: list = field(default_factory=list)
    
    def calculate(self):
        match self.method:
            case "mean":
                return np.mean(self.data)
            case "median":
                return np.median(self.data)
            case "mode":
                counts = Counter(self.data)
                d = defaultdict(list)
                max_v = max(counts.values())
                d["count"] = max_v
                for k,v in counts.items():
                    if v == max_v:
                        d["mode"].append(k)

                return {"mode":d["mode"],"count":d["count"]}
            case "sample_var":
                sum_ = 0
                for i in self.data:
                    sq = (i-np.mean(self.data))**2
                    sum_ += sq
                return sum_/(len(self.data)-1)
            case "sample_std":
                sum_ = 0
                for i in self.data:
                    sq = (i-np.mean(self.data))**2
                    sum_ += sq
                return np.sqrt(sum_/(len(self.data)-1))        
            case _:
                print("You must enter a valid method!")
        
