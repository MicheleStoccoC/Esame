#!/bin/bash


#               Creazione dei dummy files

# il numero di files viene scelto dall'utente all'esecuzione del programma, controllo dell'input
if [ -z "$1" ]; then
    echo "Errore: specificare il numero di dummy files da creare come argomento." 
    exit 1
fi

# generazione 2 directory vuote
for ((i=1; i<=2; i++)); do
	mkdir "Sciocchino_$i"
done

# generazione file
num_files=$1
for ((i=1; i<=num_files; i++)); do
    touch "Sciocchino_$i.txt"
done

echo "$num_files files creati nella directory corrente."


#               Creazione dell'array con tutti i file presenti

# Da "man file". -maxdepth: cerca solo nei livelli inseriti (1=livello corrente), type: cerca solo file di una certa tipologia (f=file), printf: scrive il file nell'array
files=($(find . -maxdepth 1 -type f -printf "%f\n"))

#               Controllo riempimento
if [ ${#files[@]} -eq 0 ]; then
    echo "Nessun file trovato nella directory corrente."
else
    echo "${#files[@]} file trovati:"
    for file in "${files[@]}"; do
        echo "$file"
    done

    #           Rinomina di tutti i file con data odierna
    current_date=$(date +%Y-%m-%d)
    for file in "${files[@]}"; do
        mv "$file" "$current_date-$file" # "move" per rinominare
    done

    echo "Tutti i file sono stati rinominati aggiungendo la data odierna: $current_date"
fi


#	Ripristino nomi file importanti
mv "$current_date-Esercizio1.sh" "Esercizio1.sh"
mv "$current_date-Pulizia.sh" "Pulizia.sh"



#			THE END




