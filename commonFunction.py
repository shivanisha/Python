# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:13:47 2021

@author: Shivani Sharma 

create log file

"""

import os.path
from os import path


def logfile(msg):
    
    if path.exists("epub.log"):
        file  = open("epub.log", "a")
    else:
        file  = open("epub.log", "w+")
    
    file.write(msg)
    file.close()  


logfile("test 2 \n")