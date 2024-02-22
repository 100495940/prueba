"""
Created by Álvaro Retana 
Universidad Carlos III de Madrid
"""
from circle import Circle

class myTest:

    def calculate_area_test(self):
        obj = Circle()
        assert (obj.radius(2, 5) == 1, 'messages')