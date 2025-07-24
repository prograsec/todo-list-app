def noteENTITY(item) -> dict:
 return {
    "id": str(item["_id"]),
    "Title": item["Title"],
    "Discription": item ["Discription"],
    "Important": item["Importan"],
}
def notesENTITY(item) -> list :
  return[notesENTITY(item) for item in item ],