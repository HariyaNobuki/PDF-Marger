import os
# My Tools
from tools.rotation import Rotation

# For Marge
import pypdf

""" Member list """

M2 = ["来栖","川崎","三浦","針谷","平岡"]
M2_ANN = {
    "来栖":[42, 157.4, 140+132, 157.4+5],
    "川崎":[42, 138.5, 42+132, 138.5+5],
    "三浦":[42, 119.5, 103+132, 119.5+5],
    "針谷":[42, 100.5, 42+136, 100.5+5],
    "平岡":[42, 81.5, 121+132, 81.5+5],
}
M2_PAGE = {
    "来栖" : 1,
    "川崎" : 1,
    "三浦" : 1,
    "針谷" : 1,
    "平岡" : 1,
}

#0.3528mm = 1pt
M2P = (1/0.3528)

if __name__ == '__main__':
    #print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//"

    ## M2 Rotation
    M2_path = os.path.join(pdf,"M2")
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        Rotation(ind_path,ind)

    ## M2 Summary Marge
    """横"""
    M2_path = os.path.join(pdf,"M2")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(M2).pdf"))
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横.pdf'))
    merger.close()
    """縦"""
    M2_path = os.path.join(pdf,"M2")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(M2).pdf"))
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-縦.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2022年度大学院輪講_中田研_M2_縦.pdf'))
    merger.close()

    ## _Get Page 
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    sum_pages = 0
    for idx in range(len(M2)):
        ind = M2[idx]
        ind_path = os.path.join(M2_path,ind)
        pdf_reader_proceeding = PdfFileReader(open(os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind)), 'rb'), strict=True)
        pdf_reader_proceeding_page = pdf_reader_proceeding.numPages
        pdf_reader_slide = PdfFileReader(open(os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind)), 'rb'), strict=True)
        pdf_reader_slide_page = pdf_reader_slide.numPages
        if M2[idx] != M2[-1]:
            M2_PAGE[M2[idx+1]] += (pdf_reader_proceeding_page + pdf_reader_slide_page)+sum_pages
            sum_pages += (pdf_reader_proceeding_page + pdf_reader_slide_page)


    ## M2 AddLink
    """横"""
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
    ## AddLink
    for name in M2:
        output.addLink(
            pagenum=0, 
            pagedest=M2_PAGE[name], 
            rect=RectangleObject([M2_ANN[name][0]*M2P,M2_ANN[name][1]*M2P, M2_ANN[name][2]*M2P,M2_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2022年度大学院輪講_中田研_M2_横_1733.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()

    """縦"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2022年度大学院輪講_中田研_M2_縦.pdf')
    pdf_reader = PdfFileReader(open(pdf_file_path, 'rb'), strict=True)
    output = PdfFileWriter()
    num = pdf_reader.numPages
    for cp in range(num):
        # p_size = page.mediaBox
        # Decimal('595.32000000000005') Width
        # Decimal('841.91999999999996') Height
        page = pdf_reader.getPage(cp)
        output.addPage(page)
    ## AddLink
    for name in M2:
        output.addLink(
            pagenum=0, 
            pagedest=M2_PAGE[name], 
            rect=RectangleObject([M2_ANN[name][0]*M2P,M2_ANN[name][1]*M2P, M2_ANN[name][2]*M2P,M2_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2022年度大学院輪講_中田研_M2_縦_1733.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()