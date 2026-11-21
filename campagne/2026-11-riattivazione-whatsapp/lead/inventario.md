# Inventario lead storici (tappa 1)

> Fonte: `EKKECARS_Leads.xlsx` ricevuto il 21/11/2026 (export del Google Sheet di gestione lead). Dati rigenerabili con `script/run.sh`.
> **In revisione:** la legenda dei colori e i codici nelle note sono mie ipotesi. Li stanno correggendo Simone e Loris.

## In una riga

**1.689 iscrizioni → 1.482 persone uniche → 1.280 lead riattivabili** (1.274 via WhatsApp + 6 numeri fissi solo da chiamare).

La stima del brief (500-700) era bassa di circa la metà.

## 1. Da dove vengono

Il file ha 21 fogli: 19 con lead, 1 vuoto (`1OTTOBRE`) e il foglio `KPI` (solo definizioni). Le 19 campagne si raggruppano in 6 famiglie:

| Famiglia | Campagne (foglio) | Periodo | Iscrizioni | Nel perimetro |
|-|-|-|-:|-:|
| **Prezzo Basso** (form Meta corto: nome, auto cercata) | OTT25 Sogni (CH-NE), NOV25 Prezzo IT-IT, NOV25 Prezzo IT-DE, DIC25 Prezzo Basso Timing | ott 2025 – feb 2026 | 606 | **472** |
| **Auto ITA** (tipo di auto + budget) | 25FEB Auto ITA | feb – apr 2026 | 483 | **420** |
| **Profilazione** (tempistica, budget, tipo, nuova/usata, permuta) | 15MAR Altamente profilante, 15APR Altaprofilazione, 15MAG Altaprofilazione, 18APR Imprenditori | mar – mag 2026 | 173 | **146** |
| **Modulo Acquisto** (domande "psicologiche" sul concessionario) | 29MAG, 21OTT, 26OTT Modulo Acquisto, 10NOV Modulo Svizzera | mag – nov 2026 | 227 | **205** |
| **Furgoni IT** (B2B leggero: artigiani, imprese) | FEB Furgoni IT | feb 2026 | 17 | **15** |
| **Sito WEB** (organico) | Sito WEB | ott 2025 – feb 2026 | 32 | **22** |
| Tedeschi (tutti fuori) | FEB Auto DE, FEB Furgoni DE, NOV25 RS6 DE-DE, NOV25 Compra Online DE-DE | nov 2025 – mar 2026 | 151 | 0 |
| **Totale** | | ott 2025 – nov 2026 | **1.689** | **1.280** |

<details><summary>Dettaglio per singolo foglio</summary>

| Campagna | Righe | Dal | Al | Lingua form | Persone uniche | Nel perimetro |
|:-|-:|:-|:-|:-|-:|-:|
| OTT25 Sogni (Prezzo Basso CH-NE) | 196 | 09.10.25 | 06.11.25 | IT (6 righe DE) | 145 | 137 |
| Sito WEB | 32 | 20.10.25 | 28.02.26 | IT | 26 | 22 |
| NOV25 Prezzo IT-IT | 61 | 06.11.25 | 19.02.26 | IT | 43 | 42 |
| NOV25 Prezzo IT-DE | 30 | 06.11.25 | 12.11.25 | IT | 27 | 26 |
| NOV25 Compra Online DE-DE | 2 | 16.11.25 | 16.11.25 | DE | 2 | 0 |
| NOV25 RS6 DE-DE | 6 | 23.11.25 | 25.11.25 | DE | 4 | 0 |
| DIC25 Prezzo Basso Timing | 319 | 30.11.25 | 05.02.26 | IT | 280 | 267 |
| FEB Furgoni DE | 12 | 08.02.26 | 12.02.26 | DE | 12 | 0 |
| FEB Furgoni IT | 17 | 08.02.26 | 12.02.26 | IT | 16 | 15 |
| FEB Auto DE | 131 | 15.02.26 | 02.03.26 | DE | 121 | 0 |
| 25FEB Auto ITA | 483 | 26.02.26 | 27.04.26 | IT | 437 | 420 |
| 15MAR Altamente profilante | 111 | 16.03.26 | 17.04.26 | IT | 96 | 93 |
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
| − Numero non valido (nota o cella rossa) | 25 | 1.302 |
| − Telefono vuoto o `#ERROR!` nel file | 22 | **1.280** |
| di cui numero fisso (niente WhatsApp, solo chiamata) | 6 | |

