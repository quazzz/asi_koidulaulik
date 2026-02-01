from sklearn.feature_extraction.text import TfidfVectorizer
import re

def extract_keywords(docs, top_n=3):
    if len(docs) < 2: return [[] for _ in docs]

    # Laiendatud STOP-sõnad, et vältida koodiprahti ja üldiseid sõnu
    EST_STOP = [
        'ja', 'ning', 'ega', 'ehk', 'või', 'aga', 'kuid', 'ent', 'sest', 'oli', 'on', 'see', 'need', 
        'kui', 'ka', 'siis', 'nii', 'et', 'vms', 'pole', 'ikka', 'juba', 'oma', 'nagu', 'mis', 'kes', 
        'mida', 'mille', 'vastu', 'läbi', 'toimus', 'vaata', 'loe', 'lisaks', 'uudised', 'teatas',
        'span', 'class', 'href', 'html', 'datetime', 'time', 'post', 'appeared', 'first', 'filmiarvustus'
    ]

    # Ainult tähed, eemaldame kõik muu (numbrid, sümbolid)
    clean_docs = [re.sub(r'[^a-zäöüõ ]', '', d.lower()) for d in docs]

    vectorizer = TfidfVectorizer(
        stop_words=EST_STOP,
        ngram_range=(1, 1), # Üksikud sõnad on selgemad
        max_df=0.7,         # Kui sõna on 70% artiklites, pole see unikaalne
        min_df=1
    )

    try:
        matrix = vectorizer.fit_transform(clean_docs)
        names = vectorizer.get_feature_names_out()
        results = []
        
        for i in range(len(clean_docs)):
            row = matrix.getrow(i).toarray()[0]
            top_ids = row.argsort()[::-1]
            
            keywords = []
            for idx in top_ids:
                word = names[idx]
                # Kontroll: sõna pikkus > 3 ja ei tohi sisaldada koodi osi
                if row[idx] > 0 and len(word) > 3 and word not in keywords:
                    keywords.append(word)
                if len(keywords) == top_n:
                    break
            results.append(keywords)
        return results
    except:
        return [[] for _ in docs]