# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:14:04 2022

@author: Alexa
"""

class Edge:
    """Edges for Digraph"""
    
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        
    def get_source(self):
        return self.src
    
    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + ' ----> ' + self.dest.get_name()