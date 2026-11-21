import pandas as pd,re,sys
df=pd.read_pickle(sys.argv[1]); OUT=sys.argv[2]
d=df[df.perimetro.str.startswith('dentro')].copy()
# (regex, nome da mostrare, articolo, economica?)
M=[(r'\ba ?1\b','Audi A1','una',1),(r'kia rio|\brio\b','Kia Rio','una',1),(r'proceed|\bceed','Kia ProCeed','una',1),(r'touran','VW Touran','una',0),(r'\beos\b','VW Eos','una',0),
 (r'\ba ?(180|200|220|250)e?\b|a class','Mercedes Classe A','una',0),(r'\bb ?(180|200|220|250)|class[ea] b\b','Mercedes Classe B','una',0),(r'grandland','Opel Grandland','una',0),
 (r'scenic','Renault Scenic','una',1),(r'kodiak','Skoda Kodiaq','una',0),(r'a6 ?allroad','Audi A6 Allroad','una',0),(r'cayen','Porsche Cayenne','una',0),(r'giula','Alfa Romeo Giulia','una',0),
 (r'\bs ?60\b','Volvo S60','una',0),(r'berlingo','Citroen Berlingo','un',1),(r'fornentor','Cupra Formentor','una',0),(r'\b124\b','Fiat 124 Spider','una',0),(r'\b992|\b991','Porsche 911','una',0),
 (r'\b([1-8])[1-6]0 ?[di]\b','BMW Serie {0}','una',0),(r'proace','Toyota Proace','un',1),(r'\b147\b','Alfa Romeo 147','una',1)]+[(r'\bglc\b','Mercedes GLC','una',0),(r'\bgle\b','Mercedes GLE','una',0),(r'\bgla\b','Mercedes GLA','una',0),(r'\bglb\b','Mercedes GLB','una',0),(r'\bgls\b','Mercedes GLS','una',0),
 (r'\bg ?63\b|classe g\b','Mercedes Classe G','una',0),(r'\bcla\b','Mercedes CLA','una',0),(r'class[ea] a\b|\ba ?180|\ba ?200','Mercedes Classe A','una',0),
 (r'class[ea] c\b|\bc ?(180|200|220|300)','Mercedes Classe C','una',0),(r'class[ea] e\b|\be ?(200|220|300|350)','Mercedes Classe E','una',0),
 (r'\brs ?q ?3|\brsq3','Audi RS Q3','una',0),(r'\brs ?q ?8|\brsq8','Audi RS Q8','una',0),(r'\bs ?q ?[578]\b','Audi SQ5/SQ7/SQ8','una',0),(r'\brs ?([3-7])\b','Audi RS{0}','una',0),
 (r'\bq ?([2-8])\b(?: ?sportback)?','Audi Q{0}','una',0),(r'\ba ?([3-8])\b(?: ?(sportback|avant|allroad))?','Audi A{0}','una',0),(r'\bs ?([3-8])\b','Audi S{0}','una',0),
 (r'\bx ?([1-7])\b','BMW X{0}','una',0),(r'\bm ?([2-8])\b','BMW M{0}','una',0),(r'serie ?([1-8])\b','BMW Serie {0}','una',0),(r'\b([1-5])[12][08][di]\b','BMW Serie {0}','una',0),
 (r'golf','VW Golf','una',0),(r'tiguan','VW Tiguan','una',0),(r't-?roc','VW T-Roc','una',0),(r'touareg|tuareg','VW Touareg','una',0),(r'passat','VW Passat','una',0),(r'\bid\.? ?([3-7])','VW ID.{0}','una',0),
 (r'transporter|trasporter|multivan|california','VW Transporter','un',0),(r'caddy','VW Caddy','un',0),(r'\bpolo\b','VW Polo','una',1),
 (r'stelvio','Alfa Romeo Stelvio','una',0),(r'giulia','Alfa Romeo Giulia','una',0),(r'tonale','Alfa Romeo Tonale','una',0),(r'mito','Alfa Romeo MiTo','una',1),
 (r'macan|meccan|maccan','Porsche Macan','una',0),(r'cayenne','Porsche Cayenne','una',0),(r'panamera','Porsche Panamera','una',0),(r'\b911\b','Porsche 911','una',0),(r'taycan','Porsche Taycan','una',0),
 (r'kodiaq|kodiq','Skoda Kodiaq','una',0),(r'octavia','Skoda Octavia','una',0),(r'superb','Skoda Superb','una',0),(r'karoq','Skoda Karoq','una',0),(r'enyaq','Skoda Enyaq','una',0),
 (r'formentor','Cupra Formentor','una',0),(r'\bborn\b','Cupra Born','una',0),(r'ateca','Cupra Ateca','una',0),(r'leon','Seat Leon','una',0),(r'tarraco','Seat Tarraco','una',0),(r'ibiza','Seat Ibiza','una',1),(r'arona','Seat Arona','una',1),
 (r'kuga','Ford Kuga','una',0),(r'ranger','Ford Ranger','un',0),(r'mustang','Ford Mustang','una',0),(r'puma','Ford Puma','una',1),(r'fiesta','Ford Fiesta','una',1),(r'focus','Ford Focus','una',1),
 (r'rav ?4','Toyota RAV4','una',0),(r'c-?hr','Toyota C-HR','una',1),(r'yaris','Toyota Yaris','una',1),(r'aygo','Toyota Aygo','una',1),(r'corolla','Toyota Corolla','una',1),(r'land ?cruiser','Toyota Land Cruiser','una',0),(r'hilux','Toyota Hilux','un',0),
 (r'xc ?90','Volvo XC90','una',0),(r'xc ?60','Volvo XC60','una',0),(r'xc ?40','Volvo XC40','una',0),
 (r'range rover sport','Range Rover Sport','una',0),(r'evoque','Range Rover Evoque','una',0),(r'velar','Range Rover Velar','una',0),(r'defender','Land Rover Defender','una',0),(r'range','Range Rover','una',0),
 (r'tesla|model ?[3ysx]\b','Tesla','una',0),(r'levante','Maserati Levante','una',0),(r'ghibli','Maserati Ghibli','una',0),(r'lexus|\brx\b','Lexus RX','una',0),
 (r'countryman','Mini Countryman','una',1),(r'\bmini\b','Mini','una',1),
 (r'tucson','Hyundai Tucson','una',0),(r'sportage','Kia Sportage','una',0),(r'sorento','Kia Sorento','una',0),
 (r'\bfiat 500|\b500\b','Fiat 500','una',1),(r'panda','Fiat Panda','una',1),(r'jeep|compass|renegade|avenger','Jeep','una',0),
 (r'captur|reno cap','Renault Captur','una',1),(r'clio','Renault Clio','una',1),(r'austral','Renault Austral','una',0),(r'arkana','Renault Arkana','una',0),(r'dacia|duster|sandero','Dacia','una',1),
 (r'jimny|jimmy','Suzuki Jimny','una',1),(r'vitara','Suzuki Vitara','una',1),(r'swift','Suzuki Swift','una',1),(r'qashqai','Nissan Qashqai','una',1),(r'x-?trail','Nissan X-Trail','una',0),
 (r'\b2008\b','Peugeot 2008','una',1),(r'\b3008\b','Peugeot 3008','una',0),(r'\b5008\b','Peugeot 5008','una',0),(r'\bbyd\b','BYD','una',0),(r'\bmg\b','MG','una',1),
 (r'corsa','Opel Corsa','una',1),(r'mokka','Opel Mokka','una',1)]
