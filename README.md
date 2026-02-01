<div style="background-color: #fdfaf4; padding: 30px; border: 1px solid #d4c4a8; font-family: 'Georgia', serif; color: #2c1e1a;">

<div style="text-align: center; border-bottom: 2px solid #b5a48b; margin-bottom: 20px; padding-bottom: 10px;"> <span style="font-size: 2.5em; font-weight: bold; color: #4e342e;">Koidulauliku E-laulik</span>


<span style="font-style: italic; color: #795548;">Kureeritud Eesti kultuuripärand digitaalses ajastus</span> </div>

<div style="margin-bottom: 20px;"> <strong style="font-size: 1.2em; color: #8d6e63;">PROJEKTI EESMÄRK</strong>


Rakendus on loodud Lydia Koidula vaimule, kes on naasnud tänapäeva Eestisse. See koondab ühte kohta olulisemad kodumaised kultuuriuudised, filtreerides välja maailma poliitilise müra ja esitades info puhtal, akadeemilisel ja väärikal kujul. </div>

<div style="background-color: #ffffff; padding: 15px; border-left: 4px solid #b5a48b; margin-bottom: 20px;"> <strong style="color: #4e342e;">PÕHIFUNKTSIOONID:</strong> <ul> <li><strong>Automaatne andmekogumine:</strong> Skaneerib reaalajas 12+ Eesti usaldusväärset RSS-allikat.</li> <li><strong>Semantiline filter:</strong> Spetsiaalne algoritm tagab, et sisu keskendub ainult Eesti kultuuriruumile.</li> <li><strong>TF-IDF analüüs:</strong> Leiab igast artiklist olulisemad märksõnad, eemaldades HTML-prahi ja kordused.</li> <li><strong>Vaimusõbralik disain:</strong> Klassikaline pärgamentstiilis liides koos dünaamiliste Koidula tsitaatidega.</li> </ul> </div>

<div style="margin-bottom: 20px;"> <strong style="font-size: 1.2em; color: #8d6e63;">PAIGALDUSJUHEND</strong>


Rakenduse käivitamiseks järgige neid samme: <ol> <li>Veenduge, et süsteemis on <strong>Python 3.10+</strong>.</li> <li>Paigaldage vajalikud teegid: <code style="background: #eee; padding: 2px 5px;">pip install -r requirements.txt</code></li> <li>Käivitage server: <code style="background: #eee; padding: 2px 5px;">python app.py</code></li> <li>Liikuge brauseris aadressile: <code style="background: #eee; padding: 2px 5px;">http://127.0.0.1:5000</code></li> </ol> </div>

<div style="margin-bottom: 20px;"> <strong style="font-size: 1.2em; color: #8d6e63;">TEHNILINE VIRN (STACK)</strong> <table style="width: 100%; border-collapse: collapse; margin-top: 10px;"> <tr style="background-color: #f9f5ed;"> <td style="padding: 8px; border: 1px solid #d4c4a8;"><strong>Raamistik</strong></td> <td style="padding: 8px; border: 1px solid #d4c4a8;">Flask (Python)</td> </tr> <tr> <td style="padding: 8px; border: 1px solid #d4c4a8;"><strong>Analüütika</strong></td> <td style="padding: 8px; border: 1px solid #d4c4a8;">Scikit-learn (TF-IDF Vectorizer)</td> </tr> <tr style="background-color: #f9f5ed;"> <td style="padding: 8px; border: 1px solid #d4c4a8;"><strong>Andmetöötlus</strong></td> <td style="padding: 8px; border: 1px solid #d4c4a8;">BeautifulSoup4, Feedparser</td> </tr> </table> </div>

<div style="border-top: 1px solid #b5a48b; padding-top: 10px; font-size: 0.85em; color: #9e9e9e; text-align: center;"> Kasutatud graafika ja kood on loodud õppe-eesmärgil. Kõik uudiste autoriõigused kuuluvad algsetele väljaandjatele (ERR, Sirp, Müürileht jne). </div>

</div>
