import PySimpleGUI as sg      
import requests

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [
          [sg.Text('Persistent window')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Read'), sg.Exit()],
          [sg.Column([[sg.Text(size=(37,50), key='-OUTPUT-' )]], justification='center', scrollable=True,  vertical_scroll_only=True)]
          ]
      
window = sg.Window('Window that stays open', layout, element_justification='c')      
      
while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == 'Read':
        try:
            res = requests.get(values['-IN-'])
            window['-OUTPUT-'].update(res.text)
        except:
            window['-OUTPUT-'].update("you are doing shit")

window.close()