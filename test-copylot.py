import PyPDF2
import pdfplumber
import re

# Funzione per estrarre domande e risposte da un file PDF
def stampa_domande_risposte(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            testo_pagina = page.extract_text()
            domande, risposte = separa_domande_risposte(testo_pagina)
            print(domande)
            # for domanda in domande:
            #     with open('domande.txt', 'a') as file:
            #         file.write(domanda)
            # for risposta in risposte:
            #     with open('risposte.txt', 'a') as file:
            #         file.write(risposta)

def extract_year(text):
    pattern = r'\b\d{4}\b'  # Matches a 4-digit number
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None
    
def separa_domande_risposte(testo):
    domande = []
    risposte = []
    # Dividi il testo in righe
    righe = testo.split('?')
    domanda_corrente = None
    risposte_correnti = []
    for riga in righe:
        riga = riga.strip()
        # Se la riga inizia con un numero seguito da un punto, è una domanda
        if riga.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            # Se abbiamo già raccolto una domanda, aggiungiamola alla lista
            if domanda_corrente is not None and risposte_correnti:
                domande.append(domanda_corrente)
                risposte.append(risposte_correnti)
            # Impostiamo la nuova domanda
            domanda_corrente = riga
            risposte_correnti = []
        # Se la riga inizia con una lettera maiuscola seguita da una parentesi, è una risposta
        elif riga.startswith(("A)", "B)", "C)", "D)", "E)")):
            # Aggiungiamo la risposta corrente alla lista
            risposte_correnti.append(riga)
    # Aggiungiamo l'ultima domanda e le relative risposte alla fine del testo
    if domanda_corrente is not None and risposte_correnti:
        domande.append(domanda_corrente)
        risposte.append(risposte_correnti)
    return domande, risposte




# Nome del file PDF contenente le domande e le risposte
file_pdf = 'CompitoMedicina2022.pdf'

# Stampare domande e risposte dal file PDF
stampa_domande_risposte(file_pdf)