def auto(t):
    t=t.lower()
    for rx,name,art,cheap in M:
        m=re.search(rx,t)
        if m:
            g=[x for x in m.groups() if x and x.isdigit()]
            return name.format(g[0] if g else ''),art,cheap
    return '','',0
r=d.request.map(auto)
d['auto']=[x[0] for x in r]; d['articolo']=[x[1] for x in r]; d['auto_economica']=[x[2] for x in r]
# solo marca premium, senza modello riconosciuto: si usa la marca
PREMIUM={'Mercedes':'Mercedes','Audi':'Audi','BMW':'BMW','Porsche':'Porsche','Alfa Romeo':'Alfa Romeo','Volvo':'Volvo','Range/Land Rover':'Land Rover','Tesla':'Tesla','Lexus':'Lexus'}
for i in d.index:
    if not d.at[i,'auto']:
        b=[x for x in d.at[i,'marca_richiesta'].split(', ') if x]
        if len(b)==1 and b[0] in PREMIUM: d.at[i,'auto']=PREMIUM[b[0]]; d.at[i,'articolo']='una'
def con_articolo(a,art):
    if not a: return ''
    if art=='un': return 'un '+a
    if re.match(r'(Audi|Alfa)',a): return "un'"+a
    return 'una '+a
d['auto_con_articolo']=[con_articolo(a,b) for a,b in zip(d.auto,d.articolo)]
TIPO={'SUV/crossover':'un SUV','Berlina':'una berlina','Station wagon':'una station wagon','City car/compatta':'una city car','Coupé/cabrio/sportiva':'una sportiva',
 'Monovolume/7 posti':'una monovolume','Furgone/commerciale':'un furgone','Elettrica/ibrida':"un'auto ibrida o elettrica"}
def tipo(r):
    if 'Furgoni' in r.campagna: return 'un furgone'
    first=r.carrozzeria.split(', ')[0] if r.carrozzeria else ''
    t=TIPO.get(first,'')
    if t and r.nuova_usata in ('Usata','Nuova') and first not in ('Elettrica/ibrida',):
        t+=' '+('usato' if t.startswith('un ') and r.nuova_usata=='Usata' else 'usata' if r.nuova_usata=='Usata' else 'nuovo' if t.startswith('un ') else 'nuova')
    return t
d['tipo']=d.apply(tipo,axis=1)
def seg(r):
    economica = r.auto_economica or r.budget_fascia=='meno di 20k'
    if r.livello_info.startswith(('A','B')) and r.auto and not economica: return 'S1'
    if r.tipo: return 'S2'
    return 'S3'
d['segmento']=d.apply(seg,axis=1)
d['nota_segmento']=''
d.loc[d.livello_info.str.startswith(('A','B'))&(d.segmento!='S1'),'nota_segmento']=d.apply(lambda r:'auto economica o budget basso: spostato' if (r.auto_economica or r.budget_fascia=='meno di 20k') and r.auto else 'modello non riconosciuto: da controllare',axis=1)
d.to_pickle(OUT)
print(d.segmento.value_counts().to_dict())
print(d.nota_segmento.value_counts().to_dict())
print(d[d.segmento=='S1'].auto.value_counts().head(25).to_dict())
print(d[d.segmento=='S2'].tipo.value_counts().to_dict())
x=d[d.nota_segmento.str.startswith('modello')]; print(x.request.str[:40].tolist()[:40])
