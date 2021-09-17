from pydantic import BaseModel
from typing import Optional

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