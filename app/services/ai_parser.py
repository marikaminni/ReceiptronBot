import json
from google import genai
from google.genai import types
from config import GEMINI_KEY


client= genai.Client(api_key=GEMINI_KEY)

def parse_receipt(image_path: str)-> dict:
    with open(image_path, 'rb') as f:
        image_bytes = f.read()

    prompt= """
    Analizza questo scontrino ed estrai le seguenti informazioni in formato JSON:
    - date: data di emissione dello scontrino in formato YYYY-MM-DD
    - negozio: il negozio da cui è stato emesso
    - category: la categoria dell negozio ad esempio cura della persona, estetica, alimentari, farmacia, visite mediche, svago, ristoranti, shopping, altro
    - total: il totale dello scontrino espresso come numero decimale
    
    Rispondi SOLO con JSON grezzo, senza markdown, senza backtick, senza testo aggiuntivo.
    """
    response = client.models.generate_content(
        model= 'gemini-2.5-flash',
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type='image/jpeg',
            ),
            prompt
        ]
    )
    return json.loads(response.text.strip())
