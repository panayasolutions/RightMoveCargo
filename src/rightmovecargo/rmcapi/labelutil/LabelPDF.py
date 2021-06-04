
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Frame, Image, Table, Paragraph, SimpleDocTemplate, Spacer, PageBreak
from reportlab.platypus.figures import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.lib.units import inch
import logging
from configuration import config
from constants import constants
from API import DLabelAPI
import base64
from random import randint
import os
from datetime import datetime
from Extract import extractData
from rightmovecargo.rmcapi.models import BookingWeb

configitems = config.configuration()
DBConnString = configitems["databaseconnstr"]
logfilename = configitems["logfilename"]
loglevel = configitems["loglevel"]

logging.basicConfig(filename=logfilename, level=loglevel)

pathf = Path(__file__).parent / '../static/fonts/3of9/fonts/code128.TTF'

pdfmetrics.registerFont(TTFont('code128', pathf))

def createmultilabel(awblist):
    printop = 'N'

    timen = datetime.now().strftime('%H%M%S')
    randstr = str(randint(100000, 999999))

    labelfilename = '../static/LabelDocs/multilabel' + str(timen) + randstr + '.pdf'
    logging.debug("label filename" + labelfilename)
    parentpath = Path(__file__).parent
    lblpath = str(parentpath) + "\\..\\static\\LabelDocs\\multilabel" + str(timen) + randstr + '.pdf'

    doc = SimpleDocTemplate(lblpath, pagesize=(4 * inch, 6 * inch),
                            showBounday=0.5,
                            leftMargin=0.05 * inch,
                            rightMargin=0.05 * inch,
                            topMargin=0.05 * inch,
                            bottomMargin=0.05 * inch)

    awbstrs = str(awblist).split(',')
    pages = list()

    for awbstr in awbstrs:
        courier = awbstr[-4:]
        awb = awbstr[:len(awbstr)-4]

        if courier == constants.TRACKON:
            courierlogo = 'trackon1.jpg'
        elif courier == constants.PROFESSIONAL:
            courierlogo = 'proff.png'
        elif courier == constants.DTDC:
            courierlogo = 'dtdc.jpeg'
        else:
            courierlogo = 'trackon1.jpg'

        logging.debug(str(courier)+str(awb))
        retcode, labeldata = extractData.getLabelData(awb)

        if courier != '' and awb != '':

            if courier == constants.DELHIVERY:
                logging.debug('entered here DELC')
                retcode, lbldata = DLabelAPI.getDelhiveryLabelData(awb)

                if retcode == 'SUCCESS':
                    printop, page = delhiverylabel(lbldata)
                    pages.extend(page)
                else:
                    logging.debug("No booking found in Delhivery")
            else:
                boxno = 1
                printop, page = othercourier(labeldata, courierlogo, courier, '', boxno)
                pages.extend(page)
                if int(labeldata[8]) > 1:
                    if courier == constants.TRACKON:
                        rcode, rc = extractData.getchildseries(labeldata[0])
                        if rcode == 'ERROR' or rcode == 'FAIL':
                            (printop, labelfilename) = ('N', '')
                        else:
                            for row in rc:
                                boxno = boxno + 1
                                printop, page = othercourier(labeldata, courierlogo, courier, row[1], boxno)
                                pages.extend(page)
                    else:
                        for i in range(2, int(labeldata[8])+1):
                            printop, page = othercourier(labeldata, courierlogo, courier, '', i)
                            pages.extend(page)
        else:
            logging.debug("courier not supported yet:")

    logging.debug(str(len(pages)))
    doc.build(pages)

    return printop, labelfilename


