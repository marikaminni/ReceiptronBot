def format_message_receipt(parsed_data: dict, receipt_id: int) -> str:
    return(
        "✅ Scontrino salvato!\n\n"
        "Recap: \n\n"
        f"- Receipt:ID: {receipt_id}\n"
        f"- Date: {parsed_data['date']}\n"
        f"- Negozio: {parsed_data['negozio']}\n"
        f"- Categoria: {parsed_data['category']}\n"
        f"- Totale: € {parsed_data['total']:.2f}\n"
    )