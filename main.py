import os
# My Tools
from tools import rotation

# For Marge
import pypdf

M1 = ["洞口"]
M2 = ["針谷","西原"]
DID2 = ["西原"]


if __name__ == '__main__':
    print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//M2//"


    print()
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,os.path.join(pdf,"針谷_中間発表_予稿.pdf")))
    merger.append(os.path.join(pdf,os.path.join(pdf,"針谷_中間発表_スライド_4in1-横.pdf")))
    merger.write(os.path.join(pdf,'針谷-縦.pdf'))
    merger.close()

