import pandas as pd,sys
df=pd.read_pickle(sys.argv[1])
df['data']=pd.to_datetime(df.data)
def md(t): return t.to_markdown(index=False)
out=[]
din=df.perimetro.str.startswith('dentro')
# per campaign
g=df.groupby('campagna')
t=pd.DataFrame({
 'Righe':g.size(),
 'Dal':g.data.min().dt.strftime('%d.%m.%y'),'Al':g.data.max().dt.strftime('%d.%m.%y'),
 'Canale':g.canale.first(),'Lingua form':g.lingua_form.agg(lambda s:'/'.join(sorted(set(s)))),
 'Persone uniche':g.record_principale.sum(),
 'Nel perimetro':g.perimetro.agg(lambda s:s.str.startswith('dentro').sum()),
}).reset_index().sort_values('Dal',key=lambda s:pd.to_datetime(s,format='%d.%m.%y'))
tot=pd.DataFrame([{'campagna':'**Totale**','Righe':t.Righe.sum(),'Dal':'','Al':'','Canale':'','Lingua form':'','Persone uniche':t['Persone uniche'].sum(),'Nel perimetro':t['Nel perimetro'].sum()}])
out.append('## T1\n'+md(pd.concat([t,tot])))
# funnel
f=df.motivo_perimetro.replace('', 'dentro').value_counts()
out.append('## T2\n'+f.to_markdown())
# per campaign, in-perimeter: contact outcome + info level
d=df[din]
ct=pd.crosstab(d.campagna,d.esito_contatto,margins=True,margins_name='Totale')
out.append('## T3 esito\n'+ct.to_markdown())
ct=pd.crosstab(d.campagna,d.livello_info,margins=True,margins_name='Totale')
out.append('## T4 info\n'+ct.to_markdown())
# what info each form collects
out.append('## T5 età\n'+pd.cut(d.eta_giorni,[0,30,60,90,180,270,365,500],labels=['<1 mese','1-2 mesi','2-3 mesi','3-6 mesi','6-9 mesi','9-12 mesi','>12 mesi']).value_counts().sort_index().to_markdown())
out.append('## T6 mesi\n'+d.data.dt.to_period('M').value_counts().sort_index().to_markdown())
out.append('## T8 consulente (dentro)\n'+d.consultant.replace('','(nessuno)').value_counts().to_markdown())
out.append('## T9 iscrizioni multiple\n'+d.n_iscrizioni.value_counts().sort_index().to_markdown())
out.append('## T10 tel tipo dentro\n'+d.tel_tipo.value_counts().to_markdown())
out.append('## flags dentro\n'+str({'comprato_altrove':int(d.ha_comprato_altrove.sum()),'non_interessato':int(d.non_interessato.sum()),'budget_basso':int(d.budget_basso.sum()),'concluso':int(d.concluso.sum()),'interessato_flag':int(d.interessato_flag.sum()),'chat_link':int(d.chat.str.startswith('http').sum()),'scoring':int((d.scoring.str.strip()!='').sum()),'tentativi>=1':int((d.tentativi_x>0).sum())}))
print('\n\n'.join(out))
