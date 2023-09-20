import os
# My Tools
from tools.rotation import Rotation
# For Marge
import pypdf
# For Rotation
from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter
# For Annotation
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm


""" Member list """
M1 = []
M2 = ["針谷","西原"]
DID2 = []
ALL_MEMBER = M1+M2+DID2

if __name__ == '__main__':
    print('PDF Annotation Checker')
    pdf = "C://gitedit//NKT_Merger//TED//_表紙_TED_Only//表紙(ALL).pdf"

    cc = canvas.Canvas("C://gitedit//NKT_Merger//TED//_表紙_TED_Only//表紙(ALL)_annotation.pdf")
    pdf_input = PdfReader(pdf, decompress=False)
    ## 0-page
    page = pdf_input.pages[0]
    pp = pagexobj(page) #ページデータをXobjへの変換
    rl_obj = makerl(cc, pp) # ReportLabオブジェクトへの変換 
    cc.doForm(rl_obj) # 展開

    cc.setFillColor("blue", 0.2)
    cc.setStrokeColorRGB(0.1, 1.0, 0)

    # 平岡
    cc.rect(42 * mm, 73.6 * mm, 121 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 針谷
    cc.rect(42 * mm, 93.5 * mm, 136 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 三浦
    cc.rect(42 * mm, 112.4 * mm, 103 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 川崎
    cc.rect(42 * mm, 131.3 * mm, 132 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 来栖
    cc.rect(42 * mm, 150.2 * mm, 140 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 西原
    cc.rect(42 * mm, 29 * mm, 120 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 白石
    cc.rect(42 * mm, 48 * mm, 82 * mm, 12 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)

    # 洞口
    #cc.rect(42 * mm, 99 * mm, 120 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # 池口
    #cc.rect(42 * mm, 118 * mm, 133 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)
    # ｷﾓﾃｨｰﾅ
    #cc.rect(42 * mm, 137 * mm, 90 * mm, 5 * mm, 1, 1)   # rect(x, y, width, height, stroke=1, fill=0)

    cc.save()



