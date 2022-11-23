from serpapi import GoogleSearch

from farmers_log.scrape_website import scrape_website
from farmers_log.summarize_log import xlnet_summarizer

api_key = "7b524a836388776ada58e38ae837281d7486f2b7e29348d6f97d071afe3e9ccc"


def search_log(query):
    answers = ''
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
        answers = {
            "organic_result_1": {
               'title': results["organic_results"][0]["title"],
                'link': results["organic_results"][0]["link"],
                'response': get_response(results,1),
            },
            "organic_result_2": {
               'title': results["organic_results"][1]["title"],
                'link': results["organic_results"][1]["link"],
                'response': get_response(results,2),
            },
            "organic_result_3": {
               'title': results["organic_results"][2]["title"],
                'link': results["organic_results"][2]["link"],
                'response':get_response(results,2),
            },
            "organic_result_4": {
                'title': results["organic_results"][3]["title"],
                'link': results["organic_results"][3]["link"],
                'response': get_response(results,3),
            },
            "organic_result_5": {
                'title': results["organic_results"][4]["title"],
                'link': results["organic_results"][4]["link"],
                'response': get_response(results,4),
            },
        }
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

def get_response(results, index):
    result = scrape_website(results["organic_results"][index]["link"])
    if result == None:
        return get_description(results, index)
    return result

def get_description(results, index):
    try: 
        return results["organic_results"][index]["snippet"]
    except Exception:
        return "No answer found"