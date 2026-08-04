Analisi dei mittenti email
Descrizione

Questo programma analizza un archivio di messaggi email in formato mbox e individua il mittente che ha inviato il maggior numero di messaggi.

Il programma legge il file di testo, estrae gli indirizzi email dalle righe che iniziano con From , calcola la frequenza di ogni mittente e restituisce quello con il numero più alto di email.

Funzionalità
Lettura di file di testo in formato mbox.
Estrazione degli indirizzi email dei mittenti.
Conteggio delle occorrenze tramite dizionari.
Ricerca del mittente più frequente.
Visualizzazione del risultato finale.
Tecnologie e concetti utilizzati
Python 3
Gestione dei file (open)
Liste e dizionari
Manipolazione di stringhe
Cicli e condizioni
Conteggio delle frequenze
Utilizzo

Eseguire il programma:

python main.py

Inserire il nome del file mbox da analizzare quando richiesto.

Esempio:

Enter file name: mbox-short.txt

Output:

cwen@iupui.edu 5
Dataset

Il programma è stato sviluppato utilizzando un archivio email in formato mbox fornito come esercizio didattico nel corso Python for Everybody.

Possibili miglioramenti
Aggiungere una gestione più specifica degli errori di apertura file.
Utilizzare collections.Counter per semplificare il conteggio.
Aggiungere statistiche aggiuntive sui messaggi analizzati.
