import os
# My Tools
from tools.rotation import Rotation

# For Marge
import pypdf

""" Member list """
M1 = []
M2 = ["川崎","針谷"]
DID2 = []
ALL_MEMBER = M1+M2+DID2

if __name__ == '__main__':
    print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//"

    # M2 Rotation
    M2_path = os.path.join(pdf,"M2")
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        Rotation(ind_path,ind)

    # M2 Summary Marge
    M2_path = os.path.join(pdf,"M2")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(M2).pdf"))
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横.pdf'))
    merger.close()

    # M2 AddLink
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横.pdf')
    pdf_reader = PdfFileReader(open(pdf_file_path, 'rb'), strict=True)
    
