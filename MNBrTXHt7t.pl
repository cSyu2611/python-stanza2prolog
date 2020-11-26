text(1,"I").
lemma(1,"I").
upos(1,"PRON").
xpos(1,"PRP").
feats(1,"Case=Nom|Number=Sing|Person=1|PronType=Prs").
head(1,2).
deprel(1,"nsubj").
text(2,"like").
lemma(2,"like").
upos(2,"VERB").
xpos(2,"VBP").
feats(2,"Mood=Ind|Tense=Pres|VerbForm=Fin").
head(2,0).
deprel(2,"root").
text(3,"him").
lemma(3,"he").
upos(3,"PRON").
xpos(3,"PRP").
feats(3,"Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs").
head(3,2).
deprel(3,"obj").

is_subj_of_pred(SUBJ, PRED) :- head(SUBJ_NUM, PRED_NUM), deprel(SUBJ_NUM, “nsubj”), upos(PRED_NUM, “VERB”), text(SUBJ_NUM, SUBJ), text(PRED_NUM, PRED).