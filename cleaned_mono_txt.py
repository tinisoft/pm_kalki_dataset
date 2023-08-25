import os

folder_path = "."  # Replace with the actual path to your folder

import spacy
from spacy.language import Language

from spacy_language_detection import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42


nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)


ret = []

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        print("read file {}".format(filename))
        with open(file_path, "r") as file:
            content = file.read()
            lines = content.split("\n")
            for line in lines:
                # Document level language detection
                #print(line)
                doc = nlp_model(line)
                language = doc._.language
                lang = language['language']
                if lang == 'ta':
                    ret.append(line)

with open("kalki.txt", "w") as out:
    out.write("\n".join(ret))
