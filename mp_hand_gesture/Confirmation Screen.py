#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:32:18 2022

@author: thiruchelvan
"""

import PySimpleGUI as sg 

# Collected information from all inputs 
collected_info = ['input 1', 'input 2', 'input 3']

# Layout for confirmation box
layout =[[sg.Listbox(values = collected_info, s=(30,10), disabled=True)],
         [sg.HorizontalSeparator()],
         [sg.Button('CONFIRM'), sg.Button('CANCEL')] ]
                 

sg.Window('CONFIRMATION',layout).read()
