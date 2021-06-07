
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Frame, Image, Table, Paragraph, SimpleDocTemplate, Spacer, PageBreak
from reportlab.platypus.figures import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.lib.units import inch
import logging



import base64
from random import randint
import os
import time
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
from reportlab.platypus.tables import TableStyle




def code128encoded(data):

    encodestr = 'Ë'+data
    ldata = len(data) + 1
    logging.debug(str(data))
    logging.debug(str(ldata))
    sumval = 103
    for i in range(1, ldata):
        sumval += (ord(data[i-1])-32)*i

    logging.debug(str(sumval))

    modval = sumval % 103

    logging.debug(str(modval))

    if modval >= 95:
        chkchar = chr(modval+100)
    else:
        chkchar = chr(modval+32)

    encodestr += chkchar+'Î'

    logging.debug(str(encodestr))

    return str(encodestr)

path_rmcapi = str(Path(__file__).parent.parent) # upto rmcapi

awbNo = '1234567'

dir_name = str(path_rmcapi)+"/static/labels/"
file_ext = ".pdf"
full_file_path = os.path.realpath(dir_name+awbNo+file_ext)
pathf = path_rmcapi+'/static/fonts/3of9/fonts/code128.TTF'
pdfmetrics.registerFont(TTFont('code128', pathf))

if os.path.isfile(full_file_path):
    os.remove(full_file_path)
    # return 'Y', full_file_path

doc = SimpleDocTemplate(full_file_path, pagesize=(4 * inch, 6 * inch),showBounday=0.5,leftMargin=0.05 * inch,rightMargin=0.05 * inch,topMargin=0.05 * inch,bottomMargin=0.05 * inch)

styles = getSampleStyleSheet()
styleN = styles['Normal']
story = []
pages = list()

courierlogo = 'delhivery.jpg'

ri = Image(path_rmcapi+ '/static/images/logo.png')
ri.drawHeight = 1.2*inch * ri.drawHeight / ri.drawWidth
ri.drawWidth = 1.2*inch

rd = Image(path_rmcapi+'/static/images/'+courierlogo)
rd.drawHeight = 1.7 * inch * rd.drawHeight / rd.drawWidth
rd.drawWidth = 1.7 * inch

awbBarCode = code128encoded('12345678');


r3s = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=28)
p22 = Paragraph(code128encoded(str('12345678')), style=r3s)
p23 = Paragraph('<br/><br/><br/>'+str(awbNo), style=r3s)

row1 = [ri,'','Origin','', 'Destination',''];
row2 = ['', '','IXC', '', 'KAKINADA', '']
row3 = ['Master AWB','','Piece 1 of 2 Pieces', '', '', '']
row4 = [p22,'', '', '', '', '']
row5 = ['','', '', '', '', '']
row6 = ['','', '', '', '', '']
row7 = ['00','', '01', '02', '03', '04']
row8 = ['00','', '01', '02', '03', '04']
row9 = ['00','', '01', '02', '03', '04']
data= [
 row1, #rows
 row2,
 row3,
 row4,
 row5,
 row6,
 row7,
 row8,
 row9,
 row9,
 row9,
 row9,
]


t=Table(data,style=[
('GRID',(0,0),(-1,-1),1,colors.black),
('SPAN',(0,0),(1,1)), # track on image
('SPAN',(2,0),(3,0)), # orgin 
('SPAN',(4,0),(5,0)), # destination
('SPAN',(2,1),(3,1)), # orgin value
('SPAN',(4,1),(5,1)), # destination value

('SPAN',(0,2),(1,2)), # awbno
('SPAN',(2,2),(5,2)), # Pieces number


('SPAN',(0,3),(5,9)), # barcode
#  ('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
#  ('SPAN',(-2,-2),(-1,-1)),
 ])

story = [t, PageBreak()]

pages.extend(story)
doc.build(pages)

print('abc')


