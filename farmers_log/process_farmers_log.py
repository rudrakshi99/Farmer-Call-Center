import search_and_translate
import summarizer


def process_farmers_log(problem, lang):
    # Summarize the problem
    bert_summary = summarizer.bert_summarizer(problem)
    gpt_summary = summarizer.gpt_summarizer(problem)
    xlnet_summary = summarizer.xlnet_summarizer(problem)
    # Search for the problem
    bert_answer = search_and_translate.translate_and_search_log(bert_summary, lang)
    gpt_answer = search_and_translate.translate_and_search_log(gpt_summary, lang)
    xlnet_answer = search_and_translate.translate_and_search_log(xlnet_summary, lang)
    # Return the answers
    return bert_answer, gpt_answer, xlnet_answer


solution1, solution2, solution3 = process_farmers_log('After planting my maize for 20 days, it got attacked by pest. How can i control this', 'en')
print('Solution 1')
print(solution1)
print('Solution 2')
print(solution2)
print('Solution 3')
print(solution3)