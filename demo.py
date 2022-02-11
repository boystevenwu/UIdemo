import PySimpleGUI as sg
import json

layout = [[sg.Text("Current temprature       ", key='temp', justification='left')],
          [sg.Text("Last Time Used           ", key='last', justification='left')],
          [sg.Text("Schedule Your Next Shower", key='time', justification='center')],
          [sg.Input(key='INPUT')],
          [sg.Button('OK')],
          [sg.Text(size=(40, 1), key='OUTPUT')]]

window = sg.Window('The Screen', layout)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break

    f = open("data.json")
    data = json.load(f)

    window["temp"].update("Current temprature       "+str(data["temperature"]))
    window["last"].update("Last Time Used           "+str(data["last_used"])+":00")
    # if values['INPUT'] != "":
    if event == 'OK':
        window['OUTPUT'].update('You have set showertime to be ' + values['INPUT'] + ":00 !")

    window.refresh()

    data["scheduled"] = values['INPUT']
    # We can also change the current temp and last time used here
    """
    if change is True:
        data["temperature"] = new temp
        data["last_used"] = new time
    """

    with open("data.json", "w") as j:
        json.dump(data, j)

    f.close()

window.close()
