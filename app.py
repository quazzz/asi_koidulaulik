from flask import Flask, render_template
import random
from scraper import get_culture_data
from analysis import extract_keywords

app = Flask(__name__)

def get_random_quote():
    quotes = [
        "Meil aiaäärne tänavas, kui armas oli see!",
        "Eesti muld ja Eesti süda – kes neid jõuaks lahuta!",
        "Mu isamaa on minu arm, kell’ südant andnud ma.",
        "Sinu põue põhja peidaks oma kõige sügavama õnne ja mure.",
        "Töö on püha, töö on suur, töö on elu alusmüür!",
        "Üks paigake siin ilmas on, kus varju leiab vaim."
    ]
    return random.choice(quotes)

@app.route('/')
def index():
    items = get_culture_data()
    quote = get_random_quote()
    
    if items:
        # Analüüsime sisu TF-IDF-iga
        summaries = [f"{i['title']} {i['summary']}" for i in items]
        keywords_list = extract_keywords(summaries)
        for idx, item in enumerate(items):
            item['keywords'] = keywords_list[idx]
    
    return render_template('index.html', culture_items=items, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)