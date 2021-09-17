from fastapi import APIRouter
from starlette.routing import Router
from data import dokumen as list_dokumen
from connect import *
from model import *
from starlette.responses import Response

router = APIRouter()
dokumen = list_dokumen

def mssql_result2dict(cursor):
    try: 
        result = []
        columns = [column[0] for column in cursor.description]
        for row in  cursor.fetchall():
            result.append(dict(zip(columns,row)))

        print(result)

        if len(result) > 0:
            ret = result
        else:
            ret = {"message": "no results found"}
    except pyodbc.Error as e:
        print(e)
        ret = { "message": "Internal Database Query Error"}
    
    return ret

@router.get("/search/{noreg}", status_code=201)
async def search_dokumen_by_noreg(noreg : int,  response: Response):
        
    try :
        cursor.execute ("SELECT * FROM tb_document WHERE noreg=?", noreg)
        ret = mssql_result2dict(cursor)
        conn.commit()
    except pyodbc.Error as e:
        print('SQL Query Failed : {e}')
        ret = {"message": "system error"}
    return ret