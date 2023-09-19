import os
# My Tools
from tools.rotation import Rotation

# For Marge
import pypdf

""" Member list """

M1 = ["木元","池口","洞口"]
M1_ANN = {
    "木元":[42, 137, 42+90, 137+5],
    "池口":[42, 118, 42+133, 118+5],
    "洞口":[42, 99, 42+120, 99+5],
}
M1_PAGE = {
    "木元" : 1,
    "池口" : 1,
    "洞口" : 1,
}

#0.3528mm = 1pt
M1P = (1/0.3528)

if __name__ == '__main__':
    #print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//"

    ## M1 Rotation
    M1_path = os.path.join(pdf,"M1")
    for ind in M1:
        ind_path = os.path.join(M1_path,ind)
        Rotation(ind_path,ind)

    ## M1 Summary Marge
    """横"""
    M1_path = os.path.join(pdf,"M1")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(M1).pdf"))
    for ind in M1:
        ind_path = os.path.join(M1_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中間発表_中田研_M1_横.pdf'))
    merger.close()
    """縦"""
    M1_path = os.path.join(pdf,"M1")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(M1).pdf"))
    for ind in M1:
        ind_path = os.path.join(M1_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-縦.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中間発表_中田研_M1_縦.pdf'))
    merger.close()

    ## _Get Page 
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    sum_pages = 0
    for idx in range(len(M1)):
        ind = M1[idx]
        ind_path = os.path.join(M1_path,ind)
        pdf_reader_proceeding = PdfFileReader(open(os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind)), 'rb'), strict=True)
        pdf_reader_proceeding_page = pdf_reader_proceeding.numPages
        pdf_reader_slide = PdfFileReader(open(os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind)), 'rb'), strict=True)
        pdf_reader_slide_page = pdf_reader_slide.numPages
        if M1[idx] != M1[-1]:
            M1_PAGE[M1[idx+1]] += (pdf_reader_proceeding_page + pdf_reader_slide_page)+sum_pages
            sum_pages += (pdf_reader_proceeding_page + pdf_reader_slide_page)


    ## M1 AddLink
    """横"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2023年度中間発表_中田研_M1_横.pdf')
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
    for name in M1:
        output.addLink(
            pagenum=0, 
            pagedest=M1_PAGE[name], 
            rect=RectangleObject([M1_ANN[name][0]*M1P,M1_ANN[name][1]*M1P, M1_ANN[name][2]*M1P,M1_ANN[name][3]*M1P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2023年度中間発表_中田研_M1_横_fin.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()

    """縦"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2023年度中間発表_中田研_M1_縦.pdf')
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
    for name in M1:
        output.addLink(
            pagenum=0, 
            pagedest=M1_PAGE[name], 
            rect=RectangleObject([M1_ANN[name][0]*M1P,M1_ANN[name][1]*M1P, M1_ANN[name][2]*M1P,M1_ANN[name][3]*M1P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2023年度中間発表_中田研_M1_縦_fin.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()