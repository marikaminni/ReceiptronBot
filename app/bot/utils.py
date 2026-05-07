"""Return info from parsed data and receipt id"""
def format_message_receipt(parsed_data: dict, receipt_id: int) -> str:
    return(
        "✅ Scontrino salvato!\n\n"
        "Recap: \n\n"
        f"- ReceiptID: {receipt_id}\n"
        f"- Date: {parsed_data['date']}\n"
        f"- Negozio: {parsed_data['negozio']}\n"
        f"- Categoria: {parsed_data['category']}\n"
        f"- Totale: € {parsed_data['total']:.2f}\n"
    )
"""Return filtered data from db based on period of filtering"""
def format_db_filter(db_data) -> str:
    recap= "Recap totale per categoria: \n"
    for data in db_data:
        recap += f"- {data["category"]}: €{data["Total"]}\n"

    return recap
