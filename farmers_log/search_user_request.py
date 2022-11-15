from serpapi import GoogleSearch

from farmers_log.scrape_website import scrape_website
from farmers_log.summarize_log import xlnet_summarizer

api_key = "7b524a836388776ada58e38ae837281d7486f2b7e29348d6f97d071afe3e9ccc"


def search_log(query):
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
                'description': results["organic_results"][0]["snippet"],
                'response': xlnet_summarizer(scrape_website(results["organic_results"][0]["link"])),
                'source_description': results["organic_results"][0]['about_this_result']["source"]['description'],
            },
            "organic_result_2": {
               'title': results["organic_results"][1]["title"],
                'link': results["organic_results"][1]["link"],
                'description': results["organic_results"][1]["snippet"],
                'response': xlnet_summarizer(scrape_website(results["organic_results"][1]["link"])),
                'source_description': results["organic_results"][1]['about_this_result']["source"]['description'],
            },
            "organic_result_3": {
               'title': results["organic_results"][2]["title"],
                'link': results["organic_results"][2]["link"],
                'description': results["organic_results"][2]["snippet"],
                'response': xlnet_summarizer(scrape_website(results["organic_results"][2]["link"])),
                'source_description': results["organic_results"][2]['about_this_result']["source"]['description'],
            },
            "organic_result_4": {
                'title': results["organic_results"][3]["title"],
                'link': results["organic_results"][3]["link"],
                'description': results["organic_results"][3]["snippet"],
                'response': xlnet_summarizer(scrape_website(results["organic_results"][3]["link"])),
                'source_description': results["organic_results"][3]['about_this_result']["source"]['description'],
            },
            "organic_result_5": {
                'title': results["organic_results"][4]["title"],
                'link': results["organic_results"][4]["link"],
                'description': results["organic_results"][4]["snippet"],
                'response': xlnet_summarizer(scrape_website(results["organic_results"][4]["link"])),
                'source_description': results["organic_results"][4]['about_this_result']["source"]['description'],
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
