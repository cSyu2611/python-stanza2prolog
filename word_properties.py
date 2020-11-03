class Word:
    def __init__(self, word_obj):
        self.id = word_obj.id if hasattr(word_obj, "id") else None
        self.text = word_obj.text if hasattr(word_obj, "text") else None
        self.lemma = word_obj.lemma if hasattr(word_obj, "lemma") else None
        self.upos = word_obj.upos if hasattr(word_obj, "upos") else None
        self.xpos = word_obj.xpos if hasattr(word_obj, "xpos") else None
        self.feats = word_obj.feats if hasattr(word_obj, "feats") else None
        self.head = word_obj.head if hasattr(word_obj, "head") else None
        self.deprel = word_obj.deprel if hasattr(word_obj, "deprel") else None
        self.misc = word_obj.misc if hasattr(word_obj, "misc") else None

    def print_prolog_predicate(self):
        print(f'text({self.id},"{self.text}").') if self.text != None else None
        print(
            f'lemma({self.id},"{self.lemma}").') if self.lemma != None else None
        print(f'upos({self.id},"{self.upos}").') if self.upos != None else None
        print(f'xpos({self.id},"{self.xpos}").') if self.xpos != None else None
        print(
            f'feats({self.id},"{self.feats}").') if self.feats != None else None
        print(f'head({self.id},{self.head}).') if self.head != None else None
        print(
            f'deprel({self.id},"{self.deprel}").') if self.deprel != None else None

    def get_prolog_str(self):
        buf = []
        buf.append(
            f'text({self.id},"{self.text}").') if self.text != None else None
        buf.append(
            f'lemma({self.id},"{self.lemma}").') if self.lemma != None else None
        buf.append(
            f'upos({self.id},"{self.upos}").') if self.upos != None else None
        buf.append(
            f'xpos({self.id},"{self.xpos}").') if self.xpos != None else None
        buf.append(
            f'feats({self.id},"{self.feats}").') if self.feats != None else None
        buf.append(
            f'head({self.id},{self.head}).') if self.head != None else None
        buf.append(
            f'deprel({self.id},"{self.deprel}").') if self.deprel != None else None
        return "\n".join(buf)
