
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
from datetime import datetime
from rightmovecargo.rmcapi.models import BookingWeb



pathf = Path(__file__).parent / '../static/fonts/3of9/fonts/code128.TTF'

pdfmetrics.registerFont(TTFont('code128', pathf))

def createLabel(awbNo):

# from rightmovecargo.rmcapi.labelutil import labelTest
# labelTest.createLabel('500188521464')
    printop = 'N'
    pages = list()

    labelfilename = '../static/LabelDocs/' + awbNo + '.pdf'
    logging.debug("label filename" + labelfilename)
    parentpath = Path(__file__).parent
    lblpath = str(parentpath) + "\\..\\static\\LabelDocs\\" + awbNo + '.pdf'

    if os.path.isfile(labelfilename):
        return 'Y', labelfilename

    doc = SimpleDocTemplate(lblpath, pagesize=(4 * inch, 6 * inch),showBounday=0.5,leftMargin=0.05 * inch,rightMargin=0.05 * inch,topMargin=0.05 * inch,bottomMargin=0.05 * inch)

    courierlogo = 'dtdc.jpeg'
    
    lbldata = [] #BookingWeb.objects.get(awbNo=awbNo);
    printop, story = delhiverylabel(lbldata)
    pages.extend(story)
    doc.build(pages)
    return printop, labelfilename


def delhiverylabel(labeldata):
     #rand = randint(10000, 99999)
    styles = getSampleStyleSheet()

    styleN = styles['Normal']

    story = []

    ri = Image(Path(__file__).parent / '../static/images/logo.png')

    ri.drawHeight = 1.7*inch * ri.drawHeight / ri.drawWidth
    ri.drawWidth = 1.7*inch

    rd = Image(Path(__file__).parent / '../static/images/delhivery.jpg')

    rd.drawHeight = 1.7 * inch * rd.drawHeight / rd.drawWidth
    rd.drawWidth = 1.7 * inch

    samt = 200
    camt = 300
    ptstr = '<b>TO PAY<br/> '+str(camt)+'<br/>100</b>'
    sortcode = 'To Pay'
    ps1 = ParagraphStyle('left', alignment=TA_LEFT)
    ps2 = ParagraphStyle('right', alignment=TA_RIGHT)
    ps3 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=6)
    ps4 = ParagraphStyle('normal', alignment=TA_LEFT, fontName='Helvetica', fontSize=7)
    ps5 = ParagraphStyle('normal', alignment=TA_LEFT, fontName='Helvetica', fontSize=8)
    ps5c = ParagraphStyle('normal', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    psb = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=42)
    psbo = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=28)
    p2 = Paragraph(str('10091'), style=ps1)
    p3 = Paragraph('<b>'+sortcode+'</b>', style=ps2)
    p4 = Paragraph('Shipping Address:<br/><b>AMIT KUMAR <br/>13/67 TRILOK PURN<br/>DESTINATION<br/>PIN: '+str('110091')+'</b>', style=ps1)
    p9 = Paragraph('Seller: SELLET', style=ps4)
    p11 = Paragraph("Product PRODUCT ", style=ps3)
    p12 = Paragraph("Price", style=ps3)
    p13 = Paragraph("Total", style=ps3) # repeated twice
    p14 = Paragraph('Prod', style=ps1)
    p15 = Paragraph("adsfa", style=ps3) #repeated four times
    p17 = Paragraph('\n'+'OID', style=styleN)
    p18 = Paragraph('Return Address:ADDRESS--PINT', style=ps4)
    p19 = Paragraph("asdf", style=ps3)
    p21 = Paragraph('Dt:'+str('TEST'), style=ps4)
    p22 = Paragraph(code128encoded(str('TEST2')), style=psb)
    p23 = Paragraph('<br/><br/><br/>'+str(), style=ps5c)
    p24 = Paragraph(code128encoded(str('TEST3')), style=psbo)
    p25 = Paragraph('<br/><br/>'+str('OID'), style=ps5c)

    data = [[ri, rd]]
    t = Table(data, style=[('GRID', (0, 0), (1, 0), 0.5, colors.black),
                           ('VALIGN', (0, 0), (1, 0), 'MIDDLE')])
    t._argH[0] = 0.6*inch

    t1 = Table([[[p22, p23], ''], [p2, p3]], style=[('BOX', (0, 0), (1, 1), 0.5, colors.black),
                                                    ('SPAN', (0, 0), (1, 0)),
                                                    ('ALIGN', (0, 0), (0, 0), 'CENTER'),
                                                    ('VALIGN', (0, 0), (0, 0), 'TOP')])
    t1._argH[0] = 0.8*inch
    t1._argH[1] = 0.2*inch
    t1._argW[0] = 1.735*inch
    t1._argW[1] = 2*inch

    t2 = Table([[p4, p19]], style=[('GRID', (0, 0), (1, 0), 0.5, colors.black),
                                   ('VALIGN', (1, 0), (1, -1), 'MIDDLE')])

    t2._argW[0] = 3*inch

    t3 = Table([[p9, p21]], style=[('GRID', (0, 0), (1, 0), 0.5, colors.black)])

    t3._argW[0] = 2.485*inch

    data1 = [[p11, p12, p13],
             [p14, p15, p15],
             [p13, p15, p15]]

    t4 = Table(data1, style=[('GRID', (0, 0), (2, 2), 0.5, colors.black),
                             ('VALIGN', (0, 1), (2, 1), 'MIDDLE')])

    t4._argH[1] = 0.35*inch
    t4._argW[0] = 2*inch

    #if rob.drawHeight > 0.75*inch:
    #    rob.drawHeight = 0.65*inch

    t5 = Table([[[p24, p25]]], style=[('GRID', (0, 0), (0, 0), 0.5, colors.black),
                                      ('ALIGN', (0, 0), (0, 0), 'CENTER'),
                                      ('VALIGN', (0, 0), (0, 0), 'TOP')])

    t5._argW[0] = 3.735*inch
    t5._argH[0] = 0.75*inch

    t6 = Table([[p18]], style=[('GRID', (0, 0), (0, 0), 0.5, colors.black)])

    story = [t, t1, t2, t3, t4, t5, t6, PageBreak()]

    return 'Y', story


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
