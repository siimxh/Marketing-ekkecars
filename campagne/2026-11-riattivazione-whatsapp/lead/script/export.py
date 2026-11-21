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
 'consulente':df.consultant,'note_consulente':df.note.map(scrub),
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

# ---------------- XLSX per Loris (versione semplice, dopo la revisione del 21/11)
wb=Workbook(); B=Font(bold=True); W=Alignment(wrap_text=True,vertical='top'); YEL=PatternFill('solid',fgColor='FFFFF59D')
def sheet(title,headers,rows,widths,ans_cols):
    ws=wb.create_sheet(title); ws.append(headers)
    for c in ws[1]: c.font=B; c.fill=PatternFill('solid',fgColor='FFDDE6F5')
    for r in rows: ws.append(r)
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=W
        for j in ans_cols: row[j-1].fill=YEL
    ws.freeze_panes='A2'; return ws
ws=wb.active; ws.title='Leggimi'
for line in ['Domande ancora aperte – lead riattivazione (versione 2)','',
 'Revisione già applicata: X = chiamato, mai risposto · WA = parlato su WhatsApp · colori ignorati, conta solo la nota.',
 'Qui restano solo le cose che non posso decidere io. Scrivete nelle celle gialle.',
 'Il file contiene nomi: NON va nel repo.']: ws.append([line])
ws['A1'].font=Font(bold=True,size=14); ws.column_dimensions['A'].width=110
Q=[['Calendario','Avete deciso 5 messaggi, circa 1 a settimana. Partendo lunedì 23/11 l\'ultimo cade intorno al 21/12, mentre nel brief la sequenza finiva il 12/12 e Hamza diceva "tutto prima del 20 dicembre". Teniamo 1 a settimana (e l\'ultimo messaggio slitta o diventa di gennaio) o stringiamo a circa 2 a settimana per chiudere prima di Natale?'],
 ['Valuta e prezzo GoHighLevel','In attesa della risposta che avete chiesto: dollari o franchi, e quanto costa un messaggio marketing verso un numero svizzero.'],
 ['Tempo di Loris','Per il costo pieno: quanti minuti in media per ogni lead che risponde, e quanti lead (storicamente) arrivano a offerta e a vendita.'],
 ['Nota "CRM"','27 lead hanno solo "CRM" come nota: passati a GoHighLevel, esito sconosciuto. Li trattiamo come "da recuperare dall\'export di GoHighLevel" (come previsto)? Nel frattempo restano dentro.'],
 ['Nota "Perso"','Alcune note dicono solo "Perso". Vuol dire non interessato, o che non si sa più niente?']]
sheet('Domande',['Tema','Domanda','Risposta'],Q,[26,110,60],[3])
rows=[]
for _,p in prob.iterrows():
    a,b=df.iloc[p.a],df.iloc[p.b]
    rows.append([a.id,a.sheet,a.row,a['name'],b.id,b.sheet,b.row,b['name'],''])
sheet('Possibili duplicati',['ID 1','Foglio','Riga','Nome','ID 2','Foglio','Riga','Nome','Stessa persona? (sì/no)'],rows,[8,28,6,22,8,28,6,22,22],[9])
rows=[[r.id,r.sheet,r.row,r['name'],r.phone or '(vuoto)',''] for _,r in df[(df.motivo_perimetro=='telefono mancante o illeggibile nel file')].iterrows()]
sheet('Telefoni da recuperare',['ID','Foglio','Riga','Nome','Nel file','Numero giusto (da GoHighLevel)'],rows,[8,30,6,26,14,30],[6])
rows=[[r.id,r.sheet,r.row,r['name'],r.city,'Form in tedesco ma comune italofono',''] for _,r in df[(df.lingua_form=='DE')&df.city.str.lower().str.contains('poschiavo|brusio|bregaglia|roveredo|mesocco')].iterrows()]
rows+=[[r.id,r.sheet,r.row,r['name'],r.city,'Nota: '+r.note[:80],''] for _,r in df[df.lingua_nota.str.contains('spagnolo')].iterrows()]
sheet('Lingua da decidere',['ID','Foglio','Riga','Nome','Città','Perché','Dentro o fuori?'],rows,[8,30,6,24,16,60,18],[7])
wb.save(XLSX); print('ok',len(an))
