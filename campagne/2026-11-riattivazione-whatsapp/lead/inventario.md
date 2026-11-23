# Inventario lead storici (tappa 1)

> Fonte: `EKKECARS_Leads.xlsx` ricevuto il 21/11/2026 (export del Google Sheet di gestione lead). Dati rigenerabili con `script/run.sh`.
> **Versione 2 (21/11), con la revisione di Simone e Loris applicata:** X1/X2/X3 = chiamato, mai risposto · WA = parlato su WhatsApp · **i colori si ignorano, conta solo la nota**.

## In una riga

**1.689 iscrizioni → 1.482 persone uniche → 1.274 lead riattivabili** (1.267 via WhatsApp + 7 numeri fissi solo da chiamare).

> Aggiornamento del 21/11 sera: tolti **7 lead che nelle chat WhatsApp di maggio avevano scritto "Disiscriviti"** (5 Prezzo Basso Timing, 1 Prezzo IT-IT, 1 Auto ITA). Le tabelle di dettaglio sotto sono ancora a 1.281: la differenza è solo questa.

La stima del brief (500-700) era bassa di circa la metà.

> **Lista di invio finale (23/11): 1.096 lead.** Ai 1.274 riattivabili qui sotto vanno tolti i duplicati di numero (2), i 7 numeri fissi (li chiama Loris) e i 169 lead con budget dichiarato sotto i 20'000 franchi, messi da parte come "lead con budget basso". Dettaglio in `README.md`.

## 1. Da dove vengono

Il file ha 21 fogli: 19 con lead, 1 vuoto (`1OTTOBRE`) e il foglio `KPI` (solo definizioni). Le 19 campagne si raggruppano in 6 famiglie:

| Famiglia | Campagne (foglio) | Periodo | Iscrizioni | Nel perimetro |
|-|-|-|-:|-:|
| **Prezzo Basso** (form Meta corto: nome, auto cercata) | OTT25 Sogni (CH-NE), NOV25 Prezzo IT-IT, NOV25 Prezzo IT-DE, DIC25 Prezzo Basso Timing | ott 2025 – feb 2026 | 606 | **471** |
| **Auto ITA** (tipo di auto + budget) | 25FEB Auto ITA | feb – apr 2026 | 483 | **422** |
| **Profilazione** (tempistica, budget, tipo, nuova/usata, permuta) | 15MAR Altamente profilante, 15APR Altaprofilazione, 15MAG Altaprofilazione, 18APR Imprenditori | mar – mag 2026 | 173 | **147** |
| **Modulo Acquisto** (domande "psicologiche" sul concessionario) | 29MAG, 21OTT, 26OTT Modulo Acquisto, 10NOV Modulo Svizzera | mag – nov 2026 | 227 | **205** |
| **Furgoni IT** (B2B leggero: artigiani, imprese) | FEB Furgoni IT | feb 2026 | 17 | **14** |
| **Sito WEB** (organico) | Sito WEB | ott 2025 – feb 2026 | 32 | **22** |
| Tedeschi (tutti fuori) | FEB Auto DE, FEB Furgoni DE, NOV25 RS6 DE-DE, NOV25 Compra Online DE-DE | nov 2025 – mar 2026 | 151 | 0 |
| **Totale** | | ott 2025 – nov 2026 | **1.689** | **1.281** |

<details><summary>Dettaglio per singolo foglio</summary>

| Campagna | Righe | Dal | Al | Lingua form | Persone uniche | Nel perimetro |
|:-|-:|:-|:-|:-|-:|-:|
| OTT25 Sogni (Prezzo Basso CH-NE) | 196 | 09.10.25 | 06.11.25 | IT (6 righe DE) | 145 | 136 |
| Sito WEB | 32 | 20.10.25 | 28.02.26 | IT | 26 | 22 |
| NOV25 Prezzo IT-IT | 61 | 06.11.25 | 19.02.26 | IT | 43 | 40 |
| NOV25 Prezzo IT-DE | 30 | 06.11.25 | 12.11.25 | IT | 27 | 26 |
| NOV25 Compra Online DE-DE | 2 | 16.11.25 | 16.11.25 | DE | 2 | 0 |
| NOV25 RS6 DE-DE | 6 | 23.11.25 | 25.11.25 | DE | 4 | 0 |
| DIC25 Prezzo Basso Timing | 319 | 30.11.25 | 05.02.26 | IT | 280 | 269 |
| FEB Furgoni DE | 12 | 08.02.26 | 12.02.26 | DE | 12 | 0 |
| FEB Furgoni IT | 17 | 08.02.26 | 12.02.26 | IT | 16 | 14 |
| FEB Auto DE | 131 | 15.02.26 | 02.03.26 | DE | 121 | 0 |
| 25FEB Auto ITA | 483 | 26.02.26 | 27.04.26 | IT | 437 | 422 |
| 15MAR Altamente profilante | 111 | 16.03.26 | 17.04.26 | IT | 96 | 94 |
| 15APR Altaprofilazione | 38 | 15.04.26* | 14.05.26 | IT | 33 | 30 |
| 18APR Imprenditori | 4 | 18.04.26* | 18.04.26 | IT | 4 | 4 |
| 15MAG Altaprofilazione | 20 | 16.05.26 | 29.05.26 | IT | 19 | 19 |
| 29MAG Modulo Acquisto | 143 | 30.05.26 | 03.09.26 | IT | 136 | 128 |
| 26OTT Modulo Acquisto | 48 | 26.10.26 | 20.11.26 | IT | 46 | 44 |
| 21OTT Modulo Acquisto | 30 | 26.10.26 | 09.11.26 | IT | 29 | 28 |
| 10NOV Modulo Svizzera Profilante | 6 | 10.11.26 | 13.11.26 | IT | 6 | 5 |