- **Duplicati:** 151 persone si sono iscritte a più campagne (120 due volte, 24 tre volte, 7 da quattro a sette volte). Le coppie più frequenti sono 25FEB Auto ITA con 15MAR Altamente profilante e con Prezzo Basso Timing. Come record si tiene il più recente; le note delle altre iscrizioni restano nel CSV (`id_persona`).
- **6 casi dubbi** (stesso telefono ma nome diverso, per esempio famiglia o ditta): tenuti entrambi e messi tra i casi da verificare per Loris.
- **"Modulo Sogni DE" non è tedesco:** nonostante il nome, il foglio contiene la campagna Prezzo Basso CH-NE con lead che scrivono in italiano (Lugano, Bellinzona, Airolo…). Tenuto dentro, tranne 6 righe di una campagna DE.

## 3. Quanto sono vecchi

| Età (al 21/11/2026) | Lead nel perimetro |
|-|-:|
| meno di 1 mese (ott-nov 2026) | 77 |
| 1-3 mesi | 12 |
| 3-6 mesi | 120 |
| 6-9 mesi | 565 |
| 9-12 mesi | 314 |
| più di 12 mesi | 192 |

**L'84% ha più di 6 mesi.** Il buco tra giugno e settembre 2026 (circa 120 lead in 4 mesi) probabilmente coincide con il cambio di gestione del marketing (vedi `contesto/01-azienda.md`): da confermare.

## 4. Quanto li abbiamo lavorati (stato nel file)

| Esito ricavato dalle note | Lead | % |
|-|-:|-:|
| Parlato / note con contenuto (auto, budget, motivo di scarto…) | 457 | 36% |
| Mai raggiunto (solo "X1/X2/X3", "WA", "non risponde") | 274 | 21% |
| **Nessuna nota** | 522 | 41% |
| Passato al CRM (nota "CRM") | 27 | 2% |

Per famiglia la situazione cambia molto:

| Famiglia | Parlato | Mai raggiunto | Nessuna nota | CRM |
|-|-:|-:|-:|-:|
| Prezzo Basso (472) | 290 | 173 | 9 | 0 |
| Auto ITA (420) | 121 | 84 | 201 | 14 |
| Profilazione (146) | 19 | 9 | 105 | 13 |
| Modulo Acquisto (205) | 0 | 0 | **205** | 0 |
| Furgoni IT (15) | 9 | 6 | 0 | 0 |
| Sito WEB (22) | 18 | 2 | 2 | 0 |

⚠️ **"Nessuna nota" non vuol dire "mai chiamato".** Le campagne da marzo in poi hanno pochissime note o nessuna, e in 25FEB Auto ITA 204 celle delle note sono colorate di azzurro senza testo. Probabilmente da un certo punto i lead sono stati gestiti in **GoHighLevel** e gli esiti sono lì. Serve un export (vedi domande).

## 5. Cosa sappiamo di loro (livello di informazione)

