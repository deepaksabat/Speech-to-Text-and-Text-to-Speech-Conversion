import speech_recognition as sr

r = sr.Recognizer()

audio = 'Dil Mera Churaya Kyun  Rahul Jain  Cover  Kumar Sanu.wav'

with sr.AudioFile(audio) as source:
    print('Say Somthing')
    audio = r.record(source)
    print('done')

try:
	text = r.recognize_google(audio)
	with open('C:/Users/user/Desktop/speechtotexttexttospeech/pymp3/somefile.txt', 'a') as the_file:
		the_file.write(text)
	print('Google thinks you said:\n' + text)

except:
    pass
    
