import pandas as pd,re,sys,random
from openpyxl import Workbook
from openpyxl.styles import PatternFill,Font,Alignment
from openpyxl.utils import get_column_letter
df=pd.read_pickle(sys.argv[1]); CSV=sys.argv[2]; XLSX=sys.argv[3]
prob=pd.read_pickle(sys.argv[1].replace('final.pkl','cls_prob.pkl'))
def scrub(s):
    s=re.sub(r'[\w.+-]+@[\w-]+\.[\w.]+','[email]',s)
    s=re.sub(r'\+?\d[\d\s/.-]{7,}\d','[numero]',s)
    return s.replace('\n',' ').strip()
pid=df.set_index('gruppo_dup').loc[df[df.record_principale].gruppo_dup].id if False else None
princ=df[df.record_principale].set_index('gruppo_dup').id
df['id_persona']=df.gruppo_dup.map(princ)
an=pd.DataFrame({
 'id':df.id,'id_persona':df.id_persona,'record_principale':df.record_principale,'n_iscrizioni':df.n_iscrizioni,
 'campagna':df.campagna,'canale':df.canale,'foglio_origine':df.sheet,'riga_origine':df.row,
 'data':pd.to_datetime(df.data).dt.date,'data_stimata':df.data_stimata,'eta_giorni':df.eta_giorni,
 'citta':df.city.str.strip(),'regione_stimata':df.regione,'lingua_form':df.lingua_form,'lingua_da_nota':df.lingua_nota,'tipo_telefono':df.tel_tipo,
 'richiesta':df.request.map(scrub),'risposte_form':(df.answers+' '+df.form_extra).map(scrub),'budget_testo':df.budget_testo.map(scrub),
 'budget_fascia':df.budget_fascia,'tempistica':df.tempistica,'carrozzeria':df.carrozzeria,'marca_richiesta':df.marca_richiesta,'marca_nelle_note':df.marca_nelle_note,
 'nuova_usata':df.nuova_usata,'permuta':df.permuta,'livello_info':df.livello_info,'scoring':df.scoring,'chat_presente':df.chat.str.strip()!='',
 'consulente':df.consultant,'note_consulente':df.note.map(scrub),'stato_colore':df.stato_colore,'colore_cella_note':df.colore_note,
 'esito_contatto':df.esito_contatto,'tentativi_x':df.tentativi_x,'flag_interessato':df.interessato_flag,'flag_valido':df.f_valido.str.strip()!='',
 'flag_offerta':df.f_offerta.str.strip()!='','flag_concluso':df.concluso,'nota_comprato_altrove':df.ha_comprato_altrove,
 'nota_non_interessato':df.non_interessato,'nota_budget_basso':df.budget_basso,'perimetro':df.perimetro,'motivo_perimetro':df.motivo_perimetro})
STOP={'auto','audi','golf','mini','nuova','usata','chur','erbil'}
for i,n in enumerate(df.name):
    for tok in re.findall(r'[A-Za-zÀ-ÿ]{3,}',n):
        if tok.lower() in STOP: continue
        for c in ['richiesta','risposte_form','note_consulente','budget_testo']:
            an.iat[i,an.columns.get_loc(c)]=re.sub(r'\b'+re.escape(tok)+r'\b','[nome]',an.iat[i,an.columns.get_loc(c)],flags=re.I)
an.to_csv(CSV,index=False)

# ---------------- XLSX per Loris
wb=Workbook(); B=Font(bold=True); W=Alignment(wrap_text=True,vertical='top')
def sheet(title,headers,rows,widths):
    ws=wb.create_sheet(title); ws.append(headers)
    for c in ws[1]: c.font=B; c.fill=PatternFill('solid',fgColor='FFDDE6F5')
    for r in rows: ws.append(r)
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=W
    ws.freeze_panes='A2'; return ws
ws=wb.active; ws.title='Leggimi'
for line in ['Revisione inventario lead – per Loris (e Simone)','',
 'Cosa serve: correggere le mie ipotesi su colori, codici e casi dubbi. Scrivi nelle colonne gialle.',
 'Il file originale contiene 1.689 righe in 19 fogli (+ 1 foglio vuoto e il foglio KPI).',
 'Ogni lead ha un ID (L0001…). "Foglio" e "riga" ti portano alla riga esatta nel file originale.',
 'Tab: 1) Legenda colori  2) Codici note  3) Domande  4) Casi da verificare  5) Esempi per colore',
 'Questo file contiene nomi: NON va nel repo.']:
    ws.append([line])
