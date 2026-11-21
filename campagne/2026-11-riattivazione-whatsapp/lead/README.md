# Lead storici – inventario e analisi per la riattivazione

> Aperto il 21 novembre 2026. Lavoro **separato** dai copy della riattivazione: qui si capisce *chi* c'è nella lista. Il *cosa* scrivere resta in `../brief.md` e `../copy/`.

## Perché esiste

Il brief della riattivazione è partito da una stima (500-700 lead, un messaggio uguale per tutti). Ora abbiamo il file completo dei lead (`EKKECARS_Leads.xlsx`, export del Google Sheet di gestione lead) e possiamo decidere con i dati:

- se ha senso un messaggio uguale per tutti o messaggi diversi per tipo di lead;
- come testare la riattivazione (giorni, orari, varianti);
- quanto costa davvero una riattivazione.

## Tappe (con stop e revisione dopo ognuna)

| # | Tappa | Stato |
|-|-|-|
| 1 | **Inventario** + revisione di Simone e Loris | ✅ fatta, revisione applicata (v2) → `inventario.md` |
| 2 | Differenze tra campagne: richieste, tipo di lead, informazioni, tassi di contatto e risposta | da fare |
| 3 | Voce dei lead (parole e auto da riusare nei messaggi) + proposta di segmenti e test (anche A/B sabato vs lunedì, orari scaglionati) | da fare |
| 4 | Costi WhatsApp via GoHighLevel (simulazioni a 5, 10, 15 messaggi) + rischi di blocco Meta | ✅ chiusa: 5 messaggi entro il 14/12 → `costi-e-rischi.md` |

## Decisioni prese (grilling del 21/11)

| Tema | Decisione |
|-|-|
| Data del primo messaggio | **Non parte sabato 21/11**. Probabilmente lunedì, con A/B tra sabato e lunedì a orari scaglionati |
| Messaggio uguale per tutti? | **Si riapre la domanda.** Prima l'inventario, poi si decide cosa mandare, a chi e come |
| Quali lead | **Tutti quelli del file**, si spremono tutti. Fuori solo le eccezioni sotto |
| Lead in tedesco | **Fuori** (Loris non parla tedesco), tranne chi ha risposto al form in italiano. I lead di "Prezzo IT-DE" sono italofoni in Svizzera tedesca: **dentro** |
| Furgoni, Imprenditori, Sito WEB | **Dentro**. Sito WEB in particolare: di solito sono i più caldi |
| Lead recenti (ott-nov 2026) | **Dentro**, come tutti gli altri |
| Numeri non validi o falsi | **Fuori**. Unica esclusione per esito |
| Insulti, chi ha attaccato in faccia, chi ci ha mandato a quel paese | **Dentro**: si ricontattano |
| Duplicati | Tolti, **ma solo se sicuri al 100%**. Nei casi dubbi si tengono entrambi e si segnalano |
| Dati personali | Nel repo **solo** dati anonimizzati (ID al posto di nome, telefono, email). Il file Excel originale e le liste con i contatti restano fuori |
| Revisione note (21/11) | **X1/X2/X3 = chiamato, mai risposto · WA = parlato su WhatsApp · i colori si ignorano, conta solo la nota** |
| Consenso WhatsApp | **Sì**, i lead hanno dato il consenso a ricevere messaggi |
| Lead ott-nov 2026 ancora in lavorazione (77) | **Si riattivano comunque** |
| Clienti che hanno già comprato | Non serve la lista: **si riattivano tutti** |
| Valentino, Riccardo, Paolo | **Non lavorano più con noi.** I lead li chiama solo Loris (quindi niente lead in tedesco) |
| Colonna Chat | Sono le **chat WhatsApp con i lead** (Google Doc, una per lead, titolo = numero di telefono). Accesso verificato il 21/11: si leggono. 193 in tutto, di cui 108 di lead italiani (95 Prezzo Basso Timing, 12 Prezzo IT-IT, 1 Furgoni) e 85 di FEB Auto DE. Materiale per la tappa 3 |
| Esiti in GoHighLevel | Export da fare più avanti. Nel frattempo Loris fornisce alcuni dati a voce |
| Quanti messaggi | **5** (calendario sotto). È la prima riattivazione: è un test, non si vuole spendere troppo |
| Chi risponde | **Esce dalla sequenza e resta in pipeline** per Loris |
| Chi chiede stop | **Fuori** da tutto |
| Chi non risponde | **Continua** a ricevere i messaggi successivi |
| Ritmo degli invii | **Ondate da 200-300 lead**, scaglionate negli orari, in base a quanti Loris riesce a richiamare |
| Numero mittente | **Numero aziendale**, non quello personale di Loris. Loris ha accesso alle chat, legge e chiama al volo |
| Limite di invio | Il numero ha già mandato messaggi in passato (non tantissimi): si presume nessun limite stretto. Le ondate da 200-300 stanno comunque sotto anche il livello minimo (250 al giorno) |
| Tempo di Loris | Ha il tempo per chiamare i lead che rispondono |
| Tariffa GoHighLevel | In attesa, **in secondo piano**: si assume che sia una cifra sostenibile |
| Calendario | **2 messaggi a settimana nelle prime due settimane**, poi 1: la sequenza **chiude entro il 14/12**, prima di Natale |
| Costo pieno con il tempo di Loris | **Non serve** |
| Nota "CRM" (27 lead) | Esito da recuperare dall'export di GoHighLevel, **se c'è tempo**. Intanto restano dentro |
| Nota "Perso" | In quel momento non era più interessato, **ma si richiama comunque** |
| Possibili duplicati (6) | Nessuna certezza: **si tengono entrambi** |
| Telefoni illeggibili (22) | **Non si recuperano**: restano fuori |
| Lingua: Poschiavo e "parla spagnolo" | **Dentro** (il lead di Poschiavo era già dentro con un'altra iscrizione in italiano) |
| Lead seguiti da ex consulenti | **Nessun problema**: non si ricordano chi li ha chiamati, si ricordano solo che qualcuno gli ha parlato |

## File

| File | Cosa contiene |
|-|-|
| `inventario.md` | Tappa 1: quanti lead, da quali campagne, chi è dentro e chi è fuori, cosa sappiamo di loro, domande aperte |
| `costi-e-rischi.md` | Tappa 4: tariffe, simulazioni a 5, 10 e 15 messaggi, tempo di Loris, rischi per il numero WhatsApp, raccomandazione |
| `dati/lead-anonimi.csv` | Una riga per iscrizione (1.689), **senza nome, telefono, email**. Colonne derivate: perimetro, esito contatto, livello di informazione, budget, tempistica, marca, regione… |
| `script/` | Script Python che rigenerano tutto dal file Excel originale (`bash script/run.sh <xlsx> <cartella-lavoro>`) |

Gli Excel con i nomi (domande aperte, poi le liste per gli invii) stanno in `_privato/`, **esclusa da git**. Le domande della tappa 1 sono tutte chiuse (21/11).

## Come leggere il CSV

- `id` = la riga; `id_persona` = la persona dopo il dedup (stesso valore per le iscrizioni multiple). Per contare le persone, filtra `record_principale = True`.
- `perimetro` = `dentro` / `dentro (solo chiamata)` / `fuori`, con il motivo in `motivo_perimetro`.
- `foglio_origine` + `riga_origine` portano alla riga esatta del Google Sheet originale.
- `esito_contatto` segue la revisione del 21/11 (conta solo la nota). `regione_stimata` e `livello_info` sono **ricavate da me** dal testo: sono stime.
- I colori del foglio originale non sono nel CSV: abbiamo deciso di ignorarli.