def createLabel(labeldata, courier):

    logging.debug(labeldata)
    logging.debug(courier)
    printop = 'N'
    pages = list()

    labelfilename = '../static/LabelDocs/' + labeldata[0] + '.pdf'
    logging.debug("label filename" + labelfilename)
    parentpath = Path(__file__).parent
    lblpath = str(parentpath) + "\\..\\static\\LabelDocs\\" + labeldata[0] + '.pdf'

    if os.path.isfile(labelfilename):
        return 'Y', labelfilename

    doc = SimpleDocTemplate(lblpath, pagesize=(4 * inch, 6 * inch),showBounday=0.5,leftMargin=0.05 * inch,rightMargin=0.05 * inch,topMargin=0.05 * inch,bottomMargin=0.05 * inch)

    if courier == constants.TRACKON:
        courierlogo = 'trackon1.jpg'
    elif courier == constants.PROFESSIONAL:
        courierlogo = 'proff.png'
    elif courier == constants.DTDC:
        courierlogo = 'dtdc.jpeg'
    else:
        courierlogo = 'trackon1.jpg'


    if courier == constants.DELHIVERY:
        retcode, lbldata = DLabelAPI.getDelhiveryLabelData(labeldata[0])
        if retcode == 'SUCCESS':
            printop, story = delhiverylabel(lbldata)
            pages.extend(story)
    else:
        boxno = 1
        printop, story = othercourier(labeldata, courierlogo, courier, '', boxno)
        pages.extend(story)
        if int(labeldata[8]) > 1:
            if courier == constants.TRACKON:
                rcode, rc = extractData.getchildseries(labeldata[0])
                if rcode == 'ERROR' or rcode == 'FAIL':
                    (printop, labelfilename) = ('N', '')
                else:
                    for row in rc:
                        boxno = boxno + 1
                        printop, story = othercourier(labeldata, courierlogo, courier, row[1], boxno)
                        pages.extend(story)
            else:
                for i in range(2, int(labeldata[8])+1):
                    printop, story = othercourier(labeldata, courierlogo, courier, '', i)
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

    #barcode = labeldata['barcode']
    #barcode = barcode[barcode.find(',')+1:]
    #barcode = base64.b64decode(barcode)

    #f = open('image'+str(rand)+'.png', 'wb')
    #f.write(barcode)
    #f.close()

    #rb = Image('image'+str(rand)+'.png')

    #rb.drawHeight = 2*inch * rb.drawHeight / rb.drawWidth
    #rb.drawWidth = 2*inch

    #barcode = labeldata['obarcode']
    #barcode = barcode[barcode.find(',') + 1:]
    #barcode = base64.b64decode(barcode)

    #f = open('image'+str(rand)+'.png', 'wb')
    #f.write(barcode)
    #f.close()

    #rob = Image('image'+str(rand)+'.png')

    #rob.drawHeight = 2 * inch * rob.drawHeight / rob.drawWidth
    #rob.drawWidth = 2 * inch

    samt = '{:10,.2f}'.format(labeldata['price'])
    if 'cod' in labeldata:
    	camt = '{:10,.2f}'.format(labeldata['cod'])
    else:
        camt = ''

    if str(labeldata.toFreight).upper() == 'COD':
        ptstr = '<b>' + labeldata.toFreight + '<br/> '+str(camt)+'<br/>' + labeldata.toFreight + '</b>'
    else:
        ptstr = '<b>' + labeldata.toFreight + '<br/>' + labeldata.toFreight + '</b>'

    if labeldata.toFreight is not None:
        sortcode = labeldata.toFreight
    else:
        sortcode = ' '

    ps1 = ParagraphStyle('left', alignment=TA_LEFT)
    ps2 = ParagraphStyle('right', alignment=TA_RIGHT)
    ps3 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=6)
    ps4 = ParagraphStyle('normal', alignment=TA_LEFT, fontName='Helvetica', fontSize=7)
    ps5 = ParagraphStyle('normal', alignment=TA_LEFT, fontName='Helvetica', fontSize=8)
    ps5c = ParagraphStyle('normal', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    psb = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=42)
    psbo = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=28)
    p2 = Paragraph(str(labeldata['pin']), style=ps1)
    p3 = Paragraph('<b>'+sortcode+'</b>', style=ps2)
    p4 = Paragraph('Shipping Address:<br/><b>AMIT KUMAR <br/>13/67 TRILOK PURN<br/>DESTINATION<br/>PIN: '+str('110091')+'</b>', style=ps1)
    p9 = Paragraph('Seller: SELLET', style=ps4)
    p11 = Paragraph("Product PRODUCT ", style=ps3)
    p12 = Paragraph("Price", style=ps3)
    p13 = Paragraph("Total", style=ps3) # repeated twice
    p14 = Paragraph(labeldata['prd'], style=ps1)
    p15 = Paragraph(samt, style=ps3) #repeated four times
    p17 = Paragraph('\n'+'OID', style=styleN)
    p18 = Paragraph('Return Address:ADDRESS--PINT', style=ps4)
    p19 = Paragraph(ptstr, style=ps3)
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


