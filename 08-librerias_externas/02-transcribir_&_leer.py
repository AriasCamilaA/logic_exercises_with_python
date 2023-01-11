import pyttsx3
import speech_recognition as sr 

def escribir_leer():
    """Escribe por consola lo que se dice por micrófono, y luego lo lee
    """
    # obtener audio del micrófono                                                                       
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Dí algo:")                                                                                   
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio,"es-ES")
        print("Dijiste: " + texto)
    except sr.UnknownValueError:
        print("No se pudo escuchar")
    except sr.RequestError as e:
        print("No se pudo solicitar el audio; {0}".format(e))
    
    try:
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
    except:
        print("No puedo repetir, no entendì")
    

escribir_leer()

