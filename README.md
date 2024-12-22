#           ESAME ABILITA' INFORMATICHE E TELEMATICHE
# AUTHOR: Michele Stocco Calzavara

Qui vengono caricati gli esercizi per l'esame di Abilità Informatiche e Telematiche

Ho scelto di eseguire gli esercizi bash  numero: 1, 3, 6, 8. Assieme all'esercizio 9 in Python. 



#           Esercizio1
    BREVE SOMMARIO
-) L'esercizio 1 chiede di generare file e rinominarli aggiungendo la data odierna. Nel programma sono stati implementati vari comandi tra i quali "date" per l'inserimento della data, "find" per trovare i file e differenziarli da eventiali directory, "mv" per rinominarli.


    ESECUZIONE DEL PROGRAMMA
1) L'utilizzatore ha bisogno dell'autorizzazione per eseguire il programma, questa si può implementare con il comando "chmod u+x Esercizio1.sh" prima di eseguire il file.

2) Il programma richiede un numero N  di file da generare a discrezione dell'esecutore; questo numero deve essere specificato all'avvio del programma (e.g. "./Esercizio1.sh N"); in ogni caso se questo numero non sarà specificato il programma ritorna un messaggio di errore.

3) Il programma stampa tutto a schermo, se non si vuole intasare il terminale si può redirezionare l'output in un file log: "./Esercizio1.sh N &> LOG"; anch'esso verrà rinominato con la data odierna, in questo modo si può tenere traccia degli output del programma se viene eseguito più volte in giorni differenti.

4) Il programma genera anche 2 cartelle 'Sciocchino' in modo da dimostrare che riesce a distinguerle dai file e a non rinominarle.

5) A programma eseguito si può verificare il risultato semplicemente con il comando "ls -1".

6) Infine il programma prende i due file eseguibili e li riporta al nome originale in modo da lasciarli inalterati.


    PULIZIA DELLA CARTELLA
-) Per evitare inutili perdite di tempo ho aggiunto anche un programma che rimuove direttamente tutti gli elementi 'Sciocchino' (file e cartelle). Anche questo ha bisogno dei permessi di esecuzione del punto 1).

-) Nota: stranamente il programma stampa a schermo che non può eliminare le directory ma alla fine lo fa lo stesso (da investigare...).



#           Esercizio3
    BREVE SOMMARIO



#           Esercizio6
    BREVE SOMMARIO



#           Esercizio8
    BREVE SOMMARIO




#           Esercizio 9


