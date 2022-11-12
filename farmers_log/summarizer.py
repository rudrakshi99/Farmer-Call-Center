from summarizer import Summarizer, TransformerSummarizer


def bert_summarizer(text):
    bert_model = Summarizer()
    bert_summary = bert_model(text, ratio=0.5)
    return bert_summary


def gpt_summarizer(text):
    gpt_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    gpt_summary = gpt_model(text, min_length=60)
    return gpt_summary

def xlnet_summarizer(text):
    xlnet_model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
    xlnet_summary = xlnet_model(text, min_length=60)
    return xlnet_summary
