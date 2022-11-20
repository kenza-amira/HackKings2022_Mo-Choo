import io
import os
import PySimpleGUI as sg 
from PIL import Image

image = Image.open('Instructions.png')
image2 = Image.open('Act1.png')
image.thumbnail((400,300))
image2.thumbnail((80,80))
bio = io.BytesIO()
bio2 = io.BytesIO()
image.save(bio, format="PNG")
image2.save(bio2, format="PNG")


layout = [[sg.Image(data=bio.getvalue(), key="-IMAGE-")],
          [[sg.Image(data=bio2.getvalue())],[sg.Button('SIGN 1 TO BEGIN')]]]
sg.Window('APPLICATION NAME!', layout).read()