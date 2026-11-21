import pandas as pd,re,sys,collections
df=pd.read_pickle(sys.argv[1]); d=df[df.perimetro.str.startswith('dentro')]
# 29MAG: known questions in a single string
Q29=['Quanto tempo hai già perso visitando concessionari?','Ti è mai capitato di sentirti “spinto” verso un’auto diversa da quella che volevi davvero?',
 'Quanto è importante per te trovare ESATTAMENTE l’auto con il colore desiderato, gli optional specifici, il chilometraggio ideale, la motorizzazione giusta e un budget preciso?',
 'Preferiresti:','Cosa ti crea più stress quando cerchi un’auto?','Se potessi trovare la tua auto ideale online, risparmiando tempo e spesso anche denaro, prenderesti in considerazione questa possibilità?',
 'Quanto conta per te avere un prezzo competitivo senza rinunciare alla qualità?','Ultimo passo, un consulente ti contatterà per capire al meglio che auto desideri. Quando vorresti essere chiamato?']
def split_known(t,qs):
    t=t.replace('\xa0',' ').replace('⁠','')
    pos=[(t.find(q),q) for q in qs if t.find(q)>=0]; pos.sort()
    out={}
    for i,(p,q) in enumerate(pos):
        end=pos[i+1][0] if i+1<len(pos) else len(t)
        out[q]=t[p+len(q):end].strip(' -')
    return out
def dist(sub,qs,name):
    c=collections.defaultdict(collections.Counter)
    for t in sub.answers:
        for q,a in split_known(t.lower() if qs[0].islower() else t,qs).items(): c[q][a.strip()[:70]]+=1
    print(f'\n### {name} (n={len(sub)})')
    for q in qs:
        if c[q]: print(' Q:',q[:90]); [print(f'    {v:3d}  {k}') for k,v in c[q].most_common(6)]
dist(d[d.campagna=='29MAG Modulo Acquisto'],Q29,'29MAG')
Q21=["Che cosa rappresenta per te la tua prossima automobile?","Che cosa ti è mancato nelle ricerche fatte finora?","Quale sarebbe l'automobile ideale per te?","Quale budget hai previsto? (Non trattiamo auto dai 30.000 franchi in giù)","Hai un'auto da permutare e come copriresti l'eventuale differenza?","Quando vorresti acquistare?","Quali vantaggi ti aspetti dalla ricerca online?","Quando possiamo ricontattarti?"]
dist(d[d.campagna=='21OTT Modulo Acquisto'],Q21,'21OTT')
QN=['quanto tempo hai già perso visitando concessionari?:','ti è mai capitato di sentirti “spinto” verso un’auto diversa da quella che volevi davvero?:','cosa ti crea più stress quando cerchi un’auto?:','se potessi trovare la tua auto ideale online, risparmiando tempo e spesso anche denaro, prenderesti in considerazione questa possibilità?:',"qual è la fascia di prezzo che hai previsto per la tua prossima auto? prima di rispondere, ricorda che ekkecars propone  solo veicoli a partire da chf 30'000.:",'ultimo passo raccontaci l’auto che desideri davvero: marca e modello,colore preferito, optional indispensabili, cambio automatico/manuale, nuovo o usato, tempistiche d’acquisto :']
dist(d[d.campagna=='10NOV Modulo Svizzera Profilante'],QN,'10NOV')
QP=["Quando vorresti acquistare l'auto?","Qual è il tuo budget indicativo?","Che tipo di auto stai cercando?","Preferisci auto:","Hai un'auto da permutare?","Verso che ora preferisci essere contattato?","Se avessimo già l'auto che cerchi, saresti pronto a bloccarla subito?"]
sub=d[d.campagna.isin(['15APR Altaprofilazione','15MAG Altaprofilazione','18APR Imprenditori'])].copy()
dist(sub,QP,'15APR+15MAG+18APR')
sub=d[d.campagna=='15MAR Altamente profilante'].copy(); sub['answers']=sub.answers.str.replace('\n',' ').str.replace('/',' ')
dist(sub,QP,'15MAR')
