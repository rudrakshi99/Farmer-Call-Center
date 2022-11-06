from googletrans import Translator
from serpapi import GoogleSearch

api_key = "YOUR_API_KEY"


def search_and_translate(query, lang):
    search_params = {
        "q": query,
        "location": "United States",
        "hl": "en",
        "gl": "us",
        "api_key": api_key
    }
    search = GoogleSearch(search_params)
    results = search.get_dict()
    try:
        answers = (results['knowledge_graph']['answer_box']['answer'])
    except Exception:
        try:
            answers = (results['answer_box']['snippet'] +"\n" + 
            "\n".join(results['answer_box']['list']).replace('...', ''))
        except Exception:
            try:
                answers = (results['organic_results'][0]['snippet'])
            except Exception:
                answers = "No answer found"
    return answers


def translate(text, lang):
    translator = Translator()
    return translator.translate(text, dest=lang).text

def translate_and_search(query, lang):
    answers = search_and_translate(query, lang)
    return translate(answers, lang)

def translate_empty_log(lang):
    return translate("Sorry, I didnt find anything. Kindly refram your question and try again.", lang)


def translate_and_search_log(query, lang):
    if query == "":
        return translate_empty_log(lang)
    try:
        return translate_and_search(query, lang)
    except Exception:
        return translate_empty_log(lang)