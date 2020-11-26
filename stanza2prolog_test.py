import stanza
from word_properties import Word

if __name__ == "__main__":
    # ↓初回のみ。2回目からは無駄なダウンロードになるのでコメントアウト
    stanza.download('en')
    nlp = stanza.Pipeline('en')
    while True:
        sent = input()
        # doc = nlp("The quick brown fox jumps over the lazy dog.")
        doc = nlp(sent)
        buf = []
        for word in doc.sentences[0].words:
            word_props = Word(word)
            buf.append(word_props.get_prolog_str())

        prolog_str = "\n".join(buf)
        prolog_str += "\n"
        prolog_str += 'is_subj_of_pred(SUBJ,PRED):-head(SUBJ_NUM,PRED_NUM),deprel(SUBJ_NUM,"nsubj"),upos(PRED_NUM,"VERB"),text(SUBJ_NUM,SUBJ),text(PRED_NUM,PRED).'

        with open("test_prolog", "w") as f:
            f.write(prolog_str)
