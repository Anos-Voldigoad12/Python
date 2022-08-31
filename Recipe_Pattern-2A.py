"""
    ============================================================================
    Recipe - Pattern 2A - Persistent window (multiple reads using an event loop)
    ============================================================================
    The more advanced/typical GUI programs operate with the window remaining visible on the screen.
    Input values are collected, but rather than closing the window,
    it is kept visible acting as a way to both input and output information.
    In other words, a typical Window, Mac or Linux window.

    This code will present a window and will print values
    until the user clicks the exit button or closes window using an X.
"""

import PySimpleGUI as sg

sg.theme("DarkAmber")
layout = [[sg.Text("Persistent Window")], [sg.InputText(key="text")], [sg.Submit(), sg.Exit()]]
window = sg.Window("Window that stays open", layout)

while True :
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == "Exit" :
        break

window.close()
