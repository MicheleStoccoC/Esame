#           ESAME ABILITA' INFORMATICHE E TELEMATICHE
# AUTHOR: Michele Stocco Calzavara

Qui vengono caricati gli esercizi per l'esame di Abilità Informatiche e Telematiche

Ho scelto di eseguire gli esercizi bash  numero: 1, 3, 6, 8. Assieme all'esercizio 9 in Python. 



#           Esercizio1
    BREVE SOMMARIO
-) L'esercizio 1 chiede di generare file e rinominarli aggiungendo la data odierna. Nel programma sono stati implementati vari comandi tra i quali "date" per l'inserimento della data, "find" per trovare i file e differenziarli da eventiali directory, "mv" per rinominarli.


     ESECUZIONE DEL PROGRAMMA
1) L'utilizzatore ha bisogno dell'autorizzazione per eseguire il programma, questa si può implementare con il comando "chmod u+x Esercizio1.sh" prima di eseguire il file.

2) Il programma richiede un numero N di file da generare a discrezione dell'esecutore; questo numero deve essere specificato all'avvio del programma (e.g. "./Esercizio1.sh N"); in ogni caso se questo numero non sarà specificato il programma ritorna un messaggio di errore.

3) Il programma stampa tutto a schermo, se non si vuole intasare il terminale si può redirezionare l'output in un file log: "./Esercizio1.sh N &> LOG"; anch'esso verrà rinominato con la data odierna, in questo modo si può tenere traccia degli output del programma se viene eseguito più volte in giorni differenti.

4) Il programma genera anche 2 cartelle 'Sciocchino' in modo da dimostrare che riesce a distinguerle dai file e a non rinominarle.

5) A programma eseguito si può verificare il risultato semplicemente con il comando "ls -1".

6) Infine il programma prende i due file eseguibili e li riporta al nome originale in modo da lasciarli inalterati.


    PULIZIA DELLA CARTELLA
-) Per evitare inutili perdite di tempo ho aggiunto anche un programma che rimuove direttamente tutti gli elementi 'Sciocchino' (file e cartelle). Anche questo ha bisogno dei permessi di esecuzione del punto 1).

-) Nota: stranamente il programma stampa a schermo che non può eliminare le directory ma alla fine lo fa lo stesso (da investigare...).



#           Esercizio3
    BREVE SOMMARIO
-) L'esercizio 3 chiede di generare file in una cartella e di creare una funzione che li conti.


    ESECUZIONE DEL PROGRAMMA
1) L'utilizzatore ha bisogno dell'autorizzazione per eseguire il programma, questa si può implementare con il comando "chmod u+x Esercizio3.sh" prima di eseguire il file.

2) Il programma richiede un numero N di file da generare a discrezione dell'esecutore; questo numero deve essere specificato all'avvio del programma (e.g. "./Esercizio3.sh N"); in ogni caso se questo numero non sarà specificato il programma ritorna un messaggio di errore.

3) Il programma stampa tutto a schermo, se non si vuole intasare il terminale si può redirezionare l'output in un file log: "./Esercizio3.sh N &> LOG"; nota: anch'esso verrà contato da 'file count'.

4) Il programma genera anche 2 cartelle 'Sciocchino' in modo da dimostrare che riesce a distinguerle dai file e a non conteggiarle.

5) A programma eseguito si può verificare il risultato semplicemente con il comando "ls -1".


    PULIZIA DELLA CARTELLA
-) Per evitare inutili perdite di tempo ho aggiunto anche un programma che rimuove direttamente tutti gli elementi 'Sciocchino' (file e cartelle). Anche questo ha bisogno dei permessi di esecuzione del punto 1).


#           Esercizio6
    BREVE SOMMARIO
-) L'esercizio 6 chiede di generare un file e modificare una delle parole in loco attraverso il comando 'gawk'.


    ESECUZIONE DEL PROGRAMMA
1) L'utilizzatore ha bisogno dell'autorizzazione per eseguire il programma, questa si può implementare con il comando "chmod u+x Esercizio6.sh" prima di eseguire il file. 

2) Per verificare l'effettivo cambiamento del file il programma ne stampa sul terminale la prima versione da confrontare successivamente aprendo il file "memory control.txt"; se non si vuole intasare il terminale si può redirezionare l'output in un file log: "./Esercizio6.sh &> LOG".

3) Alla riga 18 il comando è stato compresso. La sintassi utilizzata permette a "gawk" di scrivere solamente la riga che ha identificato (i.e. scrive solo la riga 'MaxMem 512'), il valore '1' all'esterno impone una nuova condizione a "gawk" sempre vera che gli impone di applicare l'azione di default ossia scrivere l'intera linea: in questo modo il comando legge e riscrive ogni linea lasciandola invariata finché non trova la stringa indicata ('MaxMem') e sostisuisce il valore della seconda colonna.

4) E' stato utilizzato un file temporaneo di supporto in modo da non agire direttamente su 'memory control.txt': in caso di problemi durante l'esecuzione il file originario non viene toccato\rovinato; il contenuto del file temporaneo viede poi sovrascritto su 'memory control.txt' e l'effetto cumulativo è quello di una sostituzione in loco del valore '512' in '1024'.

5) Nel caso si volesse rimuovere il file appena creato si può utilizzare il comando "rm memory_control.txt".


#           Esercizio8
    BREVE SOMMARIO
-) L'esercizio 8 chiede di entrare in una cartella e conteggiare gli elementi presenti distinguendoli in file, directories e file vuoti.

    ESECUZIONE DEL PROGRAMMA
1) L'utilizzatore ha bisogno dell'autorizzazione per eseguire il programma, questa si può implementare con il comando "chmod u+x Esercizio6.sh" prima di eseguire il file.

2) Il programma ha bisogno di un argomento per poter essere eseguito; se questo viene fornito si blocca e fornisce un messaggio di errore; l'argomento deve essere una directory, se non lo è il programma si blocca comunque e fornisce un messaggio di errore. Inserimento dell'argomento: "./Esercizio8 Directory"

3) Il programma stampa tutti i risultati sul terminale, il consiglio e quello di reindirizzare gli output in un file log: "./Esercizio8.sh Directory &> LOG8".

4) Il programma non mostra tutta la sua efficacia nella cartella 'Esercizio_8' (si può provare ad eseguirlo con il nome di una cartella esterna e osservare il risultato).      Si consiglia di muovere il file nella directory 'Esame', eseguire il file 'Esercizio3.sh' nella rispettiva directory, NON utilizzare il file 'Pulizia.sh' ed infine eseguire il comando "./Esercizio8.sh Esercizio_3 &> LOG8".



#           Esercizio 9
    BREVE SOMMARIO




