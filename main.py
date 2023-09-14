
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter

if __name__ == '__main__':
    print('slide.pdf to ')
    path = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//M2//針谷//針谷_中間発表_スライド.pdf"

    pdf_open = open(path,"rb")      # open by binary mode
    
