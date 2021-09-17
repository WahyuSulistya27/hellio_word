from fastapi import APIRouter
from starlette.responses import Response
from data import dokumen as list_dokumen
from connect import *
from model import *
import base64

router = APIRouter()
dokumen = list_dokumen

@router.put("/edit/{noreg}", status_code=201)
async def edit_dokumen(dokumen : item):
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
        cursor.execute ("UPDATE tb_document SET img1=?,img2=?,img3=?,img4=?,img5=?,img6=?,img7=?,img8=?,jenis_document=?,ket=? WHERE noreg=?", b64_img1, b64_img2, b64_img3, b64_img4, b64_img5, b64_img6, b64_img7, b64_img8, jenis_document, ket, noreg)
        cursor.commit()
    except Exception as e:
        print(e)
    
    return dokumen