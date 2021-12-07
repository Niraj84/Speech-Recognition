import speech_recognition as sr
r=sr.Recognizer()

while True:
    with sr.Microphone() as source:
        #clear background Noise
        r.adjust_for_ambient_noise(source,duration=0.1)

        print("Speack Now")
        #capture the audio
        audio= r.listen(source)
        try:
            text=r.recognize_google(audio)
            print("Speaker:", text)
            if text=='quit':
                break
        except:
            print("Please say again!!")