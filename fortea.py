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
      "平岡巧光","三浦岳也",
      "洞口裕真","川﨑弘貴",
      "須藤駿","小山天輔",
      "坪井陽人","藤澤大世",
      "渡慶次一哲"
      ]

if __name__ == '__main__':
    #print('slide rotation')
    pdf = "//192.168.11.6//Archive//20240209_作業用//"

    ## M2 Rotation
    rt_path = os.path.join(pdf,"付録削除済スライド")

    #ind_path = os.path.join(rt_path)
    #Rotation_hir(ind_path)
    #Rotation_tit(r"\\192.168.11.6\Archive\20240209_作業用\表紙\2023")

    ## M2 Summary Marge
    """横"""
    M2_path = os.path.join(pdf,"付録削除済スライド")
    merger = pypdf.PdfMerger()
    merger.append(os.path.join(pdf,"表紙","2023","表紙2023_スライド_2in1.pdf"))
    for ind in M2:
        print(ind)
        #ind_path = os.path.join(M2_path,ind)
        merger.append(os.path.join(M2_path,"2023_発表資料_%s.pdf"%(ind)))
        #merger.append(os.path.join(ind_path,os.path.join(ind_path,"%s_中間発表_スライド_4in1-横.pdf"%(ind))))
    merger.write(os.path.join(pdf,'2023年度中田研_スライド集先生用.pdf'))
    merger.close()


