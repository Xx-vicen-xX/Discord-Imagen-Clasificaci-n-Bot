import speech_recognition as speech_recog
#### V1 - función
def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-ES")
    
print("Decime algo...")
texto = speech()  
print("Texto reconocido:", texto)