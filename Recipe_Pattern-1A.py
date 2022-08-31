"""
    =================================================================
    Recipe - Pattern 1A - "One-shot Window" - (The Simplest Pattern)
    =================================================================
    This will be the most common pattern you'll follow if you are not using an "event loop"
    (not reading the window multiple times). The window is read and then closed.

    When you "read" a window, you are returned a tuple consisting of an event and a dictionary of values.

    The event is what caused the read to return.
    It could be a button press, some text clicked, a list item chosen, etc, or WIN_CLOSED
    if the user closes the window using the X.

    The values is a dictionary of values of all the input-style elements. Dictionaries use keys to define entries.
    If your elements do not specify a key, one is provided for you.
    These auto-numbered keys are ints starting at zero.

    This design pattern does not specify a key for the InputText element,
    so its key will be auto-numbered and is zero in this case.
    Thus the design pattern can get the value of whatever was input by referencing values[0]
"""

import PySimpleGUI as sg

layout = [[sg.Text('My One Shot Window')],
          [sg.InputText()],
          [sg.Submit(),sg.Cancel()]]

window = sg.Window('Window Title' , layout)

event , values = window.read()
window.close()

text_input = values[0]
sg.popup("You entered",text_input)