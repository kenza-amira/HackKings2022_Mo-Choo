# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import PySimpleGUI as sg
import io
from PIL import Image
import time

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000
map_to_nums={'okay':'1', 'peace':'2', 'fist':'3', 'rock':'4', 'call me':'5', 'smile':'6', 'stop':'8', 'live long':'8','thumbs up':'9', 'thumbs down':'10', '':''}



def get_instruction_frame():
    image = Image.open('Instructions.png')
    image2 = Image.open('Act1.png')
    image.thumbnail((400,300))
    image2.thumbnail((80,80))
    bio = io.BytesIO()
    bio2 = io.BytesIO()
    image.save(bio, format="PNG")
    image2.save(bio2, format="PNG")


    layout = [
        [sg.Image(data=bio.getvalue())],
        [sg.Image(data=bio2.getvalue())],
        [sg.Button('SIGN 1 TO BEGIN', font=('Any 30'))]
    ]
    return layout


def get_x_ray_confirmation_frame():
    first_column = [
        [sg.Text('Please Confirm:', font=('Any 15'))],
        [sg.Text('- Action          :     Booking Imaging Room', font=('Any 15'))], 
        [sg.Text('- Scan Type   :     X-Ray', font=('Any 15'))],
        [sg.Button('Confirm', font=('Any 30')), sg.Button('Cancel', font=('Any 30'))]
    ]

    layout = [[sg.Column(first_column)]]
    return layout

def get_mri_confirmation_frame():
    first_column = [
        [sg.Text('Please Confirm:', font=('Any 15'))],
        [sg.Text('- Action          :     Booking Imaging Room', font=('Any 15'))], 
        [sg.Text('- Scan Type   :     MRI', font=('Any 15'))],
        [sg.Button('Confirm', font=('Any 30')), sg.Button('Cancel', font=('Any 30'))]
    ]

    layout = [[sg.Column(first_column)]]
    return layout

def get_second_frame():
    ultra_sound = '1: Ultra Sound'
    x_ray = '2: X-Ray'
    ct = '3: CT'
    mri = '4: MRI'

    second_frame = [
        [sg.Button(ultra_sound, size=(5,5), font=('Any 15'))], 
        [sg.Button(x_ray, visible=True, size=(5,5), font=('Any 15'))],
        [sg.Button(ct, size=(5,5), font=('Any 15'))], 
        [sg.Button(mri, size=(5,5), font=('Any 15'))],
        [sg.Button('Prev'), sg.Button('Home'), sg.Button('Next')]
    ]
    return second_frame


def get_first_frame():
    first_column = [
        [sg.Button('1. Check-in', size=(8,8), font=('Any 12'))], 
        [sg.Button('2. Book Doctor', size=(8,8), font=('Any 12'))],
        [sg.Button('3. Book Imaging', size=(8,8), font=('Any 12'))], 
    ]

    second_column= [
        [sg.Button('4. Equipment', size=(8,8), font=('Any 12'))],
        [sg.Button('5. Appt. Sch.', size=(8,8), font=('Any 12'))], 
        [sg.Button('6. Prescript', size=(8,8), font=('Any 12'))],
    ]

    first_frame = [
        [
            sg.Column(first_column),
            sg.VSeperator(),
            sg.Column(second_column),
        ]
    ]
    return first_frame

