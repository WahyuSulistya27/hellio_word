from fastapi import FastAPI
from connect import *
import add, check, edit, delete, search

app = FastAPI()

app.include_router(check.router)
app.include_router(search.router)
app.include_router(add.router)
app.include_router(edit.router)
app.include_router(delete.router)