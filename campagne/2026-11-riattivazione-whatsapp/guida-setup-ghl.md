# Riattivazione WhatsApp: guida setup su GoHighLevel (messaggio 1)

> Per chi imposta l'automazione. Tempo stimato: mezza giornata, più l'attesa dell'approvazione dei template da parte di Meta (di solito poche ore).
> I nomi dei menu di GoHighLevel possono cambiare leggermente: se una voce non si trova con questo nome, cercala nella stessa sezione.

## Cosa ricevi

- **`Riattivazione-import-GHL.csv`**: 1.265 contatti da importare (Simone te lo passa a parte: contiene i dati personali e non sta nel repo).
- **I 3 testi dei template** (sezione 3).
- Il **calendario delle ondate** (sezione 6), con giorni e orari compilati da Simone.

Cosa facciamo: mandiamo **un solo messaggio** (il primo della sequenza) a 1.265 lead vecchi, in **5 ondate** da circa 250. Ogni lead riceve una di **3 versioni** del messaggio in base al suo segmento. Chi risponde va a Loris; chi scrive stop esce da tutto.

---

## 0. Prima di iniziare (5 minuti)

- [ ] Il numero WhatsApp aziendale è collegato a GoHighLevel e funziona.
- [ ] In WhatsApp Manager (Meta) la **qualità del numero è verde**.
- [ ] **Nessun bot o risposta automatica** attivo sul numero: chi risponde al messaggio deve arrivare a Loris, non a un questionario.

## 1. Crea 5 campi personalizzati (10 minuti)

*Settings → Custom Fields → Contact → Add field.* Tipo: **testo singolo** per tutti.

| Nome del campo | Esempio di valore |
|-|-|
| Riattivazione Segmento | S1 / S2 / S3 |
| Riattivazione Ondata | 1-5 |
| Riattivazione Giorno | lunedì / sabato |
| Riattivazione Auto | un'Audi Q3 (solo S1) |
| Riattivazione Tipo | un SUV usato (solo S2) |

## 2. Importa il file (15 minuti)

*Contacts → Import → carica `Riattivazione-import-GHL.csv`.*

Collega le colonne così:

| Colonna del file | Campo di GoHighLevel |
|-|-|
| Phone | Phone |
| First Name / Last Name | First Name / Last Name |
| Email | Email |
| Riattivazione Segmento, Ondata, Giorno, Auto, Tipo | i 5 campi creati al punto 1 |
| Tags | Tags |
| ID lead, Campagna origine | non importare (servono solo a noi) |

- Se GoHighLevel chiede cosa fare con i contatti già presenti, scegli **aggiornare quelli esistenti** (riconosciuti dal telefono), **non** crearne di nuovi.
- **Controllo dopo l'import** (filtra per tag):
  - `riattivazione-nov26` = **1.265** contatti
  - `riatt-s1` = **298** · `riatt-s2` = **364** · `riatt-s3` = **603**
  - `riatt-ondata-1` … `riatt-ondata-5` = circa **250** ciascuna

## 3. Crea i 3 template WhatsApp (30 minuti + approvazione)

*Settings → WhatsApp → Templates → Create.* Per tutti e 3:
- **Categoria:** Marketing · **Lingua:** Italiano
- **Bottoni (risposta rapida):** `Sì, cercamela` · `Stop`
- Dove c'è `{{1}}`: collegalo al campo indicato e inserisci l'**esempio** che chiede Meta.

### Template `riattivazione_m1_s1`  (variabile `{{1}}` = campo *Riattivazione Auto*, esempio: `un'Audi Q3`)

```
Tra tre anni, quando guarderai la tua auto, cosa vuoi pensare: "che affare" o "che fregatura"?

Ciao, sono Giuseppe, fondatore di ekkecars. Qualche mese fa ci avevi lasciato il contatto per {{1}}.

Un'auto così non si compra tutti gli anni. Ci arrivi dopo anni di lavoro. Eppure spesso la si prende di fretta, al concessionario sotto casa, al prezzo che ti fanno, con un leasing pensato per chiudere il contratto e non per rivenderla bene dopo.

Se quest'anno vuoi farti questo regalo, fattelo come si deve. Se la cerchi ancora, scrivimelo qui: la cerchiamo in tutta Europa, il prezzo lo trattiamo noi e ti troviamo un'offerta migliore.
```

### Template `riattivazione_m1_s2`  (variabile `{{1}}` = campo *Riattivazione Tipo*, esempio: `un SUV usato`)

```
Tra tre anni, quando guarderai la tua auto, cosa vuoi pensare: "che affare" o "che fregatura"?

Ciao, sono Giuseppe, fondatore di ekkecars. Qualche mese fa cercavi {{1}}.

Un'auto così non si compra tutti gli anni. Ci arrivi dopo anni di lavoro. Eppure spesso la si prende di fretta, al concessionario sotto casa, al prezzo che ti fanno, con un leasing pensato per chiudere il contratto e non per rivenderla bene dopo.

Se quest'anno vuoi farti questo regalo, fattelo come si deve. Scrivimi qui che modello hai in mente e che rata vuoi spendere: la cerchiamo in tutta Europa, il prezzo lo trattiamo noi e ti troviamo un'offerta migliore. La tua la valutiamo gratis.
```

