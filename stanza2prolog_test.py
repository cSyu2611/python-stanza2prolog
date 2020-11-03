import stanza
from word_properties import Word

if __name__ == "__main__":
    # stanza.download('en')
    nlp = stanza.Pipeline('en')
    doc = nlp("The quick brown fox jumps over the lazy dog.")
    buf = []
    for word in doc.sentences[0].words:
        word_props = Word(word)
        buf.append(word_props.get_prolog_str())

    prolog_str = "\n".join(buf)

    with open("test_prolog", "w") as f:
        f.write(prolog_str)
