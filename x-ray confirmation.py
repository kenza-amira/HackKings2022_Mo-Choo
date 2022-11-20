import PySimpleGUI as sg

first_column = [
    [sg.Text('Please Confirm:')],
    [sg.Text('- Action          :     Booking Imaging Room')], 
    [sg.Text('- Scan Type   :     X-Ray')],
    [sg.Button('Confirm'), sg.Button('Cancel')]
]

layout = [[sg.Column(first_column)]]

sg.Window('APPLICATION NAME!', layout, margins=(100,100)).read()
