"""
    =====================================================================================================
    Recipe - Pattern 2B - Persistent window (multiple reads using an event loop + updates data in window)
    =====================================================================================================
    This is a slightly more complex, but more realistic version that reads input from the user
    and displays that input as text in the window.

    Your program is likely to be doing both of those activities so this pattern will likely be your starting point.

    To modify an Element in a window, you call its update method. This is done in 2 steps.
    First you lookup the element, then you call that element's update method
"""
import PySimpleGUI as sg

sg.theme("BluePurple")
layout = [[sg.Text("Output : "), sg.Text(size=(15, 1), key="out")], [sg.InputText(key="in")],
          [sg.Button("Show"), sg.Button("Clear"), sg.Exit()]]
window = sg.Window("Recipe Pattern 2B", layout)

while True :
    event, values = window.read()
    print(event, values)

    if event in (sg.WIN_CLOSED, "Exit") :
        break
    elif event == "Show" :
        window['out'].update(values['in'])
    elif event == "Clear" :
        window["out"].update("")
        window["in"].update("")

window.close()
