import os
# My Tools
from tools.rotation import Rotation

# For Marge
import pypdf

""" Member list """

M2 = ["来栖","川崎","三浦","針谷","平岡"]
M2_ANN = {
    "来栖":[42,138.5,42+132,138.5+5],
    "川崎":[42,138.5,42+132,138.5+5],
    "三浦":[42,138.5,42+132,138.5+5],
    "針谷":[42,100.5,42+136,100.5+5],
    "平岡":[42,138.5,42+132,138.5+5],
}

#0.3528mm = 1pt
M2P = (1/0.3528)

if __name__ == '__main__':
    #print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//"
#
    ## M2 Rotation
    #M2_path = os.path.join(pdf,"M2")
    #for ind in M2:
    #    ind_path = os.path.join(M2_path,ind)
    #    Rotation(ind_path,ind)
#
    ## M2 Summary Marge
    #M2_path = os.path.join(pdf,"M2")
    #merger = pypdf.PdfMerger()
    #merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(M2).pdf"))
    #for ind in M2:
    #    ind_path = os.path.join(M2_path,ind)
    #    merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
    #    merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    #merger.write(os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横.pdf'))
    #merger.close()

    # M2 AddLink
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横.pdf')
    pdf_reader = PdfFileReader(open(pdf_file_path, 'rb'), strict=True)
    output = PdfFileWriter()
    num = pdf_reader.numPages
    for cp in range(num):
        # p_size = page.mediaBox
        # Decimal('595.32000000000005') Width
        # Decimal('841.91999999999996') Height
        page = pdf_reader.getPage(cp)
        output.addPage(page)
    # AddLink
    for name in M2:
        output.addLink(
            pagenum=0, 
            pagedest=3, 
            rect=RectangleObject([M2_ANN[name][0]*M2P,M2_ANN[name][1]*M2P, M2_ANN[name][2]*M2P,M2_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    # Output
    output_name = os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横_1733.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()
