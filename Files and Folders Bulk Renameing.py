# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:28:41 2020

@author: Fady_
"""   

import os
path = 'your path here'
files = os.listdir(path)


for index, file in enumerate(files):
    #for folders uncommint the next line
    #os.rename(os.path.join(path, file), os.path.join(path, ''.join(['book mockup order ' + str( 82 + index)])))
    #for file uncommint the next line and change the file extention.
    #os.rename(os.path.join(path, file), os.path.join(path, ''.join([ str( 1 + index), '.png'])))
