import os
from typing import List
import json
from pathlib import Path
#github

def lese_datei_und_zaehle_buchstaben(dateipfad):
    with open(dateipfad, 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
        anzahl_buchstaben = sum(c.isalpha() for c in inhalt)  # Counts all characters
        return inhalt, anzahl_buchstaben

def splitte_datei_in_chunks(inhalt, max_anzahl_buchstaben):
    chunk_index = 0
    start_index = 0
    chunks = []
    buchstaben_zaehler = 0
    aktueller_chunk = []

    for c in inhalt:
        if c.isalpha():
            buchstaben_zaehler += 1
        aktueller_chunk.append(c)

        if buchstaben_zaehler >= max_anzahl_buchstaben:
            chunks.append(''.join(aktueller_chunk).replace('\n', ' ').replace('\r', ''))
            aktueller_chunk = []
            buchstaben_zaehler = 0

    if aktueller_chunk:
        chunks.append(''.join(aktueller_chunk).replace('\n', ' ').replace('\r', ''))

    return chunks

def schreibe_chunks_in_dateien(chunks: List[str]) -> None:
    ordner = 'out'
    os.makedirs(ordner, exist_ok=True)
    
    for index, chunk in enumerate(chunks):
        dateiname = os.path.join(ordner, f'output_chunk_{index + 1:03}.txt')
        #inhalt = f"fasse im detail zusammen und erkläre alles: {chunk.replace('\n', ' ').replace('\r', '')}"
        new_chunk = chunk.splitlines()
        inhalt = "fasse im detail zusammen und erkläre alles: ".join(new_chunk)
        with open(dateiname, 'w', encoding='utf-8') as datei:
            datei.write(inhalt)
        print(f'Datei {dateiname} wurde erstellt.')

def main():
    dirname = os.path.dirname(__file__)
    print(dirname)
    dateipfad = os.path.join(dirname, 'input.txt')

    max_anzahl_buchstaben = 14100
    
    inhalt, anzahl_buchstaben = lese_datei_und_zaehle_buchstaben(dateipfad)
    print(f'Gesamtanzahl der Buchstaben in der Datei: {anzahl_buchstaben}')

    if anzahl_buchstaben > max_anzahl_buchstaben:
        chunks = splitte_datei_in_chunks(inhalt, max_anzahl_buchstaben)
        schreibe_chunks_in_dateien(chunks)
    else:
        chunks = splitte_datei_in_chunks(inhalt, max_anzahl_buchstaben)
        schreibe_chunks_in_dateien(chunks)

if __name__ == '__main__':
    main()