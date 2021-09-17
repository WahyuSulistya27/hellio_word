from fastapi import APIRouter
from data import dokumen as list_dokumen
from starlette.responses import Response
from connect import *
from model import *

router = APIRouter()
dokumen = list_dokumen

@router.delete("/delete/{noreg}", status_code=201)
async def delete_dokumen(noreg : int):
    try:
        cursor.execute("DELETE FROM tb_document WHERE noreg=?" ,noreg) 
        cursor.commit()
    except Exception as e:
        print(e)
    
    return "Dokumen Anda Telah Dihapus"