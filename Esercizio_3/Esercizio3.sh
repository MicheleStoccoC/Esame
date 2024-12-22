#!/bin/bash

#             Definizione di 'file_count'
file_count() {
    local count
    count=$(ls -p | grep -v "/" | wc -l)
    # Da manuale: 'ls -p': identifica le directories con un contrassegno/, 'grep -v "/"': inverte l'azione e non prende il contrassegno /, 'wc -l': conta le linee prese da grep. 
    echo "Numero di file nella directory corrente: $count"
}



# il numero di files viene scelto dall'utente all'esecuzione del programma, controllo dell'input
if [ -z "$1" ]; then
    echo "Errore: specificare il numero di dummy files da creare come argomento."
    exit 1
fi

#             Generazione 2 cartelle 'Sciocchino'
for ((i=1; i<=2; i++)); do
        mkdir "Sciocchino_$i"
done

#             Generazione dei file 'Sciocchino'
num_files=$1
for ((i=1; i<=num_files; i++)); do
    touch "Sciocchino_$i.txt"
done

echo "File e cartelle di test: creati."


#             Chiamata di file_count
file_count

#la funzione mostra direttamente il risultato a schermo, non serve mettere valori di 'return'. Anche se la ridondanza a volte non è un male...



#			THE END

