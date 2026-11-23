import pandas as pd,re,sys,numpy as np
d=pd.read_pickle(sys.argv[1]); OUTDIR=sys.argv[2]
d=d.copy()
def split_name(n):
    t=[x for x in re.split(r'\s+',re.sub(r'[_]',' ',n).strip()) if x]
    t=[x.capitalize() if (x.islower() or x.isupper()) else x for x in t]
    return (t[0] if t else ''), ' '.join(t[1:])
nm=d.name.map(split_name); d['first']=[a for a,b in nm]; d['last']=[b for a,b in nm]
wa=d[d.perimetro=='dentro'].copy()
# stesso numero con nomi diversi (casi dubbi tenuti): un solo messaggio per numero, si tiene l'iscrizione più recente
n0=len(wa); wa=wa.sort_values('data',ascending=False).drop_duplicates('tel'); print('numeri doppi tolti:',n0-len(wa))
call=d[d.perimetro=='dentro (solo chiamata)'].copy()
# ondate: 5 gruppi mescolati in modo uguale per segmento (seed fisso)
rng=np.random.default_rng(2026)
wa['ondata']=0
for sgm,g in wa.groupby('segmento'):
    idx=rng.permutation(g.index.values)
    for k,i in enumerate(idx): wa.at[i,'ondata']=k%5+1
GIORNO={1:'lunedì',2:'sabato',3:'lunedì',4:'sabato',5:'lunedì'}
wa['giorno_test']=wa.ondata.map(GIORNO)
out=pd.DataFrame({'Phone':wa.tel,'First Name':wa['first'],'Last Name':wa['last'],'Email':wa.email.str.strip(),
 'Riattivazione Segmento':wa.segmento,'Riattivazione Ondata':wa.ondata,'Riattivazione Giorno':wa.giorno_test,
 'Riattivazione Auto':np.where(wa.segmento=='S1',wa.auto_con_articolo,''),'Riattivazione Tipo':np.where(wa.segmento=='S2',wa.tipo,''),
 'Tags':'riattivazione-nov26, riatt-'+wa.segmento.str.lower()+', riatt-ondata-'+wa.ondata.astype(str),
 'ID lead':wa.id,'Campagna origine':wa.campagna}).sort_values(['Riattivazione Ondata','Riattivazione Segmento'])
# controlli
assert out.Phone.str.match(r'^\+\d{10,14}$').all()
assert not out.Phone.duplicated().any()
assert (out[out['Riattivazione Segmento']=='S1']['Riattivazione Auto']!='').all()
assert (out[out['Riattivazione Segmento']=='S2']['Riattivazione Tipo']!='').all()
for c in out.columns: assert not out[c].astype(str).str.contains('\n').any(), c
out.to_csv(f'{OUTDIR}/Riattivazione-import-GHL.csv',index=False,encoding='utf-8-sig')
pd.DataFrame({'Telefono':call.tel,'Nome':call.name,'ID lead':call.id,'Campagna':call.campagna,'Cosa cercava':call.request,'Note':call.note}).to_csv(f'{OUTDIR}/Riattivazione-solo-chiamata.csv',index=False,encoding='utf-8-sig')
print(len(out),len(call)); print(pd.crosstab(out['Riattivazione Ondata'],out['Riattivazione Segmento'],margins=True))
print(out['Phone'].str[:3].value_counts().to_dict())
