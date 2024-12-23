#!/bin/bash

#                          Controllo argomento ed esistenza
if [ -z "$1" ]; then
    echo "Errore: nessun argomento fornito, inserire una directory."
    exit 1
else
	if [ ! -d "$1" ]; then
		echo "Errore: l'argomento fornito ($1) non è una directory o non esiste nella directory corrente."
		exit 2
	fi
fi

#                          Entra nella directory
cd "$1"

echo "Sei nella directory: $(pwd)"
echo ""

#                          Elenco dei file
echo "Elenco dei file presenti:"
find . -maxdepth 1 -type f -printf "%f\n" # 'f': qualsiasi tipo di file non directory
echo ""

#                          Elenco delle directories
echo "Elenco delle directories:"
find . -maxdepth 1 -type d ! -path .  -printf "%f\n" # 'd': individua le directories, '! -path .': nonprende in considerazione la directory corrente
echo ""

#                          Elenco dei file vuoti
echo "Elenco dei file vuoti:"
find . -maxdepth 1 -type f -empty -printf "%f\n" # '-empty': autoesplicativo
echo ""



#			THE END
