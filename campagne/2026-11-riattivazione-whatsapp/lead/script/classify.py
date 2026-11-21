import pandas as pd,re,sys,unicodedata,datetime
df=pd.read_pickle(sys.argv[1]).reset_index(drop=True)
OUT=sys.argv[2]

SHORT={
 'Sito WEB':('Sito WEB','organico'),
 'Nuovo Modulo Svizzera - Profila':('10NOV Modulo Svizzera Profilante','meta'),
 '1OTTOBRE - Modulo Acquisto Auto':('1OTT Modulo Acquisto','meta'),
 '29MAGGIO - Modulo Acquisto Auto':('29MAG Modulo Acquisto','meta'),
 '21OTTOBRE - Modulo Acquisto Aut':('21OTT Modulo Acquisto','meta'),
 '26OTTOBRE - Modulo Acquisto Aut':('26OTT Modulo Acquisto','meta'),
 'Leads Imprenditori (18APRILE)':('18APR Imprenditori','meta'),
 'Lead ALTAPROFILAZIONE (15APRILE':('15APR Altaprofilazione','meta'),
 'Lead ALTAPROFILAZIONE (15MAGGIO':('15MAG Altaprofilazione','meta'),
 'Leads ALTAMENTE PROFILANTE (15M':('15MAR Altamente profilante','meta'),
 'Leads Auto ITA (25FEBBRAIO)':('25FEB Auto ITA','meta'),
 'Leads Auto DE (FEBBRAIO)':('FEB Auto DE','meta'),
 'Modulo Prezzo IT-IT':('NOV25 Prezzo IT-IT','meta'),
 'Furgoni IT':('FEB Furgoni IT','meta'),
 'Prezzo Basso Timing':('DIC25 Prezzo Basso Timing','meta'),
 'Furgoni DE':('FEB Furgoni DE','meta'),
 'Modulo RS6 DE-DE':('NOV25 RS6 DE-DE','meta'),
 'Modulo Prezzo IT-DE':('NOV25 Prezzo IT-DE','meta'),
 'Modulo Compra Online DE_DE':('NOV25 Compra Online DE-DE','meta'),
 'Modulo Sogni DE':('OTT25 Sogni (Prezzo Basso CH-NE)','meta'),
}
df['campagna']=df.sheet.map(lambda s:SHORT[s][0]); df['canale']=df.sheet.map(lambda s:SHORT[s][1])
DE_SHEETS={'Leads Auto DE (FEBBRAIO)','Furgoni DE','Modulo RS6 DE-DE','Modulo Compra Online DE_DE'}
def form_lang(r):
    if r.sheet in DE_SHEETS: return 'DE'
    if r.sheet=='Modulo Sogni DE' and r.campaign.startswith('LeadGen1125_DE'): return 'DE'
    return 'IT'
df['lingua_form']=df.apply(form_lang,axis=1)

# ---- dates
APPROX={'Lead ALTAPROFILAZIONE (15APRILE':'2026-04-15','Leads Imprenditori (18APRILE)':'2026-04-18'}
def pdate(r):
    s=r.date.strip()
    try:
        if re.match(r'\d{4}-\d\d-\d\d',s): return datetime.date.fromisoformat(s[:10]),False
        m=re.match(r'(\d{1,2})[./](\d{1,2})[./](\d{4})',s)
        if m: return datetime.date(int(m[3]),int(m[2]),int(m[1])),False
    except ValueError: pass
    if r.sheet in APPROX: return datetime.date.fromisoformat(APPROX[r.sheet]),True
    return None,True
pd_=df.apply(pdate,axis=1); df['data']=[x[0] for x in pd_]; df['data_stimata']=[x[1] for x in pd_]
# fill forward missing dates within a sheet (rows are chronological)
df['data']=df.groupby('sheet')['data'].transform(lambda s:s.ffill().bfill())

# ---- phones
def norm_phone(p):
    raw=p.strip()
    if not raw or raw.startswith('#') : return '', 'mancante_o_errore'
    d=re.sub(r'\D','',raw)
    if d.startswith('00'): d=d[2:]
    if len(d)==10 and d.startswith('0'): d='41'+d[1:]
    elif len(d)==9 and d[0] in '7': d='41'+d
    if re.fullmatch(r'417[5-9]\d{7}',d): return '+'+d,'CH_mobile'
    if re.fullmatch(r'41[1-9]\d{8}',d): return '+'+d,'CH_fisso'
    if re.fullmatch(r'393\d{8,9}',d): return '+'+d,'IT_mobile'
    if re.fullmatch(r'491[5-7]\d{8,9}',d): return '+'+d,'DE_mobile'
    if re.fullmatch(r'43[6]\d{9,11}',d): return '+'+d,'AT_mobile'
    if re.fullmatch(r'33[67]\d{8}',d): return '+'+d,'FR_mobile'
    if re.fullmatch(r'\d{10,14}',d) and not d.startswith('0'): return '+'+d,'estero_altro'
    return '+'+d if d else '', 'formato_non_valido'
pn=df.phone.map(norm_phone); df['tel']=[x[0] for x in pn]; df['tel_tipo']=[x[1] for x in pn]

