# Riattivazione WhatsApp: cosa impostare su GoHighLevel

Ciao Ivan, dobbiamo mandare **un messaggio WhatsApp** a circa 1.265 lead vecchi.
Ci sono **3 versioni** del messaggio. Il file ti dice quale versione va a ogni lead.

Ti serve il file **`Riattivazione-import-GHL.csv`** (te lo passo io).

---

## Passo 1 · Crea 3 campi nei contatti

Nelle impostazioni dei campi personalizzati dei contatti, crea 3 campi di testo:

- **Riattivazione Segmento** (conterrà S1, S2 o S3)
- **Riattivazione Auto** (es. "un'Audi Q3")
- **Riattivazione Tipo** (es. "un SUV usato")

## Passo 2 · Importa il file

Importa il CSV nei contatti e collega le colonne:

- Phone, First Name, Last Name, Email → i campi normali
- Riattivazione Segmento, Riattivazione Auto, Riattivazione Tipo → i 3 campi del passo 1
- Tags → Tags
- Le altre colonne non servono: non importarle

Se ti chiede cosa fare con i contatti che esistono già: **aggiornali**, non crearne di nuovi.

Alla fine controlla che i contatti con il tag `riattivazione-nov26` siano **1.265**.

## Passo 3 · Crea i 3 messaggi WhatsApp (template)

Categoria **Marketing**, lingua **Italiano**.
Aggiungi 2 bottoni di risposta rapida: **Sì, cercamela** e **Stop**.

**Messaggio S1**: al posto di `{{1}}` metti il campo *Riattivazione Auto* (esempio per Meta: `un'Audi Q3`)

```
Tra tre anni, quando guarderai la tua auto, cosa vuoi pensare: "che affare" o "che fregatura"?

Ciao, sono Giuseppe, fondatore di ekkecars. Qualche mese fa ci avevi lasciato il contatto per {{1}}.

Un'auto così non si compra tutti gli anni. Ci arrivi dopo anni di lavoro. Eppure spesso la si prende di fretta, al concessionario sotto casa, al prezzo che ti fanno, con un leasing pensato per chiudere il contratto e non per rivenderla bene dopo.

Se quest'anno vuoi farti questo regalo, fattelo come si deve. Se la cerchi ancora, scrivimelo qui: la cerchiamo in tutta Europa, il prezzo lo trattiamo noi e ti troviamo un'offerta migliore.
```

**Messaggio S2**: al posto di `{{1}}` metti il campo *Riattivazione Tipo* (esempio per Meta: `un SUV usato`)

```
Tra tre anni, quando guarderai la tua auto, cosa vuoi pensare: "che affare" o "che fregatura"?

Ciao, sono Giuseppe, fondatore di ekkecars. Qualche mese fa cercavi {{1}}.

Un'auto così non si compra tutti gli anni. Ci arrivi dopo anni di lavoro. Eppure spesso la si prende di fretta, al concessionario sotto casa, al prezzo che ti fanno, con un leasing pensato per chiudere il contratto e non per rivenderla bene dopo.

Se quest'anno vuoi farti questo regalo, fattelo come si deve. Scrivimi qui che modello hai in mente e che rata vuoi spendere: la cerchiamo in tutta Europa, il prezzo lo trattiamo noi e ti troviamo un'offerta migliore. La tua la valutiamo gratis.
```

**Messaggio S3**: nessun campo da collegare

```
Tra tre anni, quando guarderai la tua auto, cosa vuoi pensare: "che affare" o "che fregatura"?

Ciao, sono Giuseppe, fondatore di ekkecars. Qualche mese fa ci avevi lasciato il contatto per un'auto.

Un'auto non si compra tutti gli anni. Ci arrivi dopo anni di lavoro. Eppure spesso la si prende di fretta, al concessionario sotto casa, al prezzo che ti fanno, con un leasing pensato per chiudere il contratto e non per rivenderla bene dopo.

Se quest'anno vuoi farti questo regalo, fattelo come si deve. Scrivimi qui che auto hai in mente: la cerchiamo in tutta Europa, il prezzo lo trattiamo noi e ti troviamo un'offerta migliore.
```

Se Meta rifiuta un messaggio, mandami il motivo e lo sistemiamo.

## Passo 4 · Crea l'automazione di invio

Un workflow che:

1. parte quando aggiungiamo a un contatto il tag `riatt-invia-ora`;
2. guarda il campo *Riattivazione Segmento*:
   - S1 → manda il messaggio S1
   - S2 → manda il messaggio S2
   - S3 → manda il messaggio S3

## Passo 5 · Crea l'automazione per le risposte

Un workflow che parte quando un contatto con il tag `riattivazione-nov26` risponde su WhatsApp:

- se scrive **stop** (o preme il bottone Stop) → non deve ricevere più niente (DND su WhatsApp);
- **qualsiasi altra risposta** → assegna il contatto a **Loris** e mandagli una notifica, così lo chiama.

Loris deve ricevere la notifica **solo alla prima risposta**, non a ogni messaggio.

**Nessun bot o risposta automatica** deve rispondere al posto di Loris.

## Passo 6 · Prova

Crea 3 contatti di prova con i nostri numeri (uno S1, uno S2, uno S3), aggiungi il tag `riatt-invia-ora` e controlla che:

- arrivi il messaggio giusto, con l'auto o il tipo al posto giusto;
- rispondendo "ok" arrivi la notifica a Loris;
- rispondendo "stop" il contatto venga bloccato.

**Mandami gli screenshot** dei 3 messaggi.

## Poi ti fermi

**Non mandare niente ai lead veri.** Giorni e orari degli invii li decidiamo insieme.
Gli invii li faremo a gruppi: nel file ogni lead ha già il suo gruppo (tag da `riatt-ondata-1` a `riatt-ondata-5`).