def othercourier(labeldata, imagename, courier, childawb, boxno):

    imgpath = '../static/images/' + imagename
    path = Path(__file__).parent / imgpath

    lg = Image(path)

    lg.drawHeight = 1.4 * inch * lg.drawHeight / lg.drawWidth
    lg.drawWidth = 1.4 * inch
    
    iamt = '{:10,.2f}'.format(labeldata[14])

    ps1 = ParagraphStyle('left', alignment=TA_LEFT, fontName='Helvetica', fontSize=10)
    ps1c = ParagraphStyle('center', alignment=TA_LEFT, fontName='Helvetica', fontSize=10)
    ps1x = ParagraphStyle('left', alignment=TA_LEFT, fontName='Helvetica', fontSize=7)
    p1 = Paragraph('Origin', style=ps1)
    p2 = Paragraph('Destination', style=ps1)
    p3 = Paragraph('IXC', style=ps1)
    p4 = Paragraph(labeldata[3], style=ps1)
    ps2 = ParagraphStyle('barcode', alignment=TA_CENTER, fontName='code128', fontSize=48)
    ps3 = ParagraphStyle('center', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    ps3l = ParagraphStyle('left', alignment=TA_CENTER, fontName='Helvetica', fontSize=8)
    ps4 = ParagraphStyle('right', alignment=TA_RIGHT, fontName='Helvetica', fontSize=10)
    ps5 = ParagraphStyle('bold', alignment=TA_LEFT, fontName='Helvetica-Bold', spaceAfter=16, spaceBefore=16, fontSize=12)
    ps6 = ParagraphStyle('lbold', alignment=TA_CENTER, fontName='Helvetica-Bold', fontSize=26)
    p4x = Paragraph("Reference Number", style=ps3)

    if childawb !='':
        p5 = Paragraph(code128encoded(childawb), style=ps2)
        p6 = Paragraph(str(childawb), style=ps3)
    else:
        p5 = Paragraph(code128encoded(labeldata[0]), style=ps2)
        p6 = Paragraph(str(labeldata[0]), style=ps3)
    if childawb == '':
        if int(labeldata[8]) > 1:
            #p5x = Paragraph('BOX: ' + str(boxno) + '/' + str(labeldata[8]), style=ps3l)
            p5x = Paragraph('Piece ' + str(boxno) + ' of ' + str(labeldata[8]) + ' Pieces', style=ps3l)
            p7x = Paragraph('Master AWB', style=ps3l)
    else:
        #p5x = Paragraph('BOX: ' + str(boxno) + '/' + str(labeldata[8]), style=ps3l)
        p5x = Paragraph('Piece ' + str(boxno) + ' of ' + str(labeldata[8]) + ' Pieces', style=ps3l)
        #p6x = Paragraph('Child Package', style=ps3l)
        p7x = Paragraph('Master AWB: '+str(labeldata[0]), style=ps3l)

    p7 = Paragraph('CustRefNo:'+str(labeldata[10]).upper(), style=ps1x)
    p8 = Paragraph('Mode:'+labeldata[7], style=ps4)
    p9 = Paragraph('TO:<br/>'+labeldata[2].upper()+'<br/>'+labeldata[4].upper()+'<br/>'+labeldata[5].upper()+' '+labeldata[3].upper()+' '+str(labeldata[6])+'<br/>Ph:'+str(labeldata[11]), style=ps5)
    p10 = Paragraph('PCS: '+str(labeldata[8]), style=ps1)
    p10x = Paragraph('Dt: '+str(labeldata[13])[:str(labeldata[13]).rfind('.')], style=ps4)
    pinv = Paragraph('Shipment Value: '+str(iamt), style=ps1)
    p11 = Paragraph('WEIGHT: '+str(labeldata[9]), style=ps4)
    p12 = Paragraph('Remarks: ', style=ps1)
    p13 = Paragraph('Contains: '+ labeldata[12], style=ps1)
    p14 = Paragraph('From/Return Details: '+labeldata[1], style=ps1x)

    if courier == constants.TRACKON:
        p15 = Paragraph('Track your shipment at <b>trackon.in</b>', style=ps1)
    elif courier == constants.PROFESSIONAL:
        p15 = Paragraph('Track your shipment at <b>tpcindia.com</b>', style=ps1)
    elif courier == constants.DTDC:
        p15 = Paragraph('Track your shipment at <b>www.dtdc.in</b>', style=ps1)
    else:
        p15 = Paragraph('          ', style=ps1) #need to fill this when identified

    p16 = Paragraph(str(labeldata[7]).strip().upper(), style=ps6)

    #p17 = Paragraph(code128encoded(labeldata[0]), style=ps2)
    #p18 = Paragraph(str(labeldata[0]), style=ps3)

    t1 = Table([[lg, p1, p2], ['', p3, p4]], style=[('GRID', (0, 0), (2, 1), 0.5, colors.black),
                                                    ('SPAN', (0, 0), (0, 1))])
    t1._argW[0] = 1.5*inch
    t1._argW[1] = 0.6*inch

    if childawb != '':
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

    if childawb != '':
        t2xx = Table([[p7x, p5x]], style=[('GRID', (0, 0), (2, 0), 0.5, colors.black)])
        t2xx._argW[0] = 1.9 * inch
    else:
        if int(labeldata[8]) > 1:
            if courier == constants.TRACKON:
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

    #t8 = Table([[p17], [p18]], style=[('BOX', (0, 0), (2, 2), 0.5, colors.black),
    #                                ('VALIGN', (0, 0), (1, 0), 'TOP')])
    #t8._argH[0] = 0.82 * inch
    #t8._argW[0] = 3.735 * inch

    if childawb == '':
        if int(labeldata[8]) > 1:
            story = [t1, t2xx, t2,  t2x, t3, t4, t5, t6, t7, PageBreak()]
        else:
            story = [t1, t2, t2x, t3, t4, t5, t6, t7, PageBreak()]
    else:
        story = [t1, t2xx, t2, t2x, t3, t4, t5, t6, t7, PageBreak()]

    return 'Y', story

def code128encoded(data):

    encodestr = constants.STARTCHAR+data

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

    encodestr += chkchar+constants.STOPCHAR

    logging.debug(str(encodestr))

    return str(encodestr)