\* Data mancante nel file (`[object Object]`): usata quella del nome del foglio.
Le colonne "Persone uniche" e "Nel perimetro" contano la persona nella campagna della sua iscrizione **più recente**.

</details>

## 2. Chi è fuori e perché

| Passaggio | Lead | Restano |
|-|-:|-:|
| Iscrizioni nel file | | 1.689 |
| − Duplicati sicuri (stesso telefono + stesso nome, oppure stesso telefono + stessa email) | 207 | 1.482 |
| − Form compilato in tedesco | 144 | 1.338 |
| − Nota del consulente: "parla tedesco" | 11 | 1.327 |
| − Numero non valido (lo dice la nota) | 24 | 1.303 |
| − Telefono vuoto o `#ERROR!` nel file | 22 | 1.281 |
| − Hanno chiesto la disiscrizione su WhatsApp (maggio 2026) | 7 | **1.274** |
| di cui numero fisso (niente WhatsApp, solo chiamata) | 7 | |

- **Duplicati:** 151 persone si sono iscritte a più campagne (120 due volte, 24 tre volte, 7 da quattro a sette volte). Le coppie più frequenti sono 25FEB Auto ITA con 15MAR Altamente profilante e con Prezzo Basso Timing. Come record si tiene il più recente; le note delle altre iscrizioni restano nel CSV (`id_persona`).
- **6 casi dubbi** (stesso telefono ma nome diverso, per esempio famiglia o ditta): tenuti entrambi e messi nell'Excel delle domande aperte.
- **"Modulo Sogni DE" non è tedesco:** nonostante il nome, il foglio contiene la campagna Prezzo Basso CH-NE con lead che scrivono in italiano (Lugano, Bellinzona, Airolo…). Tenuto dentro, tranne 6 righe di una campagna DE.
- **I 22 telefoni illeggibili** si possono recuperare da GoHighLevel: la lista è nell'Excel.

## 3. Quanto sono vecchi

| Età (al 21/11/2026) | Lead nel perimetro |
|-|-:|
| meno di 1 mese (ott-nov 2026, ancora in lavorazione: si riattivano comunque) | 77 |
| 1-3 mesi | 12 |
| 3-6 mesi | 120 |
| 6-9 mesi | 568 |
| 9-12 mesi | 313 |
| più di 12 mesi | 191 |

**L'84% ha più di 6 mesi.** Tra giugno e settembre 2026 sono entrati pochissimi lead (circa 120 in 4 mesi): probabilmente coincide con il cambio di gestione del marketing (vedi `contesto/01-azienda.md`), da confermare.

## 4. Quanto li abbiamo lavorati (conta solo la nota)

| Esito ricavato dalla nota | Lead | % |
|-|-:|-:|
| Note di contenuto (auto, budget, motivo di scarto, "da richiamare"…): parlato o in corso | 399 | 31% |
| **Parlato su WhatsApp** (nota "WA") | 149 | 12% |
| Mai risposto (solo "X1/X2/X3" o "non risponde") | 179 | 14% |
| **Nessuna nota** | 527 | 41% |
| Passato al CRM (nota "CRM", esito in GoHighLevel) | 27 | 2% |

Per famiglia:

| Famiglia | Note di contenuto | Parlato su WA | Mai risposto | Nessuna nota | CRM |
|-|-:|-:|-:|-:|-:|
| Prezzo Basso (471) | 248 | 142 | 72 | 9 | 0 |
| Auto ITA (422) | 114 | 3 | 86 | 205 | 14 |
| Profilazione (147) | 17 | 1 | 10 | 106 | 13 |
| Modulo Acquisto (205) | 0 | 0 | 0 | **205** | 0 |
| Furgoni IT (14) | 6 | 0 | 8 | 0 | 0 |
| Sito WEB (22) | 14 | 3 | 3 | 2 | 0 |

