import speech_recognition as sr
r=sr.Recognizer()

with sr.AudioFile('test.wav') as source:
    print("Listening to Audio")
    
    #capture the audio
    audio= r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("Audio:", text)
    except:
        print("Error")