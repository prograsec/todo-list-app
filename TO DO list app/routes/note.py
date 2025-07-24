from fastapi import APIRouter, Request, Form
from models.note import Note
from config.db import conn
from schemas.note import noteENTITY, notesENTITY
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from bson import ObjectId  # Make sure to import this if using MongoDB ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")


# HTML GET route
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.todo.Notes.find({})  # corrected: conn.todo.Notes -> conn.notes.notes
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "Title": doc.get("Title", ""),
            "Discription": doc.get("Discription", ""),
            "Important": doc.get("Important", False),
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


# JSON POST route
@note.post("/")
def add_item(note: Note):
    inserted_note = conn.todo.Notes.insert_one(dict(note))
    return noteENTITY(conn.todo.Notes.find_one({"_id": inserted_note.inserted_id}))


# HTML form POST route
@note.post("/create", response_class=HTMLResponse)
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    
    # Correct Boolean parsing
    formDict["Important"] = True if formDict.get("Important") == "on" else False
    
    # Optional: type casting (if needed)
    formDict["Title"] = formDict.get("Title", "")
    formDict["Discription"] = formDict.get("Discription", "")

    conn.todo.Notes.insert_one(formDict)
    return templates.TemplateResponse("success.html", {"request": request, "message": "Note added successfully"})
