import fastapi
import typing
import json
from pathlib import Path
import uvicorn

from fastapi import FastAPI, File, UploadFile
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

app = FastAPI()
pdf_file =''

@app.get('/')
def home(): 
    return {'Data' : 'Start'}


@app.post('/Total-extract/{item}')
def main(file):
    f=open("xyz.txt","w")
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open(file,"rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle,[l])

    assert d is not None
    f.write(l.get_text_for_page(0))

    f.close()

    with open('xyz.txt') as f:
        contents = f.read()

    import re
    result = re.findall(r"[-+]?\d*\.\d+", contents)

    Total_amount= max(result,key=lambda x:float(x))
    print("Total Amount:",Total_amount)  
    return({"Data" : [file,Total_amount]})
