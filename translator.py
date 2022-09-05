#!/usr/bin/python3

# import googletrans
from googletrans import Translator
from deep_translator import MyMemoryTranslator, LingueeTranslator, PonsTranslator
from numpy import source
from langdetect import detect

import PySimpleGUI as sg

lang_source = ""


def translation_google(input):
    toTranslate = values['-INPUT-']
    translator = Translator()
    result = translator.translate(toTranslate)
    return result.text


def translation_myMem(input):
    src_lang = detect(input)
    myMemTranslator = MyMemoryTranslator(
        source=src_lang, target='english').translate(input)
    return myMemTranslator


def translation_Pons(input):
    src_lang = detect(input)
    ponsTrans = PonsTranslator(
        source=src_lang, target='english').translate(input)
    return ponsTrans

    # toTranslate = input('Enter text to be translated: ')
    #
    # gTranslator = Translator()
    # result = gTranslator.translate(toTranslate)

    # print('src: ' + result.src)
    # print('dest: ' + result.dest)
    # print('origin: ' + result.origin)
    # print('------TRANSLATIONS------')
    #
    # print('Google_Text: ' + result.text)


layout = [
    [sg.Text(text='Input(Any Language): ', font=('', 20)),
     sg.Input(key='-INPUT-', font=('', 20), size=(20, 20))],
    [sg.Text('Output 1 (In English): ', font=('', 20)),
     sg.Text(size=(15, 1), font=('', 20), key='-OUTPUT1-')],
    [sg.Text('Output 2 (In English): ', font=('', 20)),
     sg.Text(size=(15, 1), font=('', 20), key='-OUTPUT2-')],
    [sg.Text('Output 3 (In English): ', font=('', 20)),
     sg.Text(size=(15, 1), font=('', 20), key='-OUTPUT3-')],
    [sg.Button('Translate'), sg.Button('Exit')]
     ]

window = sg.Window('Translator', layout, location=(1000, 500))

while True:
    event, values = window.read()
    print(event, values)

    translated_google = translation_google(values['-INPUT-'])
    print('Translation1: ' + translated_google)
    translated_myMem = translation_myMem(values['-INPUT-'])
    print('Translation2: ' + translated_myMem)
    translated_Pons = translation_Pons(values['-INPUT-'])
    print('Translation3: ' + translated_Pons)

    if event == 'Translate':
        window['-OUTPUT1-'].update(translated_google)
        window['-OUTPUT2-'].update(translated_myMem)
        window['-OUTPUT3-'].update(translated_Pons)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
