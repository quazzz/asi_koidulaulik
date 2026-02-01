import feedparser
from bs4 import BeautifulSoup
import re

def clean_html(raw_html):
    """Eemaldab HTML märgendid ja puhastab teksti."""
    if not raw_html: return ""
    # BeautifulSoup puhastab märgistuse
    cleantext = BeautifulSoup(raw_html, "html.parser").get_text(separator=' ')
    # Eemaldame liigse tühiku ja reavahetused
    cleantext = re.sub(r'\s+', ' ', cleantext).strip()
    # Eemaldame tüüpilise RSS "The post ... appeared first on" lõpu
    cleantext = re.sub(r'The post .* appeared first on .*', '', cleantext)
    return cleantext

def is_truly_estonian(title, summary):
    text = (title + " " + summary).lower()
    blocked = ['venemaa föderatsioon', 'kreml', 'putin', 'riigiduuma', 'valge maja', 'ukraina sõda']
    if any(word in text for word in blocked): return False
    
    anchors = ['eesti', 'tallinn', 'tartu', 'viljandi', 'pärnu', 'saaremaa', 'hiiumaa', 'laulupidu', 'erm', 'estonia', 'vanemuine', 'sirp', 'koidula', 'pärand', 'rahvakultuur', 'kirjandus', 'teater', 'näitus', 'kontsert', 'muuseum', 'kunst', 'muusika', 'arvustus', 'festival']
    return any(word in text for word in anchors)

def get_culture_data():
    feeds = [
        ('Sirp', 'https://www.sirp.ee/feed/'),
        ('ERR Kultuur', 'https://kultuur.err.ee/rss'),
        ('Teatri Agentuur', 'https://www.teater.ee/uudised/rss'),
        ('Müürileht', 'https://www.muurileht.ee/feed/'),
        ('Kultuur.ee', 'https://kultuur.ee/feed/'),
        ('Eesti Kunstnike Liit', 'https://www.eaa.ee/rss.xml'),
        ('Edasi.org', 'https://edasi.org/feed/')
    ]
    
    all_news = []
    for source_name, url in feeds:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:8]:
                title = clean_html(entry.title)
                # Puhastame sisu täielikult HTML-ist
                summary = clean_html(entry.get('summary', entry.get('description', '')))
                
                if is_truly_estonian(title, summary):
                    all_news.append({
                        'title': title,
                        'link': entry.link,
                        'source': source_name,
                        'summary': summary,
                        'date': entry.get('published', 'Hiljuti')[:16]
                    })
        except: continue
            
    import random
    random.shuffle(all_news)
    return all_news