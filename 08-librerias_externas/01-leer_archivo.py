import pyttsx3

def leer(ruta:str):
    """Leer archivo en voz alta
    Arguments
        ruta {str} - Ruta dónde se encuentra el archivo que se quiere leer
    """
    mi_archivo = open(ruta,"r", encoding="utf-8")
    texto = mi_archivo.read()
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

leer("./texto_ejemplo.txt")

