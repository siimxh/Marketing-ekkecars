import pandas as pd,re,sys,collections,random
df=pd.read_pickle(sys.argv[1]); d=df[df.perimetro.str.startswith('dentro')].copy()
# use all notes of the person (all signups)
notes=df.groupby('gruppo_dup').note.agg(lambda s:' | '.join(x for x in s if x.strip()))
d['tutte_note']=d.gruppo_dup.map(notes).fillna('')
n=d.tutte_note.str.lower()
T={'budget basso / auto economica':r'budget (?:troppo )?bass|fuori budget|soldi|economic|poco prezzo|spendere poco|cheap|\b1\d[\'.]?000\b|\b[5-9][\'.]?000\b|da pochi',
'permuta / auto da dare dentro':r'permut|darla dentro|dare dentro|ritir|valutazion',
'leasing / rata mensile':r'leasing|rata|al mese|/mese|chf/m|mensil',
'leasing rifiutato / problemi finanziamento':r'rifiut|esecuzion|debit|zek|intrum|bloccato i conti|non passa',
'noleggio / long rent':r'noleggi|long rent|lungo termine|renting',
'vuole vedere/toccare, diffidenza online':r'toccar|vedere (?:l|di persona)|non vuole comprare online|online|di persona|fidarsi|fiducia|brutta esperienza|truff',
'più avanti (mesi, anno prossimo, collaudo)':r'verso |da risentire|più avanti|fra un anno|tra un anno|anno prossimo|prossimo anno|collaudo|scade|scadenza|gennaio|febbraio|marzo|aprile|maggio|giugno|settembre|estate|primavera',
'ha già comprato / trovato':r'comprat|acquistat|già trovato|gia trovato|preso (?:un|una)',
'non interessato / curioso / per sbaglio':r'non interessat|curios|per sbaglio|perditempo|cliccat|non vuole',
'per la famiglia (figli, moglie, genitori)':r'figli|moglie|marito|compagn|genitor|famiglia|madre|padre|mamma|papà',
'per lavoro / ditta':r'lavoro|ditta|impresa|azienda|artigian|cantiere|furgon|taxi|socio',
'ibrida / elettrica':r'ibrid|hybrid|elettric|plug',
'offerta di un altro / confronto prezzi':r'offerta|preventiv|confront|altro garage|concession|schiess|autoscout|ha visto',
'colore / optional precisi':r'nera|nero|bianc|grigi|color|optional|tetto|pelle|gancio|automatic|4x4|full',
'insulti / chiusure brusche':r'stronz|attacca|chiuso in faccia|chiude|spaccaminchia|maleducat|fanculo|pippone'}
rows=[]
random.seed(4)
for k,rx in T.items():
    m=n.str.contains(rx)
    ex=d[m].tutte_note.tolist(); random.shuffle(ex)
    rows.append((k,int(m.sum())))
    print(f'\n## {k}: {int(m.sum())}')
    for e in ex[:5]: print('   -',re.sub(r'\+?\d[\d\s]{7,}\d','[num]',e)[:150].replace('\n',' '))
print('\nlead con note di contenuto:',int((d.esito_contatto.str.startswith('note')).sum()))