def get_main_interface(video_recording_layout):

    # main interface page layout - first page
    main_interface_layout = [
        [
            sg.pin(sg.Column(get_instruction_frame(), key='_instruction_frame', size=(WINDOW_WIDTH/2, WINDOW_HEIGHT), visible=True)),
            sg.pin(sg.Column(get_first_frame(), key='_first_frame', size=(WINDOW_WIDTH/2, WINDOW_HEIGHT), visible=False)),
            sg.pin(sg.Column(get_second_frame(), key='_book_imaging_frame', size=(WINDOW_WIDTH/2, WINDOW_HEIGHT), visible=False)),
            sg.pin(sg.Column(get_x_ray_confirmation_frame(), key='_x_ray_confirmation_frame', size=(WINDOW_WIDTH/2, WINDOW_HEIGHT), visible=False)),
            sg.pin(sg.Column(get_mri_confirmation_frame(), key='_mri_confirmation_frame', size=(WINDOW_WIDTH/2, WINDOW_HEIGHT), visible=False)),
            sg.VSeperator(),
            sg.Column(video_recording_layout)
        ]
    ]
    window = sg.Window("OpenCV Integration", main_interface_layout, resizable=True, location=(800, 400), size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    return window


def get_option_interface(video_recording_layout):
    options_left_layout = [
        [
            sg.Column([
                [sg.Button('11', size=(5,5), font=('Any 30'))], 
                [sg.Button('12', size=(5,5), font=('Any 30'))],
                [sg.Button('13', size=(5,5), font=('Any 30'))],
            ]),
            sg.VSeperator(),
            sg.Column([
                [sg.Button('14', size=(5,5), font=('Any 30'))], 
                [sg.Button('15', size=(5,5), font=('Any 30'))],
                [sg.Button('16', size=(5,5), font=('Any 30'))],
            ])
        ],
        [sg.Button('Prev', font=('Any 30')), sg.Button('Home', font=('Any 30')), sg.Button('Next', font=('Any 30'))]
    ]

    options_interface_layout = [
        [
            sg.Column(options_left_layout, element_justification='c'),
            sg.VSeperator(),
            sg.Column(video_recording_layout)
        ]
    ]
    window = sg.Window("OpenCV Integration", options_interface_layout, location=(800, 400), size=(1000, 600))
    return window


def get_confirmation_interface(video_recording_layout):
    collected_info = ['input 1', 'input 2', 'input 3']

    # Layout for confirmation box
    confirmation_box =[
        [sg.Listbox(values = collected_info, s=(30,10), disabled=True)],
        [sg.HorizontalSeparator()],
        [sg.Button('CONFIRM', font=('Any 30')), sg.Button('CANCEL', font=('Any 30'))]
    ]
    
    confirmation_layout = [
        [
            sg.Column(confirmation_box, element_justification='c'),
            sg.VSeperator(),
            sg.Column(video_recording_layout)
        ]
    ]

    window = sg.Window("OpenCV Integration", confirmation_layout, location=(800, 400), size=(1000, 600))
    return window


def predict_gesture(frame):
    x, y, c = frame.shape
    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print('result:', result)
    
    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print('Prediction:', prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0,0,255), 2, cv2.LINE_AA)
    
    # Show the final output
    cv2.imshow("Output", frame)

    return [frame, className]




def main():
    # sg.theme("LightGreen")
    sg.theme('LightBlue')

    video_recording_layout = [
        [sg.Image(filename="", key="-IMAGE-")]
    ]


    in_Book_imaging_room = False
    in_x_confirmation = False
    in_Instruction = True
    in_mri_confirmation = False
    in_first_frame = False

    window = get_main_interface(video_recording_layout)
    # window = get_option_interface(video_recording_layout)
    # window = get_confirmation_interface(video_recording_layout)

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()
        frame, className = predict_gesture(frame)
        
        index = map_to_nums[className]

        if(index == "1" and in_Instruction):
            window['_instruction_frame'].Update(visible = False)
            window['_first_frame'].Update(visible = True)
            in_Instruction = False
            in_first_frame = True

        elif(index == "3" and in_first_frame):
            window['_first_frame'].Update(visible = False)
            window['_book_imaging_frame'].Update(visible = True)
            in_first_frame = False
            in_Book_imaging_room = True
            print('Pressed button 1')

        elif(index == "2" and in_Book_imaging_room):
            window['_book_imaging_frame'].Update(visible = False)
            window['_x_ray_confirmation_frame'].Update(visible = True)
            in_Book_imaging_room = False
            in_x_confirmation = True
            print('Pressed button 2')

        elif(index == "10" and in_x_confirmation):
            window['_x_ray_confirmation_frame'].Update(visible = False)
            window['_book_imaging_frame'].Update(visible = True)
            in_x_confirmation = False
            in_Book_imaging_room = True
            print('Pressed button 3')

        elif(index == "4" and in_Book_imaging_room):
            window['_book_imaging_frame'].Update(visible = False)
            window['_mri_confirmation_frame'].Update(visible = True)
            in_Book_imaging_room = False
            in_mri_confirmation = True
        
        elif(index =="9" and in_mri_confirmation):
            window['_mri_confirmation_frame'].Update(visible = False)
            window['_first_frame'].Update(visible = True)
            in_mri_confirmation = False
            in_first_frame = True


        if cv2.waitKey(1) == ord('q'):
            break

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
    
    # release the webcam and destroy all active windows
    cap.release()
    cv2.destroyAllWindows()
    window.close()

main()