| Livello | Lead | Da dove vengono soprattutto |
|-|-:|-|
| A. Modello specifico ("Audi Q5 Sportback", "Golf", "GLC 300d") | 413 | Prezzo Basso, Sito WEB |
| C. Tipo di auto, budget e/o tempistica, senza modello | 645 | Auto ITA, Profilazione, Furgoni |
| D. Solo risposte "psicologiche" (tempo perso, stress, "spinto" verso un'auto) | 128 | 29MAG Modulo Acquisto |
| E. Solo contatto | 90 | 26OTT Modulo Acquisto, parte di Prezzo IT-IT |
| (B. Solo marca, senza modello) | 4 | |

Questo è il primo asse naturale di segmentazione: con 413 lead possiamo aprire con **la loro auto** ("ci avevi chiesto una Q5…"); con gli altri no.

Altri dati disponibili (nel perimetro, dove il form li chiedeva):

- **Budget:** 30-50k: 167 · 20-30k: 56 · sotto i 20-30k: 172 · oltre 50k: 12 · espresso come rata mensile: 129 · non dichiarato: 744. **Una buona parte del budget dichiarato è sotto la soglia dei 35'000 franchi.**
- **Tipo di auto:** SUV/crossover 287 · berlina 148 · station wagon 70 · elettrica/ibrida 63 · city car 46 · sportiva 15.
- **Marche richieste** (dove c'è il modello): Audi 88 · Mercedes 88 · BMW 45 · Alfa Romeo 40 · VW 33 · Fiat/Jeep 29 · Toyota 23 · poi Skoda, Ford, BYD/MG, Hyundai/Kia, Porsche.
- **Tempistica dichiarata:** entro 1 mese 256 · 1-3 mesi 76 · sto valutando 125. Erano dichiarazioni di 6-12 mesi fa: chi diceva "subito" a marzo nel frattempo ha comprato o rinunciato.
- **Permuta:** sì 115 · no 83 (solo dove il form lo chiedeva).

## 6. Dove vivono (stima dal campo città)

| Regione | Lead nel perimetro |
|-|-:|
| Ticino / Grigioni italiano | 516 |
| Svizzera tedesca (compilato in italiano) | 617 |
| Romandia (compilato in italiano) | 103 |
| Italia | 22 |
| Non indicata | 22 |

**Quasi la metà sono italofoni che vivono fuori dal Ticino.** È un pubblico diverso da quello del brief ("solo Ticino"), con riferimenti e distanze diverse. Va tenuto presente nei copy: niente riferimenti solo ticinesi, consegna con trasportatore.

## 7. Chi li ha lavorati

Loris 359 · Valentino 129 · Simone 104 · Riccardo 78 · Giuseppe 13 · Paolo 6 · nessun consulente indicato 591.

## 8. Cose da chiarire (le domande sono anche nel file Excel per Loris)

1. **Legenda colori.** La legenda nel foglio (Da chiamare, Passato, Doppio, Posticipato, Da riattivare, Interessato, Concluso, Eliminato) copre solo una parte dei colori usati. Fuori legenda ci sono rosso (numero non valido?), arancione, verde acceso, azzurro nelle note e un grigio chiaro steso su interi fogli. Nessun lead è segnato "Da riattivare" o "Concluso".
2. **Esiti in GoHighLevel.** Per circa 250 lead (29MAG, 15APR, 15MAG, 21OTT, 26OTT) e per i lead "CRM" il file non dice niente. Con un export di GoHighLevel (stage + note) la segmentazione diventa molto più precisa.
3. **Clienti che hanno comprato.** Nel file risulta **1 sola vendita** (colonna Vendita). Quanti di questi lead sono diventati clienti? Abbiamo deciso di contattarli, ma con un messaggio che non dica "ci avevi lasciato il contatto per un'auto".
4. **Lead di ottobre-novembre 2026 (77).** Sono ancora in lavorazione? Rischio di riattivare qualcuno che Loris sta chiamando in questi giorni.
5. **Consenso WhatsApp.** I form Meta chiedevano il consenso ai messaggi WhatsApp? Conta per il rischio di blocco del numero (tappa 4).
6. **Romandia (103) e Svizzera tedesca (617).** Confermiamo che chi ha compilato in italiano parla italiano? Loris parla francese?
7. **Consulenti fuori contesto:** chi sono Valentino, Riccardo e Paolo? Valentino parla tedesco? Se sì, i 151 lead tedeschi non sono per forza persi.
8. **Colonna Chat:** 193 link a Google Doc. Sono trascrizioni delle conversazioni? Se sì, sono oro per la tappa 3 (voce dei lead).
9. **Colonna Scoring:** che scala è (valori da 0 a 60)?

## 9. Prime impressioni (da verificare nella tappa 2)

- **Un messaggio unico per tutti spreca il dato migliore che abbiamo:** per 413 lead sappiamo l'auto. Un richiamo specifico ("cercavi una Q5") è molto più forte di "ci avevi scritto per un'auto".
- **Le famiglie sono pubblici diversi**, non solo campagne diverse: Prezzo Basso = gente che è stata chiamata e ha parlato (290 conversazioni) · Auto ITA e Profilazione = lead con budget dichiarato, spesso basso · Modulo Acquisto = nessun dato sull'auto, solo frustrazione verso i concessionari, che è esattamente l'angolo del brief.
- **Il 41% senza note** e il 21% mai raggiunto sono, di fatto, lead "freddi mai lavorati": per loro la riattivazione è un primo contatto più che un richiamo.
