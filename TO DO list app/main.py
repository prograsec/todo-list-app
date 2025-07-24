from fastapi import FastAPI
from routes.note import note  # Adjust the import based on your folder

app = FastAPI()

app.include_router(note)
