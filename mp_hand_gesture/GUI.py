#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:38:56 2022

@author: thiruchelvan
"""

import PySimpleGUI as sg 

first_column = [
    [sg.Button('1', size=(5,5))], 
    [sg.Button('2', size=(5,5))],
    [sg.Button('3', size=(5,5))], 
    [sg.Button('4', size=(5,5))],
    [sg.Button('5', size=(5,5))]
]

second_column= [[sg.Button('6', size=(5,5))],
                [sg.Button('7', size=(5,5))], 
                [sg.Button('8', size=(5,5))],
                [sg.Button('9', size=(5,5))], 
                [sg.Button('10', size=(5,5))]
]

nav_column = [sg.Button('Prev'),
              sg.Button('Home'),
              sg.Button('Next')]

layout = [
    [sg.Column(first_column),
     sg.VSeparator(),
     sg.Column(second_column),
     sg.HSeparator(),
     sg.Column(nav_column, vertical_alignment ='bottom')]]

# margins=(100,100)
sg.Window('APPLICATION NAME!', layout).read()

