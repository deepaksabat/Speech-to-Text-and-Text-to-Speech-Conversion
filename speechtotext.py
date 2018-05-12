import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Somthing')
    audio = r.listen(source)

try:
    print("Google Thanks you said:\n" +r.recognize_google(audio))

except:
    pass
    
