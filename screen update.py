
import PySimpleGUI as sg

ultra_sound = '1: Ultra Sound'
x_ray = '2: X-Ray'
ct = '3: CT'
mri = '4: MRI'

first_column = [
    [sg.Button(ultra_sound, size=(5,5))], 
    [sg.Button(x_ray, size=(5,5))],
    [sg.Button(ct, size=(5,5))], 
    [sg.Button(mri, size=(5,5))],
]

layout = [
    [sg.Column(first_column),
     sg.VSeparator()]]

sg.Window('APPLICATION NAME!', layout, margins=(100,100)).read()