from googletrans import Translator

translator = Translator()


def Translate(message):
    try:
        translated = translator.translate(message, dest="en")
        return translated.text
    except Exception as e:
        print(e)
        return "Error"
