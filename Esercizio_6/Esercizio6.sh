#!/bin/bash

#                     Creazione del file di testo

echo "# control of memory requirements
BoundaryLayerFactor 3. 0
MaxMem 512
MaxMemPerParticle 240
PredPeakFactor 0. 8" > memory_control.txt #nota: in questo caso echo prende già i \n senza bisogno di inserirli

echo "File 'memory_control.txt' creato:"
cat memory_control.txt
echo ""


#                     Modifica in loco del valore di MaxMem usando gawk

gawk '{if ($1 == "MaxMem") $2 = 1024}1' memory_control.txt > temporaneo && mv temporaneo memory_control.txt # '1' aggiunge una nuova condizione sembre vera: stampa di ogni altra righa.

echo "Valore di MaxMem modificato da 512 a 1024 in 'memory_control.txt'."
