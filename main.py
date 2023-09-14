import os 
# For Rotation
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter
# For Marge
import pypdf

if __name__ == '__main__':
    print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//M2//針谷//"

    pdf_open = open(os.path.join(pdf,"針谷_中間発表_スライド_4in1-横.pdf"),"rb")      # open by binary mode
    pdf_reader = PdfFileReader(pdf_open)
    pdf_writer = PdfFileWriter()

    # 回転角度（時計回り）
    angle = -90

    # 全ページ回転
    for page in range(pdf_reader.numPages):
        obj = pdf_reader.getPage(page)
        obj.rotateClockwise(angle) 
        pdf_writer.addPage(obj)

    output = open(os.path.join(pdf,"針谷_中間発表_スライド_4in1-縦.pdf"), 'wb')
    pdf_writer.write(output)
    output.close()

    print()
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,os.path.join(pdf,"針谷_中間発表_予稿.pdf")))
    merger.append(os.path.join(pdf,os.path.join(pdf,"針谷_中間発表_スライド_4in1-横.pdf")))
    merger.write(os.path.join(pdf,'針谷-縦.pdf'))
    merger.close()

