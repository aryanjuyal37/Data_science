import streamlit as st
import streamlit.components.v1 as stc

st.title('Total Extract')
st.markdown("""
To get total amount from an invoice!

""")

import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


st.header("Document")
pdf_file = st.text_input("Enter path of the file")
kk=st.button("Start")
print(pdf_file)
@st.cache		


def main(pdf_file):
    f=open("xyz.txt","w")
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open(pdf_file, "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])
        

    assert d is not None
    f.write(l.get_text_for_page(0))
    f.close()

    with open('xyz.txt') as f:
        contents = f.read()

    import re
    result = re.findall(r"[-+]?\d*\.\d+", contents)
    print(contents)
    print(result)  
    Total_amount= max(result,key=lambda x:float(x))
    return Total_amount 
    

if kk==True:
    print(pdf_file)
    Total_amount=main(pdf_file)
    st.write(Total_amount)