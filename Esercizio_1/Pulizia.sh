#!/bin/bash


#               Eliminazione di tutti i file di testo


if ls *Sciocchino* &>/dev/null; then
    rm -f *Sciocchino*
else
    echo "Nessun file 'Sciocchino' trovato nella directory corrente."
fi

#               Eliminazione di tutte le directory con "Sciocchino" nel nome
if ls -d *Sciocchino*/ &>/dev/null; then
    rm -rf *Sciocchino*/
else
    echo "Nessuna directory 'Sciocchino' trovata nella directory corrente."
fi

echo "Tutti gli elementi 'Sciocchino' sono stati eliminati"



#			THE END

