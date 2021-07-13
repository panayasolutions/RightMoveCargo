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
import logging

import base64
from random import randint
import os
from datetime import datetime
from rightmovecargo.rmcapi.constants import constant
from rightmovecargo.rmcapi.models import BookingWeb, Client,Consignee, ChildBooking, User, UserCompany, UserConsignee, UserType


rmc_path=Path(__file__).parent.parent;
rmc_path = str(rmc_path);
image_path=rmc_path+"/static/images/";
font_path = rmc_path+"/static/fonts/3of9/fonts/"
dockect_path=rmc_path+"/documents/dockets/";

pdfmetrics.registerFont(TTFont('code128', font_path+"code128.TTF"))

def createDocket(booking):
    print(booking)
    printop = 'N'
    pages = list()

    lblpath = dockect_path+booking.awbNo+'.pdf'
    
    if os.path.isfile(lblpath):
        # os.remove(lblpath)
        return 'Y', lblpath

    doc = SimpleDocTemplate(lblpath, pagesize=(4 * inch, 6 * inch),
                            showBounday=0.5,
                            leftMargin=0.05 * inch,
                            rightMargin=0.05 * inch,
                            topMargin=0.05 * inch,
                            bottomMargin=0.05 * inch)

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
    return printop, lblpath


def create(booking,log):
    # consignee = booking['consignee']
    client = Client.objects.get(userid=booking.client)
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    story = []

    ri = Image(image_path+'logo.png')
    ri.drawHeight = 1.7*inch * ri.drawHeight / ri.drawWidth
    ri.drawWidth = 1.7*inch

    rd = Image(image_path+'delhivery.jpg')
    rd.drawHeight = 1.7 * inch * rd.drawHeight / rd.drawWidth
    rd.drawWidth = 1.7 * inch

    samt = booking.codAmt #'{:10,.2}'.format(booking.codAmt) #format(booking['price'])

    if str(booking.toFreight).upper() == 'COD':
        ptstr = '<b>' + booking.toFreight + '<br/> '+str(booking.codAmt)+'<br/>' + booking.prodMod + '</b>'
    else:
        ptstr = '<b>' + booking.toFreight + '<br/>' + booking.prodMod + '</b>'

    # if booking['sort_code'] is not None:
    #     sortcode = booking['sort_code']
    # else:
    sortcode = ' '

    createDate = datetime.strptime(booking.entrydate[:19],"%Y-%m-%dT%H:%M:%S").strftime("%Y-%M-%d %H:%M:%S")
    ps1 = ParagraphStyle('left', alignment=TA_LEFT)
    ps2 = ParagraphStyle('right', alignment=TA_RIGHT)
    ps3 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=6)
    ps4 = ParagraphStyle('normal', alignment=TA_LEFT, fontName='Helvetica', fontSize=7)
    ps5 = ParagraphStyle('normal', alignment=TA_LEFT, fontName='Helvetica', fontSize=8)
    ps5c = ParagraphStyle('normal', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    psb = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=42)
    psbo = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=28)
    p2 = Paragraph(str(booking['pin']), style=ps1)
    p3 = Paragraph('<b>'+sortcode+'</b>', style=ps2)
    
    p4 = Paragraph('Shipping Address:<br/><b>'+booking.recname+'<br/>'+booking.recaddr1+'<br/>'+booking.recdestination+'<br/>PIN: '+str(booking.recpin)+'</b>', style=ps1)
    p9 = Paragraph('Seller: ' + client.username, style=ps4)
    p11 = Paragraph("Product", style=ps3)
    p12 = Paragraph("Price", style=ps3)
    p13 = Paragraph("Total", style=ps3) # repeated twice
    p14 = Paragraph(booking.prodDesc, style=ps1)
    p15 = Paragraph(samt, style=ps3) #repeated four times
    p17 = Paragraph('\n'+booking.invoiceNumber, style=styleN)
    p18 = Paragraph('Return Address:'+client.username+'-'+client.address1+'-'+str(client.pin), style=ps4)
    p19 = Paragraph(ptstr, style=ps3)
    p21 = Paragraph('Dt:'+str(createDate), style=ps4)
    p22 = Paragraph(code128encoded(str(booking.awbNo)), style=psb)
    p23 = Paragraph('<br/><br/><br/>'+str(booking.awbNo), style=ps5c)
    p24 = Paragraph(code128encoded(str(booking.invoiceNumber)), style=psbo)
    p25 = Paragraph('<br/><br/>'+str(booking.invoiceNumber), style=ps5c)

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