import pandas as pd
from data import dokumen as list_dokumen
from starlette.responses import Response
from connect import *
from model import *
from fastapi import APIRouter

router = APIRouter()
dokumen = list_dokumen

@router.get("/check/{noreg}", status_code=200)
async def check_dokumen_by_noreg(noreg: int, response: Response):
        sql = "SELECT * FROM tb_document WHERE noreg=?"
        result = pd.read_sql (sql, conn, params=[noreg])
        return result