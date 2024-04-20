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

# Testiamo la funzione con il testo della domanda che hai fornito
testo_domanda = """
1. «L'insulino-resistenza non è di per sé una malattia, ma si accompagna frequentemente a
una serie di fattori di rischio cardiovascolare inclusi nella definizione generale di
«sindrome metabolica». Essi comprendono obesità viscerale, diabete, aumento di
trigliceridi e colesterolo, ipertensione arteriosa. Nelle condizioni di insulino-resistenza
viene alterata la flessibilità metabolica: la capacità del muscolo di utilizzare
alternativamente carboidrati o grassi a seconda della disponibilità dei substrati energetici
risulta insufficiente.
I soggetti affetti da insulino-resistenza hanno una ridotta capacità di utilizzazione dei
grassi nelle condizioni di digiuno e l'aumentata produzione di insulina non è comunque in
grado di stimolare la metabolizzazione degli zuccheri.»
(dal sito web del Ministero italiano della Salute: www.salute.gov.it)
Secondo il testo, che cosa si intende per «flessibilità metabolica»?
A) L’abilità del tessuto muscolare ad utilizzare energia, a seconda delle disponibilità
dell’organismo, da grassi o da zuccheri
B) La scioltezza muscolare garantita da un giusto apporto nutritivo di grassi e carboidrati
C) L’insieme di fattori metabolici che possono provocare un’insufficienza muscolare
generalizzata
D) L’incapacità dell’apparato muscolare di trarre energia dai carboidrati ingeriti con
l’alimentazione
E) La flessione patologica
"""

domande, risposte = separa_domande_risposte(testo_domanda)
print("Domande:")
for domanda in domande:
    print(domanda)
print("\nRisposte:")
for risposte_domanda in risposte:
    for risposta in risposte_domanda:
        print(risposta)
