import pandas as pd,re,sys
df=pd.read_pickle(sys.argv[1]); OUT=sys.argv[2]
lead_txt=(df.request+' '+df.answers+' '+df.form_extra).str.lower().str.replace('\xa0',' ')
BRANDS={'Mercedes':r'merced|mercedes|marcedes|metcedes|merzedes|\bamg\b|\bgl[abce]\b|\bgle\b|\bglc\b|classe [abcegs]\b|\bcla\b|\bcls\b','BMW':r'\bbmw\b|\bx[1-7]\b|serie [1-8]|\bm[2-8]\b|\b[1-8][0-9]{2}[di]\b','Audi':r'\baudi\b|\b[aq][1-8]\b|\brs ?[3-7q]|\bs[3-8]\b|\bsq[5-8]|\brsq','VW':r'\bvw\b|volkswagen|golf|tiguan|polo\b|passat|t-roc|touareg|\bid\.?[3-7]|arteon|touran|caddy|transporter|multivan','Toyota':r'toyota|yaris|rav ?4|c-?hr|corolla|aygo|land cruiser|proace|hilux','Volvo':r'volvo|\bxc ?[4-9]0|\bv[4-9]0\b','Skoda':r'skoda|kodiaq|kodiq|octavia|superb|karoq|kamiq|enyaq','Seat/Cupra':r'\bseat\b|cupra|formentor|ibiza|leon|ateca|born\b','Porsche':r'porsche|cayenne|macan|panamera|911|taycan','Ford':r'\bford\b|kuga|ranger|focus|puma|fiesta|mustang|s-max|transit','Alfa Romeo':r'alfa|giulia|stelvio|tonale|mito\b','Fiat/Jeep':r'\bfiat\b|panda|fiat 500|500[ex]\b|jeep|compass|renegade|ducato','Hyundai/Kia':r'hyundai|tucson|\bkia\b|sportage|sorento|ceed|i30|kona|karens','Range/Land Rover':r'range|land rover|defender|evoque|discovery','Tesla':r'tesla|model [3ysx]\b','Renault/Dacia':r'renault|reno |captur|clio|dacia|duster|megane|kadjar','Peugeot/Citroen':r'peugeot|citro|\b[23]008\b|\b5008\b','Nissan/Mazda/Suzuki/Mitsubishi':r'nissan|qashqai|x-?trail|mazda|cx-?\d|suzuki|jimny|vitara|swift|mitsubishi','Lexus':r'lexus','BYD/MG/cinesi':r'\bbyd\b|\bmg\b|polestar','Mini':r'\bmini\b','Opel':r'opel|corsa|astra|mokka'}
def brands(t):
    return ', '.join(b for b,rx in BRANDS.items() if re.search(rx,t))
df['marca_richiesta']=lead_txt.map(brands)
df['marca_nelle_note']=df.note.str.lower().map(brands)
BODY={'SUV/crossover':r'\bsuv\b|crossover','Berlina':r'berlina|limousine|sedan','Station wagon':r'station|kombi|\bsw\b|touring|avant','City car/compatta':r'city|compatt|kleinwagen|utilitari','Coupé/cabrio/sportiva':r'coup|cabrio|sportiv|roadster','Monovolume/7 posti':r'monovolume|7 ?posti|van\b|minivan','Furgone/commerciale':r'furgon|lieferwagen|transporter|commerciale','Elettrica/ibrida':r'elettric|ibrid|hybrid|electric'}
df['carrozzeria']=lead_txt.map(lambda t:', '.join(b for b,rx in BODY.items() if re.search(rx,t)))
def nuovo_usato(t):
    if 'km zero' in t or 'km_zero' in t or 'km0' in t: return 'KM zero'
    if re.search(r'\bnuov|\bneu\b',t): return 'Nuova'
    if re.search(r'usat|occasion|gebraucht',t): return 'Usata'
    return ''
df['nuova_usata']=lead_txt.map(nuovo_usato)
def timing(t):
    if re.search(r'subito|entro_?\s?1 mese|entro 30 giorni|entro_30|sofort|nächsten_30|naechsten_30|n.chsten_30',t): return 'entro 1 mese'
    if re.search(r'entro_?\s?3 mesi|entro_3_mesi|2-3 mesi|2–3_mesi|2–3 mesi|entro_2',t): return '1-3 mesi'
    if re.search(r'6 mesi|entro_6',t): return '3-6 mesi'
    if re.search(r'sto_?\s?valutando|sto_solo_valutando|non_so|non so|informiere|guardando',t): return 'sto valutando / non so'
    return ''