ws['A1'].font=Font(bold=True,size=14); ws.column_dimensions['A'].width=110
YEL=PatternFill('solid',fgColor='FFFFF59D')
HYP={'ELIMINATO':'Lead scartato (non interessato, budget basso, perditempo…). NB: per la riattivazione si ricontatta comunque, tranne i numeri non validi',
 'INTERESSATO':'Lead interessato, con conversazione avviata','POSTICIPATO':'Da risentire più avanti (le note riportano un mese)','PASSATO':'Passato a un altro consulente (Simone?)',
 'DOPPIO':'Secondo la legenda è "Doppio", ma la nota dice "No Soldi": colore usato a caso?',
 '(bianco: nessuno stato)':'Nessuno stato assegnato: o mai lavorato o lavorato solo con codici nelle note (X1, WA…)','(nessun colore)':'Come il bianco',
 '? rosso (fuori legenda)':'Numero non valido / non funziona (lo dicono quasi tutte le note)',
 '? grigio chiaro su tutto il foglio (fuori legenda)':'Interi fogli 29MAG, 15MAG, 21OTT, 26OTT, tutti dello stesso grigio e SENZA NOTE. Importati in blocco? Lavorati altrove (GoHighLevel)?',
 '? arancione (fuori legenda)':'In 25FEB solo su lead con "X1": primo tentativo fallito?','? verde acceso (fuori legenda)':'Lead arrivati alla fase leasing / offerta',
 '? grigio chiarissimo (fuori legenda)':'Solo foglio Furgoni IT: lavorato/chiuso?','? colore tema (fuori legenda)':'Misto: numeri non funzionanti e "non ha soldi"'}
rows=[]
for (col,f),g in df.groupby(['stato_colore','fill']):
    rows.append([f,col,'cella del nome',len(g),', '.join(f'{k} ({v})' for k,v in g.campagna.value_counts().items()),HYP.get(col,'Non so: colore raro, vedi esempi nel tab 5'),'',''])
for f,g in df[df.fill_obs.isin(['FF00FFFF','FFFF9900'])].groupby('fill_obs'):
    rows.append([f,'(solo cella Osservazioni)','cella delle note',len(g),', '.join(f'{k} ({v})' for k,v in g.campagna.value_counts().items()),
      'Azzurro: lead passato a GoHighLevel (spesso la nota dice solo "CRM", spesso è vuota)' if f=='FF00FFFF' else 'Arancione: "CRM" o "X1"','',''])
ws=sheet('1 Legenda colori',['Colore','Nome nel legenda / mia etichetta','Dove','N. righe','Campagne','Mia ipotesi','Loris: giusto? (sì/no)','Loris: significato vero'],rows,[11,34,14,9,45,60,16,40])
for r in range(2,ws.max_row+1):
    f=ws.cell(r,1).value
    if f and re.fullmatch(r'FF[0-9A-F]{6}',f): ws.cell(r,1).fill=PatternFill('solid',fgColor=f)
    ws.cell(r,7).fill=YEL; ws.cell(r,8).fill=YEL
codes=[['X1 / X2 / X3 / 2X','Numero di tentativi di chiamata senza risposta',int((df.tentativi_x>0).sum())],
 ['WA','Mandato un WhatsApp (perché non rispondeva?)',int(df.note.str.contains(r'\bWA\b').sum())],
 ['CRM','Lead spostato su GoHighLevel: gli esiti successivi sono lì e non in questo file',int(df.note.str.contains('CRM').sum())],
 ['Perso','Lead perso: per quale motivo?',int(df.note.str.contains(r'\bPerso\b',case=False).sum())],
 ['Colonne Interessato / Valido / Offerta / Leasing / Vendita','Funnel: la "x" vuol dire che il lead ha raggiunto quella fase. Compilate pochissimo (1 sola Vendita in tutto il file)',int((df.f_interessato.str.strip()!='').sum())],
 ['Colonna Scoring','Che scala è? Valori da 0 a 60, molti 0 e 5',int((df.scoring.str.strip()!='').sum())],
 ['Colonna Chat','193 link a Google Doc e 224 "X". Cosa sono? Trascrizioni delle chat WhatsApp? Le posso leggere per la tappa 3 (voce dei lead)?',int((df.chat.str.strip()!='').sum())]]
