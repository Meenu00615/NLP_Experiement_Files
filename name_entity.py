# -*- coding: utf-8 -*-
"""Name_Entity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HoKD4Q4N-s7fmsWmtUkK_GVXR6WaSzoT
"""

!pip install spacy
!pip install nltk
! python -m spacy download en_core_web_sm

import pandas as pd
import spacy
import requests
from bs4 import BeautifulSoup
nlp = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)

content = "Trinamool Congress leader Mahua Moitra has moved the Supreme Court against her expulsion from the Lok Sabha over the cash-for-query allegations against her. Moitra was ousted from the Parliament last week after the Ethics Committee of the Lok Sabha found her guilty of jeopardising national security by sharing her parliamentary portal's login credentials with businessman Darshan Hiranandani."

doc = nlp(content)

for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label_)

from spacy import displacy
displacy.render(doc, style="ent")

entities = [(ent.text, ent.label_, ent.lemma_) for ent in doc.ents]
df = pd.DataFrame(entities, columns=['text', 'type', 'lemma'])
print(df)