# ---- notes
df['note']=(df.obs+' '+df.obs2).str.strip()
low=df.note.str.lower()
INVALID=r"sbagliat|non valid|non funzion|inesistent|collegamento non possibile|numero sbagliat|numero errat|nummero di un|numero di un|non [eè] suo il numero|non e' suo|non esiste|n\. ?non|non rintracc|non ritracc|numero non"
df['nota_numero_non_valido']=low.str.contains(INVALID)
FILL_MAP={'FF666666':'ELIMINATO','FFD9EAD3':'INTERESSATO','FFC9DAF8':'POSTICIPATO','FFFFF2CC':'PASSATO','FFCC4125':'DOPPIO',
  'FF61D836':'CONCLUSO','FFEAD1DC':'DA RIATTIVARE','FFFFFFFF':'(bianco: nessuno stato)','':'(nessun colore)',
  'FFFF0000':'? rosso (fuori legenda)','FFBDC0BF':'? grigio chiaro su tutto il foglio (fuori legenda)','FFFF9900':'? arancione (fuori legenda)',
  'FF00FF00':'? verde acceso (fuori legenda)','FFD9D9D9':'? grigio chiarissimo (fuori legenda)','theme5':'? colore tema (fuori legenda)'}
df['stato_colore']=df.fill.map(lambda f:FILL_MAP.get(f,'? %s (fuori legenda)'%f))
df['colore_note']=df.fill_obs.map(lambda f:FILL_MAP.get(f,'? %s (fuori legenda)'%f))

def attempts(s):
    xs=[int(m) for m in re.findall(r'(?:\bx\s?(\d)\b|\b(\d)\s?x\b)',s.lower()) for m in m if m]
    return max(xs) if xs else 0
df['tentativi_x']=df.note.map(attempts)
# Revisione Simone/Loris 21/11: i colori si ignorano, conta solo la nota.
# X1/X2/2X... = chiamato, mai risposto · WA = parlato su WhatsApp
WA=r"(?<!no )\b(wa|whatsapp|watsapp)\b"
NORISP=r"non ?risp|mai risp|non ha risposto|segreteria|chiude subito|no risp"
XCODE=r"\bx\s?\d\b|\b\d\s?x\b"
CODES=r'^[\s,./+-]*((x\s?\d|\d\s?x|crm|non ?risp\w*|segreteria|mail|e-mail|perso|follow-?up|followup)[\s,./+-]*)+$'
def outcome(r):
    n=r.note.strip().lower()
    if r.nota_numero_non_valido: return 'numero non valido'
    if not n: return 'nessuna nota'
    if re.search(WA,n) and not re.search(NORISP,n): return 'parlato su WhatsApp'
    if re.fullmatch(r'crm',n): return 'passato al CRM'
    if re.match(CODES,n) or ((re.search(XCODE,n) or re.search(NORISP,n)) and len(n)<60):
        return 'mai risposto'
    return 'note di contenuto (parlato o in corso)'
df['esito_contatto']=df.apply(outcome,axis=1)
df['ha_comprato_altrove']=low.str.contains(r'comprat|acquistat|ha già trovato|ha gia trovato|preso (?:un|una|la|il)|appena preso|già preso')
df['non_interessato']=low.str.contains(r'non interessat|non vuole|curios|per sbaglio|perditempo|perdi tempo|cliccato')
df['budget_basso']=low.str.contains(r'budget (?:troppo )?bass|fuori budget|no soldi|non ha soldi|pochi soldi|senza .na lira|troppo bass')
df['lingua_nota']=''
df.loc[low.str.contains(r'tedesc|deutsch|non parla (?:ne |né )?italiano|solo tedesco'),'lingua_nota']='parla tedesco'
df.loc[low.str.contains(r'frances'),'lingua_nota']='parla francese'
df.loc[low.str.contains(r'spagnol'),'lingua_nota']='parla spagnolo'
df.loc[low.str.contains(r'ingles|english'),'lingua_nota']+=' (inglese citato)'
df['concluso']=(df.f_vendita.str.strip()!='')|low.str.contains(r'venduto|ha comprato da noi|consegnat')
df['interessato_flag']=df.f_interessato.str.strip().str.lower().isin(['x','si'])

# ---- dedup
def nrm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return set(t for t in re.findall(r'[a-z]{2,}',s))
df['_tok']=df.name.map(nrm)
df['_mail']=df.email.str.strip().str.lower()
import itertools,collections
parent=list(range(len(df)))
def find(i):
    while parent[i]!=i: parent[i]=parent[parent[i]]; i=parent[i]
    return i
probabili=[]
for key in ['tel','_mail']:
    for k,idx in df.groupby(key).groups.items():
        if not k or len(idx)<2: continue
        idx=list(idx)
        for a,b in itertools.combinations(idx,2):
            same_both=bool(df.tel[a]) and df.tel[a]==df.tel[b] and bool(df._mail[a]) and df._mail[a]==df._mail[b]
            if df._tok[a]&df._tok[b] or same_both: parent[find(a)]=find(b)
            else: probabili.append((a,b,key))
df['gruppo_dup']=[find(i) for i in range(len(df))]
sizes=df.gruppo_dup.value_counts()
df['n_iscrizioni']=df.gruppo_dup.map(sizes)
# primary record: most recent date, keep notes of all
df=df.sort_values(['gruppo_dup','data'],ascending=[True,False])
df['record_principale']=~df.duplicated('gruppo_dup')
df=df.sort_index()
prob=pd.DataFrame(probabili,columns=['a','b','chiave'])
df['id']=['L%04d'%(i+1) for i in range(len(df))]
prob['id_a']=df.id.values[prob.a]; prob['id_b']=df.id.values[prob.b]
df=df.drop(columns=['_tok','_mail'])
df.to_pickle(OUT); prob.to_pickle(OUT.replace('.pkl','_prob.pkl'))
print('righe',len(df),'persone uniche',df.record_principale.sum(),'gruppi dup',(sizes>1).sum(),'dup probabili (stesso tel/mail, nome diverso)',len(prob))
print(df.tel_tipo.value_counts().to_dict())
print(df.esito_contatto.value_counts().to_dict())
print(df.lingua_form.value_counts().to_dict(), df.lingua_nota.value_counts().to_dict())
print('date mancanti',df.data.isna().sum(),'min',df.data.min(),'max',df.data.max())
