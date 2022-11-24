from googletrans import Translator


def translate_text_to_language(text,lang, source_lang = 'en'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=lang, src=source_lang)
        return translation.text
    except Exception as e:
        print(e)
        return None

print(translate_text_to_language("soil type", "hi", "en"))