df['tempistica']=lead_txt.map(timing)
def money(s):
    s=s.replace("'",'').replace('’','')
    m=re.findall(r'(\d+(?:[.,]\d{3})*(?:[.,]\d+)?)\s*(k)?',s)
    out=[]
    for n,k in m:
        n=n.replace('.','').replace(',','') if re.search(r'[.,]\d{3}\b',n) else n.replace(',','.')
        try: v=float(n)
        except: continue
        if k: v*=1000
        out.append(v)
    return out
def budget(r):
    t=(r.answers+' '+r.form_extra).lower().replace('\xa0',' ')
    m=re.search(r'(budget indicativo\?|budget hai previsto\?.*?\)|fascia di prezzo.*?30.000\.:|budget\?:)\s*([^?]*?)(?:\s{2}|\s-\s|\n|che tipo|hai un|$)',t)
    src=m.group(2) if m else r.budget.lower()
    if not src.strip(): return '',''
    if re.search(r'meno.{0,4}20|unter',src): return 'meno di 20k',src
    if re.search(r'meno.{0,4}30',src): return 'meno di 30k',src
    if re.search(r'oltre|più di|über|ber_chf_50|ber chf 50',src): return 'oltre 50k',src
    vals=money(src)
    if not vals: return 'n/d',src
    v=max(vals)
    if re.search(r'mese|monat|woche|/m',src) or v<2000: return 'rata mensile',src
    if v<20000: return 'meno di 20k',src
    if v<30000: return '20-30k',src
    if v<=50000: return '30-50k',src
    return 'oltre 50k',src
b=df.apply(budget,axis=1); df['budget_fascia']=[x[0] for x in b]; df['budget_testo']=[x[1] for x in b]
def permuta(t):
    if re.search(r"permutare\?\s*(sì|si)|ho un usato da permutare|offerta bassa permuta\?: (sì|si)",t): return 'sì'
    if re.search(r"permutare\?\s*no|non_ho_auto_da_vendere|no usato",t): return 'no'
    return ''
df['permuta']=lead_txt.map(permuta)
def info_level(r):
    BR=r'mercedes|merced\w*|marcedes|metcedes|merzedes|bmw|audi|vw|volkswagen|toyota|volvo|skoda|seat|cupra|porsche|ford|alfa|romeo|fiat|jeep|hyundai|kia|range|land|rover|tesla|renault|reno|dacia|peugeot|citroen|nissan|mazda|suzuki|mitsubishi|lexus|byd|mg|mini|opel|benz|usata|nuova|km|zero|auto'
    rest=[t for t in re.findall(r'[a-z0-9\-]{2,}',r.request.lower()) if not re.fullmatch(BR,t)]
    if r.marca_richiesta and rest: return 'A modello specifico'
    if r.marca_richiesta: return 'B solo marca'
    if r.carrozzeria or r.budget_fascia or r.tempistica: return 'C tipo/budget/tempi, senza auto'
    if r.answers.strip(): return 'D solo risposte "psicologiche"'
    return 'E solo contatto'
df['livello_info']=df.apply(info_level,axis=1)

# ---- perimetro
# Decisioni di Simone/Loris sui casi singoli (21/11), per foglio e riga del file originale
OVERRIDE_DENTRO={('Leads Auto DE (FEBBRAIO)',35):'form in tedesco ma comune italofono (Poschiavo): dentro per decisione del 21/11'}
# Hanno scritto "Disiscriviti" nelle chat WhatsApp di maggio 2026 (letto nelle chat il 21/11): fuori, per tutte le loro iscrizioni
DISISCRITTI={('Modulo Prezzo IT-IT',59),('Prezzo Basso Timing',105),('Prezzo Basso Timing',110),('Prezzo Basso Timing',115),
             ('Prezzo Basso Timing',168),('Prezzo Basso Timing',199),('Prezzo Basso Timing',247)}
GRUPPI_DISISCRITTI=set(df[[ (a,b) in DISISCRITTI for a,b in zip(df.sheet,df.row)]].gruppo_dup)
def perimetro(r):
    if r.record_principale and r.gruppo_dup in GRUPPI_DISISCRITTI: return 'fuori','ha chiesto la disiscrizione su WhatsApp (maggio 2026)'
    if (r.sheet,r.row) in OVERRIDE_DENTRO and r.record_principale: return 'dentro',OVERRIDE_DENTRO[(r.sheet,r.row)]
    if not r.record_principale: return 'fuori','duplicato (tenuto il record più recente)'
    if r.tel_tipo in ('mancante_o_errore','formato_non_valido'): return 'fuori','telefono mancante o illeggibile nel file'
    if r.esito_contatto=='numero non valido': return 'fuori','numero non valido (dalla nota)'
    if r.lingua_nota.startswith('parla tedesco'): return 'fuori','parla tedesco (dalla nota del consulente)'
    if r.lingua_form=='DE': return 'fuori','form in tedesco, nessuna risposta in italiano'
    if r.tel_tipo=='CH_fisso': return 'dentro (solo chiamata)','numero fisso: niente WhatsApp'
    return 'dentro',''
