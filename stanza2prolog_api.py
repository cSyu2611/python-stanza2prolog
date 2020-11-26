from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyswip import Prolog
from time import sleep, time
import os
import io
import sys
import re
import random
import string
import stanza
from word_properties import Word


def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost",
    "http://localhost"
    # "https://demo-sip7map.datacradle.jp/tile/styles/basic/*.png"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stanza.download('en')
nlp = stanza.Pipeline('en')

@app.get('/')
async def main(query, text):
    query = query
    prolog = Prolog()
    doc = nlp(text)
    buf = []
    for word in doc.sentences[0].words:
        word_props = Word(word)
        buf.append(word_props.get_prolog_str())

    prolog_str = "\n".join(buf)
    prolog_str += "\n"
    # prolog_str += 'is_subj_of_pred(SUBJ,PRED):-head(SUBJ_NUM,PRED_NUM),deprel(SUBJ_NUM,"nsubj"),upos(PRED_NUM,"VERB"),text(SUBJ_NUM,SUBJ),text(PRED_NUM,PRED).'
    prolog_str += query

    queryy = query.split(":")[0]
    new_file_name = randomname(10) + ".pl"
    with open(new_file_name, mode="w") as f:
        f.write(prolog_str)
    with io.StringIO() as f:
        sys.stdout = f
        consult = prolog.consult(new_file_name)
        answer = list(prolog.query(queryy))
        sys.stdout = sys.__stdout__
    os.remove("./"+new_file_name)
    return answer
