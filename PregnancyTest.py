import random
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Pregnancy Test')],
            [sg.Button('Check If Pregnant'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel    
        break
    if event == 'Check If Pregnant':
        if random.randrange(0,1000) == 500:
            sg.Popup('You are Pregnant', keep_on_top=True)
        else:
            sg.Popup('You are not Pregnant', keep_on_top=True)

window.close()
