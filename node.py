# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:03:52 2022

@author: Alexa
"""

class Node:
    """Node For Digraph"""
    
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
        