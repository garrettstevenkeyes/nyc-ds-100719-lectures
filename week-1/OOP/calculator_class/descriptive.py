# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Calculator:
    def __init__(self, data):
        self.data = data
        self.legth = len(data)
        self.mean = self.average()
        self.median = self.middle()
        self.variance = self._variance()
        self.stand_dev = self._stand_dev()
        
    def average(self):
        return sum(self.data)/len(self.data)
    
    def middle(self):
        sorted_list = sorted(self.data)
        if len(sorted_list) % 2:
            return sorted_list[(len(sorted_list)//2)]
        else:
            return (sorted_list[(len(sorted_list)//2)-1] + sorted_list[(len(sorted_list)//2)])/2

    def _variance(self):
        diffs = []
        for number in self.data:
            diffs.append((number - self.mean)**2)
        return sum(diffs)/len(diffs)
    
    def _stand_dev(self):
        return (self.variance ** .5)

    def add_data(self, new_data):
        return self.data.append(new_data)
    
    def remove_data(self, dropped_data):
        for figure in dropped_data:
            if figure in self.data:
                self.data.slice(figure)
                
  #  def calc_correlation(self, y):
        
    
                
#x=calculator([1,2,3,4,5])