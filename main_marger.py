import os
# For Marge
import pypdf
# My Tools
from tools.rotation import Rotation

""" Member list """
M1 = ["木元","池口","洞口"]
M1_ANN = {
    "木元":[42, 257, 42+90, 257+5],
    "池口":[42, 238, 42+133, 238+5],
    "洞口":[42, 219, 42+120, 219+5],
}
M1_PAGE = {
    "木元" : 2,
    "池口" : 2,
    "洞口" : 2,
}


M2 = ["来栖","川崎","三浦","針谷","平岡"]
M2_ANN = {
    "来栖":[42, 150.2, 42+140, 150.2+5],
    "川崎":[42, 131.3, 42+132, 131.3+5],
    "三浦":[42, 112.4, 42+103, 112.4+5],
    "針谷":[42, 93.5, 42+136, 93.5+5],
    "平岡":[42, 73.6, 42+121, 73.6+5],
}
M2_PAGE = {
    "来栖" : 2,
    "川崎" : 2,
    "三浦" : 2,
    "針谷" : 2,
    "平岡" : 2,
}

D1D2 = ["白石","西原"]
D1D2_ANN = {
    "白石":[42, 48, 42+82, 48+12],
    "西原":[42, 29, 42+120, 29+5],
}
D1D2_PAGE = {
    "白石" : 2,
    "西原" : 2,
}

# Annotation [x,y,x+width,y+height]
MEMBER = \
{
    ## M1
    "木元":[42, 257, 42+90, 257+5],
    "池口":[42, 238, 42+133, 238+5],
    "洞口":[42, 219, 42+120, 219+5],
    ## M2
    "来栖":[42, 150.2, 42+140, 150.2+5],
    "川崎":[42, 131.3, 42+132, 131.3+5],
    "三浦":[42, 112.4, 42+103, 112.4+5],
    "針谷":[42, 93.5, 42+136, 93.5+5],
    "平岡":[42, 73.6, 42+121, 73.6+5],
    ## D1D2
    "白石":[42, 48, 42+82, 48+12],
    "西原":[42, 29, 42+120, 29+5],
}


#0.3528mm = 1pt
M2P = (1/0.3528)        # mm to points

if __name__ == '__main__':
    pdf = "C://gitedit//NKT_Merger//TED"    # Path where collected pdf files
    merger = pypdf.PdfMerger()

    """ Rotation """
    ## M1 Rotation
    M1_path = os.path.join(pdf,"M1")
    for ind in M1:
        ind_path = os.path.join(M1_path,ind)
        Rotation(ind_path,ind)

    ## M2 Rotation
    M2_path = os.path.join(pdf,"M2")
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        Rotation(ind_path,ind)

    ## D1D2 Rotation
    D1D2_path = os.path.join(pdf,"D1D2")
    for ind in D1D2:
        ind_path = os.path.join(D1D2_path,ind)
        Rotation(ind_path,ind)


    """横"""
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(ALL).pdf"))
    # M2
    M2_path = os.path.join(pdf,"M2")
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    # D1D2
    D1D2_path = os.path.join(pdf,"D1D2")
    for ind in D1D2:
        ind_path = os.path.join(D1D2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    # M1
    M1_path = os.path.join(pdf,"M1")
    for ind in M1:
        ind_path = os.path.join(M1_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中間発表_中田研_ALL_横.pdf'))
    merger.close()

    """縦"""
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"_表紙_TED_Only","表紙(ALL).pdf"))
    # M2
    M2_path = os.path.join(pdf,"M2")
    for ind in M2:
        ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-縦.pdf"%(ind))))
    # D1D2
    D1D2_path = os.path.join(pdf,"D1D2")
    for ind in D1D2:
        ind_path = os.path.join(D1D2_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-縦.pdf"%(ind))))
    # M1
    M1_path = os.path.join(pdf,"M1")
    for ind in M1:
        ind_path = os.path.join(M1_path,ind)
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_予稿.pdf"%(ind))))
        merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-縦.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中間発表_中田研_ALL_縦.pdf'))
    merger.close()


    ## _Get Page 
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    ## M2
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
        else:
            D1D2_PAGE[D1D2[0]] += (pdf_reader_proceeding_page + pdf_reader_slide_page)+sum_pages
            sum_pages += (pdf_reader_proceeding_page + pdf_reader_slide_page)
    ## D1D2
    #sum_pages = 0
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
        else:
            M1_PAGE[M1[0]] += (pdf_reader_proceeding_page + pdf_reader_slide_page)+sum_pages
            sum_pages += (pdf_reader_proceeding_page + pdf_reader_slide_page)
    ## M1
    #sum_pages = 0
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

    ## M2 AddLink
    """横"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2023年度中間発表_中田研_ALL_横.pdf')
    pdf_reader = PdfFileReader(open(pdf_file_path, 'rb'), strict=True)
    output = PdfFileWriter()
    num = pdf_reader.numPages
    for cp in range(num):
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
    for name in D1D2:
        output.addLink(
            pagenum=0, 
            pagedest=D1D2_PAGE[name], 
            rect=RectangleObject([D1D2_ANN[name][0]*M2P,D1D2_ANN[name][1]*M2P, D1D2_ANN[name][2]*M2P,D1D2_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    for name in M1:
        output.addLink(
            pagenum=1, 
            pagedest=M1_PAGE[name], 
            rect=RectangleObject([M1_ANN[name][0]*M2P,M1_ANN[name][1]*M2P, M1_ANN[name][2]*M2P,M1_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2023年度_中田研_予稿集.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()

    """縦"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    pdf_file_path = os.path.join(pdf,'2023年度中間発表_中田研_ALL_縦.pdf')
    pdf_reader = PdfFileReader(open(pdf_file_path, 'rb'), strict=True)
    output = PdfFileWriter()
    num = pdf_reader.numPages
    for cp in range(num):
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
    for name in D1D2:
        output.addLink(
            pagenum=0, 
            pagedest=D1D2_PAGE[name], 
            rect=RectangleObject([D1D2_ANN[name][0]*M2P,D1D2_ANN[name][1]*M2P, D1D2_ANN[name][2]*M2P,D1D2_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    for name in M1:
        output.addLink(
            pagenum=1, 
            pagedest=M1_PAGE[name], 
            rect=RectangleObject([M1_ANN[name][0]*M2P,M1_ANN[name][1]*M2P, M1_ANN[name][2]*M2P,M1_ANN[name][3]*M2P]),
            border='dott',
            fit='/Fit'
        )
    ## Output
    output_name = os.path.join(pdf,'2023年度中間発表_中田研_ALL_縦_fin.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()