- **Prezzo Basso è la famiglia più lavorata:** l'83% ha avuto una conversazione, al telefono o su WhatsApp. Le 108 chat WhatsApp salvate su Google Doc vengono quasi tutte da qui.
- **"Nessuna nota" non vuol dire per forza "mai chiamato":** da marzo in poi le note quasi spariscono. Probabilmente i lead sono stati gestiti in GoHighLevel. L'export è previsto più avanti.

## 5. Cosa sappiamo di loro (livello di informazione)

| Livello | Lead | Da dove vengono soprattutto |
|-|-:|-|
| A. Modello specifico ("Audi Q5 Sportback", "Golf", "GLC 300d") | 414 | Prezzo Basso, Sito WEB |
| C. Tipo di auto, budget e/o tempistica, senza modello | 647 | Auto ITA, Profilazione, Furgoni |
| D. Solo risposte "psicologiche" (tempo perso, stress, "spinto" verso un'auto) | 128 | 29MAG Modulo Acquisto |
| E. Solo contatto | 88 | 26OTT Modulo Acquisto, parte di Prezzo IT-IT |
| (B. Solo marca, senza modello) | 4 | |

Questo è il primo asse naturale di segmentazione: con 414 lead possiamo aprire con **la loro auto** ("ci avevi chiesto una Q5…"); con gli altri no.

Altri dati disponibili (nel perimetro, dove il form li chiedeva):

- **Budget:** 30-50k: 167 · 20-30k: 55 · sotto i 20-30k: 174 · oltre 50k: 12 · espresso come rata mensile: 128 · non dichiarato: 745. **Una buona parte del budget dichiarato è sotto la soglia dei 35'000 franchi.**
- **Tipo di auto:** SUV/crossover 289 · berlina 148 · station wagon 70 · city car 68 · elettrica/ibrida 63 · sportiva 15.
- **Marche richieste** (dove c'è il modello): Audi 89 · Mercedes 89 · BMW 45 · Alfa Romeo 40 · VW 33 · Fiat/Jeep 28 · Toyota 23 · poi Skoda, Ford, BYD/MG, Hyundai/Kia.
- **Tempistica dichiarata:** entro 1 mese 258 · 1-3 mesi 76 · sto valutando 125. Erano dichiarazioni di 6-12 mesi fa: chi diceva "subito" a marzo nel frattempo ha comprato o rinunciato.
- **Permuta:** sì 115 · no 82 (solo dove il form lo chiedeva).

## 6. Dove vivono (stima dal campo città)

| Regione | Lead nel perimetro |
|-|-:|
| Ticino / Grigioni italiano | 519 |
| Svizzera tedesca (compilato in italiano) | 615 |
| Romandia (compilato in italiano) | 103 |
| Italia | 22 |
| Non indicata | 22 |

**Quasi la metà sono italofoni che vivono fuori dal Ticino.** È un pubblico diverso da quello del brief ("solo Ticino"). Nei copy: niente riferimenti solo ticinesi, e va detto che consegniamo anche con trasportatore.

## 7. Chi li ha lavorati

Loris 360 · Valentino 128 · Simone 101 · Riccardo 81 · Giuseppe 13 · Paolo 6 · nessun consulente indicato 592.
Valentino, Riccardo e Paolo **non lavorano più con noi**: i lead li richiama Loris. Non è un problema: i lead non si ricordano chi li ha chiamati, solo che qualcuno gli ha parlato.

## 8. Domande della tappa 1: tutte chiuse (21/11)

- **6 possibili duplicati:** nessuna certezza, si tengono entrambi.
- **22 telefoni illeggibili:** non si recuperano, restano fuori.
- **Lingua:** il lead di Poschiavo e quello che "parla spagnolo" sono dentro.
- **"Perso"** = in quel momento non era interessato, si richiama comunque. **"CRM"** = esito da recuperare da GoHighLevel, se c'è tempo.
- **Calendario:** 2 messaggi a settimana nelle prime due settimane, chiusura entro il 14/12.

## 9. Prime impressioni (da verificare nella tappa 2)

- **Un messaggio unico per tutti spreca il dato migliore che abbiamo:** per 414 lead sappiamo l'auto. Un richiamo specifico ("cercavi una Q5") è molto più forte di "ci avevi scritto per un'auto".
- **Le famiglie sono pubblici diversi**, non solo campagne diverse: Prezzo Basso = gente che ha parlato con noi (al telefono o su WhatsApp) e che ha un modello in testa · Auto ITA e Profilazione = lead con budget dichiarato, spesso basso, poco lavorati · Modulo Acquisto = nessun dato sull'auto, solo frustrazione verso i concessionari, che è esattamente l'angolo del brief.
- **Il 41% senza note e il 14% mai risposto** sono, di fatto, lead freddi mai lavorati: per loro la riattivazione è un primo contatto più che un richiamo.
