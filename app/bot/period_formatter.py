import re

def get_number(text: str) -> str:
    """usa re per estrarre il numero, a questo se c'è un numero, allora ritorna quel numero
    altrimenti ritorna 1, così che:
    - se ho n-periodo: farò n*periodo (ultimi 2 settimane -> 2*14)
    - se il numero di giorni è già in stringhe (es. ultimi dieci giorni)
    - se non specifico il numero ma ho periodo tipo ultima settimana/mese/anno (ritornerà 1*7 o *30 o *365 todo: e per anno bisestile?)
    - se specifico numero ma ho solo giorno (es. ultimo giorno)
    - todo: se non specifico periodo es. ultimi giorni/settimane, fare un handler o altro per dire di specificarli
    - todo: vedere se fare opzione anche ultime 24h o comunque con orari
    - todo: gestisci errori su input non supportato
    """
    pattern= r"\d+"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()
    else:
        return "1"

def convert_period(text: str) -> int:
    #todo: trova altro metodo per non considerare plurali, normalizzare stringa
    time_period = {
        "settimana": 7,
        "settimane": 7,
        "mese": 30,
        "mesi": 30,
        "anno": 365,
        "anni": 365,
    }

    #verifica se la chiave del dizionario è presenta nella stringa di testo passata
    expression= (time_period[key] for key in time_period if key in text)

    return next(expression, 1) #se la stringa non è presente ritorna 1 come default


def period_formatter(period: str) -> int:
    text = str(period).lower()

    n_period= int(get_number(text))
    literal_period = convert_period(text)

    return n_period * literal_period