### Template `riattivazione_m1_s3`  (nessuna variabile)

```
Tra tre anni, quando guarderai la tua auto, cosa vuoi pensare: "che affare" o "che fregatura"?

Ciao, sono Giuseppe, fondatore di ekkecars. Qualche mese fa ci avevi lasciato il contatto per un'auto.

Un'auto come una GLC o un'A7 non si compra tutti gli anni. Ci arrivi dopo anni di lavoro. Eppure spesso la si prende di fretta, al concessionario sotto casa, al prezzo che ti fanno, con un leasing pensato per chiudere il contratto e non per rivenderla bene dopo.

Se quest'anno vuoi farti questo regalo, fattelo come si deve. Scrivimi qui che auto hai in mente: la cerchiamo in tutta Europa, il prezzo lo trattiamo noi e ti troviamo un'offerta migliore.
```

Se Meta **rifiuta** un template, manda a Simone il motivo esatto del rifiuto: si corregge il testo e si reinvia.

## 4. Crea 2 workflow (30 minuti)

### Workflow A · "Riattivazione M1 – invio"
- **Trigger:** aggiunta del tag `riatt-invia-ora`.
- **If/Else** sul campo *Riattivazione Segmento*:
  - S1 → *Send WhatsApp template* `riattivazione_m1_s1`
  - S2 → *Send WhatsApp template* `riattivazione_m1_s2`
  - S3 → *Send WhatsApp template* `riattivazione_m1_s3`
- Poi: **aggiungi tag** `riatt-m1-inviato` e **togli** il tag `riatt-invia-ora`.

### Workflow B · "Riattivazione – risposte"
- **Trigger:** *Customer replied* sul canale WhatsApp, con filtro: tag `riattivazione-nov26`.
- **If/Else** sul testo della risposta:
  - contiene `stop` (anche il bottone *Stop*) → **attiva DND su WhatsApp** + tag `riatt-stop`. Fine.
  - tutto il resto → tag `riatt-risposto`, **assegna a Loris**, **notifica interna a Loris** ("Lead riattivazione ha risposto: chiamalo") e, se lo usate, apri l'opportunità nella pipeline vendite.
- Il workflow deve partire **solo alla prima risposta**: se il lead scrive più messaggi, Loris non deve ricevere 5 notifiche.

## 5. Test prima dell'invio vero (10 minuti)

- Crea **3 contatti di prova** con i vostri numeri: uno S1 (Auto = `un'Audi Q3`), uno S2 (Tipo = `un SUV usato`), uno S3.
- Aggiungi il tag `riatt-invia-ora` ai 3 contatti di prova e controlla che:
  - [ ] arrivi il template giusto, con la parola al posto giusto ("…per un'Audi Q3.");
  - [ ] rispondendo "ok" scatti la notifica a Loris;
  - [ ] rispondendo "stop" (o premendo il bottone) il contatto vada in DND.
- **Manda a Simone gli screenshot** dei 3 messaggi ricevuti prima di partire con l'ondata 1.

## 6. Invio delle ondate

Per ogni ondata, al giorno e all'ora stabiliti: *Contacts → filtro tag `riatt-ondata-N` → seleziona tutti → Add tag `riatt-invia-ora`.* Il workflow A fa il resto.

| Ondata | Contatti | Giorno (test) | Data | Ora |
|-|-:|-|-|-|
| 1 | 254 | lunedì | __ / __ | __:__ |
| 2 | 254 | sabato | __ / __ | __:__ |
| 3 | 254 | lunedì | __ / __ | __:__ |
| 4 | 252 | sabato | __ / __ | __:__ |
| 5 | 251 | lunedì | __ / __ | __:__ |

- **Massimo un'ondata al giorno**, così Loris riesce a richiamare chi risponde.
- Ogni ondata ha gli stessi segmenti nelle stesse proporzioni, così il confronto tra lunedì e sabato è pulito.
- Mai invii prima delle 8 o dopo le 21.

## 7. Durante le ondate

- Ogni giorno: guarda la **qualità del numero** in WhatsApp Manager. Se passa a **gialla o rossa**, ferma le ondate successive e avvisa Simone.
- Fine di ogni ondata: manda a Simone **quanti inviati, quanti consegnati, quante risposte, quanti stop**.

## Fuori da questa guida

- **7 lead con numero fisso** (niente WhatsApp): file `Riattivazione-solo-chiamata.csv`, li chiama direttamente Loris.
- I messaggi dal 2 al 5 si decidono dopo aver visto i risultati del primo.
