import openpyxl,re,sys,json,datetime
import pandas as pd
SRC=sys.argv[1]; OUT=sys.argv[2]
wb=openpyxl.load_workbook(SRC)
CANON={
 'data':'date','maps':'date','nome e cognome':'name','nome':'name','telefono':'phone','e-mail':'email','email':'email',
 'città':'city','veicolo':'request','auto':'request','che modello di auto cerchi?':'request','budget':'budget','budget in mente?':'budget',
 'budget?':'budget','scoring':'scoring','chat':'chat','osservazioni':'obs','note':'obs','risposta':'obs2',
 'consulente':'consultant','interessato':'f_interessato','valido':'f_valido','offerta':'f_offerta','leasing':'f_leasing',
 'vendita':'f_vendita','campagna':'campaign','risposta domande':'answers'}
def fill(c):
    try:
        if c.fill is None or c.fill.fill_type is None: return ''
        v=c.fill.fgColor.rgb
        return v if isinstance(v,str) else ('theme%s'%c.fill.fgColor.theme)
    except Exception: return '?'
def val(c):
    v=c.value
    if v is None: return ''
    if isinstance(v,(datetime.datetime,datetime.date)): return v.isoformat()
    s=str(v)
    m=re.match(r'=HYPERLINK\("([^"]+)"',s)
    if m: return m.group(1)
    return s.strip()
rows=[]
for ws in wb:
    if ws.title=='KPI': continue
    hdr=[(c.value or '') for c in ws[1]]
    maxc=max(i for i,h in enumerate(hdr) if str(h).strip() and not str(h).startswith('Unnamed'))+1 if any(hdr) else 0
    hdr=hdr[:maxc]
    for r in ws.iter_rows(min_row=2,max_col=max(maxc,2)):
        name=val(r[1]); phone=val(r[2]) if len(r)>2 else ''
        if not name and not phone: continue
        # skip legend rows
        if name.upper() in ('DA CHIAMARE','PASSATO','DOPPIO','POSTICIPATO'): continue
        d={'sheet':ws.title,'row':r[0].row,'fill':fill(r[1]),'fill_obs':''}
        extra=[]
        for j,h in enumerate(hdr):
            key=CANON.get(str(h).strip().lower())
            v=val(r[j])
            if key=='obs': d['fill_obs']=fill(r[j])
            if key is None:
                if v: extra.append(f'{str(h).strip()}: {v}')
                continue
            if key in d and d[key]: d[key]+=' | '+v
            else: d[key]=v
        d['form_extra']=' || '.join(extra)
        rows.append(d)
df=pd.DataFrame(rows).fillna('')
df.to_pickle(OUT)
print(df.shape); print(df.groupby('sheet').size().sort_values())
