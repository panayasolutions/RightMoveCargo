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
label_path=rmc_path+"/documents/labels/";

pdfmetrics.registerFont(TTFont('code128', font_path+"code128.TTF"))

def createLabel(booking):
    print(booking)
    printop = 'N'
    pages = list()

    lblpath = label_path+booking.awbNo+'.pdf'
    
    if os.path.isfile(lblpath):
        # os.remove(lblpath)
        return 'Y', lblpath

    doc = SimpleDocTemplate(lblpath, pagesize=(4 * inch, 6 * inch),
                            showBounday=0.5,
                            leftMargin=0.05 * inch,
                            rightMargin=0.05 * inch,
                            topMargin=0.3 * inch,
                            bottomMargin=0.05 * inch)

    if booking.courier == constant.TRACKON:
        courierlogo = 'trackon1.jpg'
    elif booking.courier == constant.PROFESSIONAL:
        courierlogo = 'proff.png'
    elif booking.courier == constant.DTDC:
        courierlogo = 'dtdc.jpeg'
    else:
        courierlogo = 'trackon1.jpg'

    print(lblpath)
    if booking.courier == constant.DELHIVERY:
        printop, story = delhiverylabel(booking,courierlogo)
        pages.extend(story)
    else:
        box_no = 1;
        child_queryset = ChildBooking.objects.filter(masterawbno=booking.awbNo);
        total_box = len(child_queryset);
        total_box = total_box + box_no;
        print(str(total_box)+"  "+str(box_no));
        printop, story = otherLabel(booking,courierlogo,booking,box_no,total_box)
        pages.extend(story)
        for childBooking in child_queryset:
            box_no = box_no+1
            printop, story = otherLabel(booking,courierlogo,childBooking,box_no,total_box)
            pages.extend(story)
    doc.build(pages)
    return printop, lblpath


def delhiverylabel(booking,log):
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


