import os
# My Tools
from tools.rotation import Rotation

# For Marge
import pypdf

# For Rotation
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter


""" Member list """

M2 = ["来栖魁人","針谷亘輝",
      #"平岡巧光","三浦岳也",
      #"洞口裕真","川﨑弘貴",
      #"須藤駿","小山天輔",
      #"坪井陽人","藤澤大世",
      #"渡慶次一哲"
      ]



if __name__ == '__main__':
    #print('slide rotation')
    pdf = "//192.168.11.6//Archive//20240209_作業用//"

    ## M2 Rotation
    rt_path = os.path.join(pdf,"2in1予稿")

    #ind_path = os.path.join(rt_path)
    #Rotation_hir(ind_path)
    #Rotation_tit(r"\\192.168.11.6\Archive\20240209_作業用\表紙\2023")

    ## M2 Summary Marge
    """横"""
    M2_path = os.path.join(pdf,"2in1予稿")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"表紙","2023","表紙2023.pdf"))
    for ind in M2:
        print(ind)
        #ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(M2_path,"2023_予稿_%s.pdf"%(ind)))
        #merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度大学院輪講_中田研_M2_横.pdf'))
    merger.close()


    ## M2 AddLink
    """横"""
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import RectangleObject
    #pdf_file_path = os.path.join(pdf,'2023年度大学院輪講_中田研_M2_横.pdf')
    #pdf_reader = PdfFileReader(open(pdf_file_path, 'rb'), strict=True)

    ## Output
    output = PdfFileWriter()
    output_name = os.path.join(pdf,'2023年度大学院輪講_中田研_M2_横_1733.pdf')
    output_stream = open(output_name, 'wb')
    output.write(output_stream)
    output_stream.close()
