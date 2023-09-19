import os
# My Tools
from tools.rotation import Rotation

# For Marge
import pypdf

""" Member list """

D1D2 = ["白石","西原"]
D1D2_ANN = {
    "白石":[49.5, 130, 49.5+82, 130+12],
    "西原":[49.5, 111, 49.5+120, 111+5],
}
D1D2_PAGE = {
    "白石" : 1,
    "西原" : 1,
}

#0.3528mm = 1pt
D1D2P = (1/0.3528)

if __name__ == '__main__':
    #print('slide rotation')
    pdf = "//192.168.11.6//Archive//16_大学院輪講//2023//TED//"

    ## D1D2 Rotation
    D1D2_path = os.path.join(pdf,"D1D2")
    for ind in D1D2:
        ind_path = os.path.join(D1D2_path,ind)
        Rotation(ind_path,ind)

    ## D1D2 Summary Marge
    """横"""
    D1D2_path = os.path.join(pdf,"D1D2")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(D1D2).pdf"))
    for ind in D1D2:
        ind_path = os.path.join(D1D2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中間発表_中田研_D1D2_横.pdf'))
    merger.close()
    """縦"""
    D1D2_path = os.path.join(pdf,"D1D2")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(D1D2).pdf"))
    for ind in D1D2:
        ind_path = os.path.join(D1D2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-縦.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中間発表_中田研_D1D2_縦.pdf'))
    merger.close()

    ## _Get Page 
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    sum_pages = 0
    for idx in range(len(D1D2)):
        ind = D1D2[idx]
        ind_path = os.path.join(D1D2_path,ind)
        pdf_reader_proceeding = PdfFileReader(open(os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind)), 'rb'), strict=True)
        pdf_reader_proceeding_page = pdf_reader_proceeding.numPages
        pdf_reader_slide = PdfFileReader(open(os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind)), 'rb'), strict=True)
        pdf_reader_slide_page = pdf_reader_slide.numPages
        if D1D2[idx] != D1D2[-1]:
            D1D2_PAGE[D1D2[idx+1]] += (pdf_reader_proceeding_page + pdf_reader_slide_page)+sum_pages
            sum_pages += (pdf_reader_proceeding_page + pdf_reader_slide_page)


    ## D1D2 AddLink
    """横"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2023年度中間発表_中田研_D1D2_横.pdf')
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
    for name in D1D2:
        output.addLink(
            pagenum=0, 
            pagedest=D1D2_PAGE[name], 
            rect=RectangleObject([D1D2_ANN[name][0]*D1D2P,D1D2_ANN[name][1]*D1D2P, D1D2_ANN[name][2]*D1D2P,D1D2_ANN[name][3]*D1D2P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2023年度中間発表_中田研_D1D2_横_fin.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()

    """縦"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2023年度中間発表_中田研_D1D2_縦.pdf')
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
    for name in D1D2:
        output.addLink(
            pagenum=0, 
            pagedest=D1D2_PAGE[name], 
            rect=RectangleObject([D1D2_ANN[name][0]*D1D2P,D1D2_ANN[name][1]*D1D2P, D1D2_ANN[name][2]*D1D2P,D1D2_ANN[name][3]*D1D2P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2023年度中間発表_中田研_D1D2_縦_fin.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()