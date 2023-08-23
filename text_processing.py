import re
from stanza import Pipeline
import sqlite3
import os

nlp = Pipeline(lang='uk', processors='tokenize,pos,lemma,mwt')

DIRECTORY_PATH = 'databases'


def generate_dictionary(dir):

    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        text = open(file_path, 'r', encoding='unicode_escape')
        text_string = text.read(300000)

        # прибрати tabs і переноси на новий рядок

        def text_processing(string):
            clean_text = re.sub('\s+', ' ', string)
            return clean_text

        new_string = text_processing(text_string)
        doc = nlp(new_string)

        # лематизація
        lemmas = [
            word.lemma for sent in doc.sentences for word in sent.words if word.text.isalpha()]

        # токенізація на речення
        sent_tokens = [sent.text for sent in doc.sentences]

        # присвоєння частин мови
        pos_tags = [
            word.upos for sent in doc.sentences for word in sent.words if word.text.isalpha()]

        # токенізація на слововживання
        word_tokens = [token.text.lower(
        ) for sent in doc.sentences for token in sent.tokens if token.text.isalpha()]

        numbers = [num+1 for num, sent in enumerate(doc.sentences)
                   for token in sent.tokens if token.text.isalpha()]

        # кортежі зі списками для бази даних

        # data1 = list(zip(range(1, len(word_tokens)+1), word_tokens, numbers))
        data2 = list(zip(range(1, len(word_tokens)+1),
                     word_tokens, lemmas, pos_tags, numbers))

        conn = sqlite3.connect(f'databases/{filename}.db')

        cur = conn.cursor()

        # cur.execute("""CREATE TABLE IF NOT EXISTS words(
        #    word_id INT PRIMARY KEY,
        #    word TEXT,
        #    sent_number INT);
        #    """)

        cur.execute("""CREATE TABLE IF NOT EXISTS word_info(
         word_id INT PRIMARY KEY,
         word TEXT,
         lemma TEXT,
         pos TEXT,
         sent_number INT);
         """)

        # cur.executemany("INSERT INTO words VALUES(?, ?, ?);", data1)

        cur.executemany("INSERT INTO word_info VALUES(?, ?, ?, ?, ?);", data2)

        conn.commit()

        conn.close()



if __name__=="__main__":
    generate_dictionary(DIRECTORY_PATH)
