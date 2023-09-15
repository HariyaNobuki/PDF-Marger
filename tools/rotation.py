# For Rotation
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter

import os

def Rotation(manu_path,ind_name):
    pdf_open = open(os.path.join(manu_path,"%s_中間発表_スライド_4in1-横.pdf")%(ind_name),"rb")      # open by binary mode
    pdf_reader = PdfFileReader(pdf_open)
    pdf_writer = PdfFileWriter()

    # Rotation for counterclockwise
    angle = -90

    for page in range(pdf_reader.numPages):
        obj = pdf_reader.getPage(page)
        obj.rotateClockwise(angle) 
        pdf_writer.addPage(obj)

    output = open(os.path.join(manu_path,"%s_中間発表_スライド_4in1-縦.pdf")%(ind_name), 'wb')
    pdf_writer.write(output)
    output.close()