ws=sheet('2 Codici note',['Codice / colonna','Mia ipotesi','N. righe','Loris: giusto? (sì/no)','Loris: significato vero'],codes,[34,80,9,16,50])
for r in range(2,ws.max_row+1): ws.cell(r,4).fill=YEL; ws.cell(r,5).fill=YEL
Q=[['Esiti in GoHighLevel','Per 4 campagne (29MAG, 15MAG, 15APR, 21OTT/26OTT: circa 250 lead) e per i lead segnati "CRM" in questo file NON c\'è nessuna nota. Gli esiti delle chiamate sono in GoHighLevel? Se sì, ci serve un export (stage della pipeline + note) per non trattarli come mai contattati.'],
 ['Clienti che hanno comprato','Nel file risulta 1 sola vendita. Quanti di questi lead hanno davvero comprato da noi? Ci serve la lista (anche solo i nomi) per il segmento "già clienti".'],
 ['Lead ottobre-novembre 2026','77 lead hanno meno di un mese (21OTT, 26OTT, 10NOV). Li state ancora lavorando? Se sì, rischiano di ricevere la riattivazione mentre li chiamate.'],
 ['Consenso WhatsApp','I lead hanno dato il consenso a ricevere messaggi WhatsApp (es. una spunta nel form Meta)? Conta per il rischio di blocco del numero (tappa 4).'],
 ['Consulenti','Nel file compaiono Valentino, Riccardo e Paolo, che nel contesto del repo non ci sono. Chi sono e sono ancora in squadra? Valentino parla tedesco? (Una nota dice "passare a Valentino perché parla solo tedesco".)'],
 ['Lead in Romandia','Circa 100 lead del perimetro sono di città francofone (Ginevra, Losanna, Sion…) ma hanno compilato il form in italiano. Li teniamo? Loris parla francese?'],
 ['Lead in Svizzera tedesca','Circa 600 lead del perimetro abitano in Svizzera tedesca ma hanno compilato in italiano (es. campagne CH-NE, IT-DE). Confermi che sono italofoni come quelli di Prezzo IT-DE?'],
 ['Date mancanti','15APR Altaprofilazione e 18APR Imprenditori hanno "[object Object]" al posto della data: ho usato la data del nome del foglio.'],
 ['Telefoni illeggibili','16 numeri sono "#ERROR!" o vuoti nel file (errore di formula del foglio). Si possono recuperare da GoHighLevel?']]
ws=sheet('3 Domande',['Tema','Domanda','Risposta di Loris'],Q,[26,110,60])
for r in range(2,ws.max_row+1): ws.cell(r,3).fill=YEL
cases=[]
for _,p in prob.iterrows():
    a,b=df.iloc[p.a],df.iloc[p.b]
    cases.append(['Possibile duplicato (stesso telefono, nome diverso)',a.id,a.sheet,a.row,a['name'],f'{b.id} · {b.sheet} r.{b.row} · {b["name"]}','Tenuti entrambi: famiglia/ditta o stessa persona?',''])
for _,r in df[df.lingua_nota!=''].iterrows():
    cases.append(['Lingua dalla nota',r.id,r.sheet,r.row,r['name'],r.note[:120],'Escluso se parla tedesco; incluso altrimenti',''])
for _,r in df[(df.lingua_form=='DE')&df.city.str.lower().str.contains('poschiavo|brusio|bregaglia|roveredo|mesocco')].iterrows():
    cases.append(['Form tedesco ma città italofona',r.id,r.sheet,r.row,r['name'],r.city,'Escluso per regola, ma forse parla italiano',''])
for _,r in df[(df.tel_tipo=='CH_fisso')&df.record_principale].iterrows():
    cases.append(['Numero fisso',r.id,r.sheet,r.row,r['name'],r.tel,'Niente WhatsApp: solo chiamata',''])
for _,r in df[df.ha_comprato_altrove&df.perimetro.str.startswith('dentro')].iterrows():
    cases.append(['Nota: ha già comprato',r.id,r.sheet,r.row,r['name'],r.note[:120],'Incluso (come deciso), da messaggio diverso?',''])
ws=sheet('4 Casi da verificare',['Tipo','ID','Foglio','Riga','Nome','Dettaglio','Cosa ho fatto','Loris: decisione'],cases,[34,8,30,6,24,60,36,30])
for r in range(2,ws.max_row+1): ws.cell(r,8).fill=YEL
random.seed(7); ex=[]
for col,g in df.groupby('stato_colore'):
    g=g[g.note!='']
    for _,r in g.sample(min(6,len(g)),random_state=1).iterrows(): ex.append([col,r.id,r.sheet,r.row,r.note[:200]])
sheet('5 Esempi per colore',['Colore','ID','Foglio','Riga','Nota del consulente'],ex,[40,8,30,6,110])
wb.save(XLSX); print('ok',len(an),len(cases))
