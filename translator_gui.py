#!/usr/bin/python3

from googletrans import Translator
import PySimpleGUI as sg


def translation_google(input):
    toTranslate = input
    translator = Translator()
    result = translator.translate(toTranslate)
    print()

    return result.text


# This looks GNOME-ish
sg.theme('DarkGrey5')

layout = [
    [sg.Text(text='Input(Any Language): ', font=('', 20)),
     sg.Input(key='-INPUT-', font=('', 20), size=(20, 20))],
    [sg.Text('Output(In English): ', font=('', 20)),
     sg.Text(size=(15, 1), font=('', 20), key='-OUTPUT-')],
    [sg.Button('Translate'), sg.Button('Exit')]
     ]

window = sg.Window('Translator', layout, location=(1000, 500))

while True:
    event, values = window.read()
    print(event, values)

    translated_final = translation_google(values['-INPUT-'])
    print('Translation: ' + translated_final)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Translate':
        window['-OUTPUT-'].update(translated_final)