p=df.apply(perimetro,axis=1); df['perimetro']=[x[0] for x in p]; df['motivo_perimetro']=[x[1] for x in p]
# age
ref=pd.Timestamp('2026-11-21')
df['eta_giorni']=(ref-pd.to_datetime(df.data)).dt.days
df.to_pickle(OUT)
print(df.perimetro.value_counts().to_dict()); print(df.motivo_perimetro.value_counts().to_dict())
d=df[df.perimetro.str.startswith('dentro')]
for c in ['livello_info','budget_fascia','tempistica','nuova_usata','permuta','esito_contatto']: print(c,d[c].value_counts().to_dict())
print(d.marca_richiesta.str.split(', ').explode().value_counts().head(15).to_dict())
print(d.carrozzeria.str.split(', ').explode().value_counts().to_dict())
# ---- regione (euristica sul campo città)
TI=r'lugano|bellinzona|locarno|mendrisio|chiasso|giubiasco|biasca|airolo|faido|ticino|tessin|massagno|paradiso|minusio|ascona|losone|stabio|balerna|novazzano|morbio|vacallo|caslano|agno|bioggio|savosa|arbedo|castione|gordola|tenero|cadenazzo|camorino|sementina|monte carasso|coldrerio|riva san vitale|capriasca|tesserete|melide|bissone|maroggia|ponte tresa|magliaso|sorengo|breganzona|canobbio|porza|cadempino|lamone|taverne|torricella|rivera|bironico|antonino|claro|lodrino|osogna|cugnasco|muralto|orselina|brissago|verscio|avegno|maggia|cevio|pregassona|viganello|cassarate|molino nuovo|gravesano|manno|vezia|cureglia|comano|canobbio|pazzallo|grancia|collina d.oro|montagnola|gentilino|muzzano|neggio|vernate|pura|curio|novaggio|sessa|astano|croglio|monteggio|bedano|mezzovico|sigirino|isone|medeglia|gudo|gnosca|preonzo|moleno|personico|bodio|giornico|pollegio|malvaglia|acquarossa|blenio|olivone|semione|ludiano|serravalle|quinto|ambri|piotta|bedretto|chironico|lavertezzo|vogorno|vira|magadino|gambarogno|contone|quartino|s\. ?antonino|sant antonino|genestrerio|ligornetto|rancate|besazio|arzo|meride|tremona|salorino|castel san pietro|caneggio|bruzella|muggio|sagno|pedrinate|seseglio|corteglia|ponte capriasca|origlio|lopagno|roveredo|grono|mesocco|soazza|lostallo|cama|leggia|verdabbio|san vittore|poschiavo|brusio|bregaglia|castasegna|vicosoprano|calanca|arvigo|cerentino|bosco gurin|brione|tegna|cavigliano|intragna|golino|ronco|ascona|frasco|sonogno|mergoscia|contra|cugnasco|gerra|riazzino|lodano|someo|giumaglio|coglio|aurigeno|moghegno|gordevio|lavizzara|peccia|fusio|campo|cimalmotto|centovalli|palagnedra|camedo|onsernone|russo|vergeletto|cadro|davesco|soragno|villa luganese|sonvico|dino|carona|morcote|vico morcote|brusino|melano|arogno|rovio|maroggia|mendrisiotto|luganese|chiasso|cresciano|gorduno|agra\b|iragna|bodio|sobrio'
def regione(r):
    c=r.city.lower()
    if re.search(TI,c) or re.search(r'\b6[5-9]\d\d\b',c): return 'Ticino / Grigioni IT'
    if re.search(r'italia|italy|como\b|milano|varese|\bcomo|sondrio|lecco|novara|torino|rom[ae]\b|roma\b|napoli|salerno|torre del greco|bergamo|brescia|palermo|bari\b|catania|sicilia|calabria|puglia',c): return 'Italia'
    if re.search(r'gen[eè]v|lausanne|losanna|fribourg|friburgo|sion|neuch|montreux|vevey|nyon|yverdon|martigny|monthey|bulle|delémont|delemont|sierre|collombey|veytaux|morges|renens|carouge|vernier|lancy|meyrin|crans|chaux|crissier|lucens|ginevra|bienne|pully|ecublens|prilly|payerne|aigle|gland|rolle|vernayaz|conthey|savièse|fully|saxon|riddes|nendaz|valais|vaud',c): return 'Romandia (francese)'
    if not c.strip(): return 'n/d'
    return 'Svizzera tedesca / altro'
df['regione']=df.apply(regione,axis=1)
df.to_pickle(OUT)
d=df[df.perimetro.str.startswith('dentro')]
print(d.regione.value_counts().to_dict())
print(pd.crosstab(d.campagna,d.regione).to_string())
