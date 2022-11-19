from summarizer import TransformerSummarizer


def xlnet_summarizer(text):
    xlnet_model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
    xlnet_summary = xlnet_model(text, min_length=60)
    print(xlnet_summary)
    return xlnet_summary