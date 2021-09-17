from fastapi import params
from fastapi.params import Query
import pyodbc as pyodbc
from typing import Optional, Text
from fastapi import FastAPI
from starlette.responses import Response
from data import dokumen as list_dokumen
from pydantic import BaseModel
import json
import pandas as pd
import base64

app = FastAPI()
dokumen = list_dokumen
conn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};User ID=22;Password=;Server=127.0.0.1;Database=document;Port=3306;String Types=Unicode')
cursor = conn.cursor()

class item(BaseModel):
    noreg:Optional[str] = None
    img1:Optional[str] = None
    img2:Optional[str] = None
    img3:Optional[str] = None
    img4:Optional[str] = None
    img5:Optional[str] = None
    img6:Optional[str] = None
    img7:Optional[str] = None
    img8:Optional[str] = None
    jenis_document:Optional[str] = None
    ket:Optional[str] = None

def mssql_result2dict(cursor):
    try: 
        result = []
        columns = [column[0] for column in cursor.description]
        for row in  cursor.fetchall():
            result.append(dict(zip(columns,row)))

        print(result)

        #Check for results
        if len(result) > 0:
            ret = result
        else:
            ret = {"message": "no results found"}
    except pyodbc.Error as e:
        print(e)
        ret = { "message": "Internal Database Query Error"}
    
    return ret

@app.post("/dokumen")
async def create_dokumen(dokumen: item):
    noreg = dokumen.noreg
    img1 = dokumen.img1
    img2 = dokumen.img2
    img3 = dokumen.img3
    img4 = dokumen.img4
    img5 = dokumen.img5
    img6 = dokumen.img6
    img7 = dokumen.img7
    img8 = dokumen.img8
    jenis_document = dokumen.jenis_document
    ket = dokumen.ket

    with open(img1, "rb") as img_file:
        b64_img1 = base64.b64encode(img_file.read())
    with open(img2, "rb") as img_file:
        b64_img2 = base64.b64encode(img_file.read())
    with open(img3, "rb") as img_file:
        b64_img3 = base64.b64encode(img_file.read())
    with open(img4, "rb") as img_file:
        b64_img4 = base64.b64encode(img_file.read())
    with open(img5, "rb") as img_file:
        b64_img5 = base64.b64encode(img_file.read())
    with open(img6, "rb") as img_file:
        b64_img6 = base64.b64encode(img_file.read())
    with open(img7, "rb") as img_file:
        b64_img7 = base64.b64encode(img_file.read())
    with open(img8, "rb") as img_file:
        b64_img8 = base64.b64encode(img_file.read())

    try:
        cursor.execute("INSERT INTO tb_document VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", noreg, b64_img1, b64_img2, b64_img3, b64_img4, b64_img5, b64_img6, b64_img7, b64_img8, jenis_document, ket)
        cursor.commit()
    except Exception as e:
        print(e)
    
    return dokumen

@app.put("/edit_dokumen")
async def edit_dokumen (dokumen: item):
    noreg = dokumen.noreg
    img1 = dokumen.img1
    img2 = dokumen.img2
    img3 = dokumen.img3
    img4 = dokumen.img4
    img5 = dokumen.img5
    img6 = dokumen.img6
    img7 = dokumen.img7
    img8 = dokumen.img8
    jenis_document = dokumen.jenis_document
    ket = dokumen.ket

    with open(img1, "rb") as img_file:
        b64_img1 = base64.b64encode(img_file.read())
    with open(img2, "rb") as img_file:
        b64_img2 = base64.b64encode(img_file.read())
    with open(img3, "rb") as img_file:
        b64_img3 = base64.b64encode(img_file.read())
    with open(img4, "rb") as img_file:
        b64_img4 = base64.b64encode(img_file.read())
    with open(img5, "rb") as img_file:
        b64_img5 = base64.b64encode(img_file.read())
    with open(img6, "rb") as img_file:
        b64_img6 = base64.b64encode(img_file.read())
    with open(img7, "rb") as img_file:
        b64_img7 = base64.b64encode(img_file.read())
    with open(img8, "rb") as img_file:
        b64_img8 = base64.b64encode(img_file.read())

    try:
        cursor.execute ("UPDATE dokumen SET img1=?,img2=?,img3=?,img4=?,img5=?,img6=?,img7=?,img8=?,jenis_document=?,ket=? WHERE noreg=?", b64_img1, b64_img2, b64_img3, b64_img4, b64_img5, b64_img6, b64_img7, b64_img8, jenis_document, ket, noreg)
    except Exception as y:
        print(y)
    return dokumen

@app.delete("/delete", status_code=201)
async def delete_dokumen(noreg : int):
    try:
        cursor.execute("DELETE FROM tb_document WHERE noreg=?",noreg) 
        cursor.commit()
    except Exception as w:
        print(w)
    
    return "Dokumen Anda Telah Dihapus"

@app.get("/read/{noreg}", status_code=201)
async def read_dokumen(noreg, response: Response):
    query = "SELECT * FROM tb_document WHERE noreg=?"
    df = pd.read_sql(query, conn, params=[noreg])
    print(df)
    json_data = df.to_json(orient='records')
    data = {}
    data['status'] = 200
    data['message'] = "Success"
    data['data'] = json.loads(json_data)
    return data

@app.get("/search/{noreg}", status_code=201)
async def search_dokumen(noreg : int,  response: Response):
    try :
        cursor.execute ("SELECT * FROM tb_document WHERE noreg=?", noreg)
        ret = mssql_result2dict(cursor)
        conn.commit()
    except pyodbc.Error as e:
        print('SQL Query Failed : {e}')
        ret = {"message": "system error"}
    return ret

@app.get("/dokumen/{id}", status_code=200)
def get_dokumen_by_id(id: int, response: Response):
    try:
        return dokumen[id - 1]
    except:
        # data ngga ada
        return []

@app.get("/dokumen" ,status_code=201)
async def get_dokumen():
    query = "SELECT * FROM tb_document"
    df = pd.read_sql(query, conn)
    print(df)
    json_data = df.to_json(orient='records')
    data = {}
    data['status'] = 200
    data['message'] = "Success"
    data['data'] = json.loads(json_data)
    return data