def otherLabel(booking, imagename, childBooking, boxno,total_box):
    client = Client.objects.get(userid=booking.client)
    createDate = booking.entrydate.strftime("%Y-%M-%d %H:%M:%S")
    is_parent =True;
    
    if boxno>1:
        is_parent = False;

    lg = Image(image_path+imagename);
    lg.drawHeight = 1.4 * inch * lg.drawHeight / lg.drawWidth
    lg.drawWidth = 1.4 * inch
    
    iamt = booking.codAmt

    

    ps1 = ParagraphStyle('left', alignment=TA_LEFT, fontName='Helvetica', fontSize=10)
    ps1c = ParagraphStyle('center', alignment=TA_LEFT, fontName='Helvetica', fontSize=10)
    ps1x = ParagraphStyle('left', alignment=TA_LEFT, fontName='Helvetica', fontSize=7)
    p1 = Paragraph('Origin', style=ps1)
    p2 = Paragraph('Destination', style=ps1)
    p3 = Paragraph('IXC', style=ps1)
    p4 = Paragraph(booking.recdestination, style=ps1)
    ps2 = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=48)
    ps3 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    ps3l = ParagraphStyle('left', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    ps4 = ParagraphStyle('right', alignment=TA_RIGHT, fontName='Helvetica', fontSize=10)
    ps5 = ParagraphStyle('bold', alignment=TA_LEFT, fontName='Helvetica-Bold', spaceAfter=16, spaceBefore=16, fontSize=12)
    ps6 = ParagraphStyle('lbold', alignment=TA_CENTER, fontName='Helvetica-Bold', fontSize=26)
    p4x = Paragraph("Reference Number", style=ps3)

    if is_parent==False:
        p5 = Paragraph(code128encoded(childBooking.subAwbNo), style=ps2)
        p6 = Paragraph(str(childBooking.subAwbNo), style=ps3)
    else:
        p5 = Paragraph(code128encoded(booking.awbNo), style=ps2)
        p6 = Paragraph(str(booking.awbNo), style=ps3)
        
    if is_parent==True:
        # if int(total_box) > 1:
        p5x = Paragraph('Piece ' + str(boxno) + ' of ' + str(total_box) + ' Pieces', style=ps3l)
        p7x = Paragraph('Master AWB', style=ps3l)
    else:
        p5x = Paragraph('Piece ' + str(boxno) + ' of ' + str(total_box) + ' Pieces', style=ps3l)
        p7x = Paragraph('Master AWB: '+str(booking.awbNo), style=ps3l)




    p7 = Paragraph('CustRefNo:'+str(booking.refid).upper(), style=ps1x)
    p8 = Paragraph('Mode:'+booking.prodMod, style=ps4)
    p9 = Paragraph('TO:<br/>'+booking.recname+'<br/>'+booking.recaddr1.upper()+'<br/>'+booking.recaddr2.upper()+' '+booking.recdestination.upper()+' '+str(booking.recpin)+'<br/>Ph:'+str(booking.recphone), style=ps5)
    p10 = Paragraph('PCS: '+str(booking.prodPiece), style=ps1)
    p10x = Paragraph('Dt: '+str(createDate), style=ps4)
    pinv = Paragraph('Shipment Value: '+str(iamt), style=ps1)
    p11 = Paragraph('WEIGHT: '+str(booking.prodWeight), style=ps4)
    p12 = Paragraph('Remarks: ', style=ps1)
    p13 = Paragraph('Contains: '+ booking.prodDesc, style=ps1)
    p14 = Paragraph('From/Return Details: '+client.username, style=ps1x)

    if booking.courier == constant.TRACKON:
        p15 = Paragraph('Track your shipment at <b>trackon.in</b>', style=ps1)
    elif booking.courier == constant.PROFESSIONAL:
        p15 = Paragraph('Track your shipment at <b>tpcindia.com</b>', style=ps1)
    elif booking.courier == constant.DTDC:
        p15 = Paragraph('Track your shipment at <b>www.dtdc.in</b>', style=ps1)
    else:
        p15 = Paragraph('          ', style=ps1) #need to fill this when identified

    p16 = Paragraph(str(booking.prodMod).strip().upper(), style=ps6)

   
    t1 = Table([[lg, p1, p2], ['', p3, p4]], style=[('GRID', (0, 0), (2, 1), 0.5, colors.black),
                                                    ('SPAN', (0, 0), (0, 1))])
    t1._argW[0] = 1.5*inch
    t1._argW[1] = 0.6*inch

    if is_parent == False:
        t2 = Table([[p4x], [p5], [p6]], style=[('BOX', (0, 0), (0, 2), 0.5, colors.black),
                                        ('VALIGN', (0, 0), (0, 2), 'TOP')])
        t2._argH[0] = 0.125 * inch
        t2._argH[1] = 0.82 * inch
        t2._argW[0] = 3.735 * inch

    else:
        t2 = Table([[p5], [p6]], style=[('BOX', (0, 0), (2, 2), 0.5, colors.black),
                                   ('VALIGN', (0, 0), (1, 0), 'TOP')])
        t2._argH[0] = 0.82 * inch
        t2._argW[0] = 3.735 * inch


    t2x = Table([[p7, p8]], style=[('BOX', (0, 0), (2, 2), 0.5, colors.black)])

    if is_parent == False:
        t2xx = Table([[p7x, p5x]], style=[('GRID', (0, 0), (2, 0), 0.5, colors.black)])
        t2xx._argW[0] = 1.9 * inch
    else:
        # if int(total_box) > 1:
        if booking.courier == constant.TRACKON:
            t2xx = Table([[p7x, p5x]], style=[('GRID', (0, 0), (1, 0), 0.5, colors.black)])
        else:
            t2xx = Table([[p5x]], style=[('BOX', (0, 0), (0, 0), 0.5, colors.black)])

    t3 = Table([[Spacer(1, 0.005*inch)], [p9], [Spacer(1, 0.005*inch)]], style=[('BOX', (0, 0), (0, 2), 0.5, colors.black)])

    t4 = Table([[p10, p10x], [pinv, ''], [p12, ''], [p13, '']], style=[('BOX', (0, 0), (1, 3), 0.5, colors.black),
                                                         ('SPAN', (0, 1), (1, 1)),
                                                         ('SPAN', (0, 2), (1, 2)),
                                                         ('SPAN', (0, 3), (1, 3))])

    t5 = Table([[p14]], style=[('BOX', (0, 0), (0, 0), 0.5, colors.black)])

    t6 = Table([[p15]], style=[('BOX', (0, 0), (0, 0), 0.5, colors.black)])

    t7 = Table([[p16]], style=[('BOX', (0, 0), (0, 0), 0.5, colors.black),
                               ('VALIGN', (0, 0), (0, 0), 'TOP')])

    t7._argH[0] = 0.6*inch

    if is_parent == False:
        if int(total_box) > 1:
            story = [t1, t2xx, t2,  t2x, t3, t4, t5, t6, t7, PageBreak()]
        else:
            story = [t1, t2, t2x, t3, t4, t5, t6, t7, PageBreak()]
    else:
        story = [t1, t2xx, t2, t2x, t3, t4, t5, t6, t7, PageBreak()]

    return 'Y', story

def code128encoded(data):
    encodestr = constant.STARTCHAR+data
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

    encodestr += chkchar+constant.STOPCHAR

    logging.debug(str(encodestr))

    return str(encodestr)
