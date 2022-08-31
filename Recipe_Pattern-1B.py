"""
    =====================================================================
    Recipe - Pattern 1B - "One-shot Window" - (Self-closing, single line)
    =====================================================================
    For a much more compact window, it's possible to create, display, read,
    and close a window in a single line of code.

    The important part of this bit of code is close=True.
    This is the parameter that instructs PySimpleGUI to close the window just before the read returns.

    This is a single line of code, broken up to make reading the window layout easier.
    It will display a window, let the user enter a value, click a button and then the window will close
    and execution will be returned to you with the variables event and values being returned.

    Notice use of Element name "Shortcuts"
    (uses B rather than Button, T instead of Text,In rather than InputText, etc.).
    These shortcuts are fantastic to use when you have complex layouts.
    Being able to "see" your entire window's definition on a single screen of code has huge benefits.
    It's another tool to help you achieve simple code.
"""
import PySimpleGUI as sg

event, values = sg.Window("Login Form",
                          [[sg.T("Username : "), sg.In(key="usr")],
                           [sg.Submit(), sg.Cancel()]]).read(close=True)
user_name = values['usr']

log_entry = "User " + user_name + " logged in just now.\n"
print(log_entry)
f = open("log1B.txt", 'a+')
f.write(log_entry)
f.close()
