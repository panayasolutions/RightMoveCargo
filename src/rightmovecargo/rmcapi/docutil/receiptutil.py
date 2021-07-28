from typing import TYPE_CHECKING
from reportlab.pdfgen.canvas import Canvas
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Frame, Image, Table, Paragraph, SimpleDocTemplate, Spacer, PageBreak
from reportlab.platypus.figures import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import landscape
import logging

import base64
from random import randint
import os
from datetime import datetime
from rightmovecargo.rmcapi.constants import constant
from rightmovecargo.rmcapi.models import BookingWeb, Client

rmc_path=Path(__file__).parent.parent;
rmc_path = str(rmc_path);
image_path=rmc_path+"/static/images/";
font_path = rmc_path+"/static/fonts/3of9/fonts/"
receipts_path=rmc_path+"/documents/receipts/";

pdfmetrics.registerFont(TTFont('code128', font_path+"code128.TTF"))

def createReceipt(booking):
    printop = 'N'
    pages = list()
    lblpath = receipts_path+booking.awbNo+'.pdf'
    
    if os.path.isfile(lblpath):
        return 'Y', lblpath
    
    doc = SimpleDocTemplate(lblpath, pagesize=(4 * inch, 6 * inch),
                            showBounday=0.5,
                            leftMargin=0.05 * inch,
                            rightMargin=0.05 * inch,
                            topMargin=0.05 * inch,
                            bottomMargin=0.05 * inch)
    print(lblpath)
    if booking.courier == constant.TRACKON:
        courierlogo = 'trackon1.jpg'
    elif booking.courier == constant.PROFESSIONAL:
        courierlogo = 'proff.png'
    elif booking.courier == constant.DTDC:
        courierlogo = 'dtdc.jpeg'
    else:
        courierlogo = 'trackon1.jpg'
        printop, story = create(booking,courierlogo)
        pages.extend(story)
        print(lblpath)
    printop, story = create(booking,courierlogo)
    
    pages.extend(story)
    doc.build(pages)
    return printop, lblpath


def create(booking,log):
    # 4inch width 6 inch height
    title = "Receipt of AWB booking";
    # consignee = booking['consignee']
    client = Client.objects.get(userid=booking.client)
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    story = []

    ri = Image(image_path+log)
    ri.drawHeight = 1.7*inch * ri.drawHeight / ri.drawWidth
    ri.drawWidth = 1.7*inch

    rd = Image(image_path+log)
    rd.drawHeight = 1.7 * inch * rd.drawHeight / rd.drawWidth
    rd.drawWidth = 1.7 * inch

    samt = 'samt' #booking.codAmt #'{:10,.2}'.format(booking.codAmt) #format(booking['price'])

    if str(booking.toFreight).upper() == 'COD':
        ptstr = '<b>' + booking.toFreight + '<br/> '+str(booking.codAmt)+'<br/>' + booking.prodMod + '</b>'
    else:
        ptstr = '<b>' + booking.toFreight + '<br/>' + booking.prodMod + '</b>'
        
    sortcode = ' '
    # createDate = datetime.strptime(booking.entrydate[:19],"%Y-%m-%dT%H:%M:%S").strftime("%Y-%M-%d %H:%M:%S")
    pscenter6 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=6)
    psleft6 = ParagraphStyle('left', alignment=TA_LEFT,fontSize=6)
    psright6 = ParagraphStyle('right', alignment=TA_RIGHT,fontSize=6)

    pscenter7 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=7)
    psleft7 = ParagraphStyle('left', alignment=TA_LEFT,fontSize=7)
    psright7 = ParagraphStyle('right', alignment=TA_RIGHT,fontSize=7)
    
    pscenter8 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    psleft8 = ParagraphStyle('left', alignment=TA_LEFT,fontSize=8)
    psright8 = ParagraphStyle('right', alignment=TA_RIGHT,fontSize=8)
   
    ptitle = Paragraph(str(title), style=pscenter8);
    pconsigneedetail = Paragraph('Shipping Address:<br/><b>'+client.username+'<br/>'+client.address1+'<br/><br/>PIN: '+str(client.pin)+'</b>', style=psleft6)
    pdestination = Paragraph('Destination Address:<br/><b>'+booking.recname+'<br/>'+booking.recaddr1+'<br/>'+booking.recdestination+'<br/>PIN: '+str(booking.recpin)+'</b>', style=psright6)
    
    pawbno = Paragraph('<b>AWB No: ' + booking.awbNo+'</b>', style=pscenter8)
    pcarrier = Paragraph('Carrier: ' + booking.courier , style=pscenter6)
    pbookingdate = Paragraph('Booking Date: 13-07-2021' , style=pscenter6)
    pmode = Paragraph("Mode: "+booking.prodMod, style=pscenter6)
    # pdestination = Paragraph("Destination: ", style=psleft6)
    pnopieces = Paragraph("No. of Pieces: "+str(booking.prodPiece), style=pscenter6) # repeated twice
    pinvoicenumber = Paragraph("Invoice No: "+booking.invoiceNumber, style=psleft6)
    pinvoicevalue = Paragraph("Invoice Value: "+str(booking.invoiceValue), style=psright6) #repeated four times
    # psender = Paragraph('www.rightmovecargo.com', style=pscen7)
    
    t = Table([[pawbno]], style=[('GRID', (0, 0), (1, 0), 0.5, colors.black)])

    t1 = Table([[ri, rd]], style=[('GRID', (0, 0), (1, 0), 0.5, colors.black),
                           ('VALIGN', (0, 0), (1, 0), 'MIDDLE')])
    t1._argH[0] = 0.6*inch

    t2 = Table([[pbookingdate, pcarrier]], style=[('GRID', (0, 0), (1, 0), 0.5, colors.black),
                            ('VALIGN', (0, 0), (1, 0), 'MIDDLE')])
    t2._argW[0] = 1.87*inch

    data1 = [[pnopieces, pmode],[pconsigneedetail, pdestination],[pinvoicenumber,pinvoicevalue]]

    t5 = Table(data1, style=[('GRID', (0, 0), (3, 4), 0.5, colors.black),
                             ('VALIGN', (0, 1), (3, 4), 'MIDDLE')]);
    # t6 = Table([[psender]], style=[('GRID', (0, 0), (0, 0), 0.5, colors.black)])
    # t6
    story = [t,t1, t2, t5, PageBreak()]
    return 'Y', story