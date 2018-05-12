import speech_recognition as sr
import webbrowser as wb
import speek

r = sr.Recognizer()

with sr.Microphone() as source:
    print('please say something')
    audio = r.listen(source)
    print('done')

try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
    lang = 'en'

    speek.tts(text, lang)

    f_text = 'https://www.google.co.in/search?q=' + text
    wb.open(f_text)

except Exception as e:
    print(e)
