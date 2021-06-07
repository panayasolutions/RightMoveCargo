# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbbillregCopy610(models.Model):
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=50)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=50)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    datefrom = models.DateTimeField(db_column='DateFrom')  # Field name made lowercase.
    dateto = models.DateTimeField(db_column='DateTo')  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate')  # Field name made lowercase.
    billstatus = models.CharField(db_column='BillStatus', max_length=10)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fuelamount = models.DecimalField(db_column='FuelAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    igstamt = models.DecimalField(db_column='IGSTAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sgstamt = models.DecimalField(db_column='SGSTAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cgstamt = models.DecimalField(db_column='CGSTAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    igst = models.DecimalField(db_column='IGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sgst = models.DecimalField(db_column='SGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cgst = models.DecimalField(db_column='CGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    gramount = models.DecimalField(db_column='GRAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=5)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    odaamount = models.DecimalField(db_column='ODAAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    docamount = models.DecimalField(db_column='DOCAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otheramount = models.DecimalField(db_column='OtherAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    topayamount = models.DecimalField(db_column='TopayAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codamount = models.DecimalField(db_column='CODAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    riskamount = models.DecimalField(db_column='RiskAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    discountval = models.DecimalField(db_column='DiscountVal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    discounttype = models.CharField(db_column='DiscountType', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbBillReg_copy610'


class Tbbilling(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', primary_key=True, max_length=50)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=50)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    bookedcourier = models.CharField(db_column='BookedCourier', max_length=10)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=10)  # Field name made lowercase.
    forwardcourier = models.CharField(db_column='ForwardCourier', max_length=10)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=10)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=10)  # Field name made lowercase.
    ratezone = models.CharField(db_column='RateZone', max_length=10)  # Field name made lowercase.
    oda = models.CharField(db_column='ODA', max_length=10)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=50)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=10)  # Field name made lowercase.
    topay = models.BigIntegerField(db_column='Topay')  # Field name made lowercase.
    cod = models.BigIntegerField(db_column='COD')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=10)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='PCS')  # Field name made lowercase.
    actweight = models.DecimalField(db_column='ActWeight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    volweight = models.DecimalField(db_column='VolWeight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=50)  # Field name made lowercase.
    topaychg = models.DecimalField(db_column='TopayChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codchg = models.DecimalField(db_column='CODChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otherchg = models.DecimalField(db_column='OtherChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    actamount = models.DecimalField(db_column='ActAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    invvalue = models.DecimalField(db_column='InvValue', max_digits=19, decimal_places=4)  # Field name made lowercase.
    riskcoveredby = models.CharField(db_column='RiskCoveredBy', max_length=10)  # Field name made lowercase.
    riskchg = models.DecimalField(db_column='RiskChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    saletype = models.CharField(db_column='SaleType', max_length=10)  # Field name made lowercase.
    fuelchg = models.DecimalField(db_column='FuelChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fuelamt = models.DecimalField(db_column='FuelAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    riskper = models.DecimalField(db_column='RiskPer', max_digits=19, decimal_places=4)  # Field name made lowercase.
    odachg = models.DecimalField(db_column='ODAChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    docchg = models.DecimalField(db_column='DocChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    gramount = models.DecimalField(db_column='GRAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    consaddress = models.CharField(db_column='ConsAddress', max_length=100)  # Field name made lowercase.
    consmail = models.CharField(db_column='ConsMail', max_length=100)  # Field name made lowercase.
    consphone = models.CharField(db_column='ConsPhone', max_length=50)  # Field name made lowercase.
    consignee = models.CharField(db_column='Consignee', max_length=100)  # Field name made lowercase.
    pickupby = models.CharField(db_column='PickupBy', max_length=10)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=100)  # Field name made lowercase.
    clientadd = models.CharField(db_column='ClientAdd', max_length=100)  # Field name made lowercase.
    clientcity = models.CharField(db_column='ClientCity', max_length=100)  # Field name made lowercase.
    clientstate = models.CharField(db_column='ClientState', max_length=100)  # Field name made lowercase.
    clientpin = models.CharField(db_column='ClientPin', max_length=100)  # Field name made lowercase.
    clientphone = models.CharField(db_column='ClientPhone', max_length=10)  # Field name made lowercase.
    clientmail = models.CharField(db_column='ClientMail', max_length=100)  # Field name made lowercase.
    clientgst = models.CharField(db_column='ClientGST', max_length=50)  # Field name made lowercase.
    vas = models.CharField(db_column='VAS', max_length=20)  # Field name made lowercase.
    vastax = models.DecimalField(db_column='VASTax', max_digits=19, decimal_places=4)  # Field name made lowercase.
    datasource = models.CharField(db_column='DataSource', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbBilling'


class TbbillingCopy610(models.Model):
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=50)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=50)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    datefrom = models.DateTimeField(db_column='DateFrom')  # Field name made lowercase.
    dateto = models.DateTimeField(db_column='DateTo')  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate')  # Field name made lowercase.
    billstatus = models.CharField(db_column='BillStatus', max_length=10)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fuelamount = models.DecimalField(db_column='FuelAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    igstamt = models.DecimalField(db_column='IGSTAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sgstamt = models.DecimalField(db_column='SGSTAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cgstamt = models.DecimalField(db_column='CGSTAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    igst = models.DecimalField(db_column='IGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sgst = models.DecimalField(db_column='SGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cgst = models.DecimalField(db_column='CGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    gramount = models.DecimalField(db_column='GRAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=5)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    odaamount = models.DecimalField(db_column='ODAAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    docamount = models.DecimalField(db_column='DOCAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otheramount = models.DecimalField(db_column='OtherAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    topayamount = models.DecimalField(db_column='TopayAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codamount = models.DecimalField(db_column='CODAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    riskamount = models.DecimalField(db_column='RiskAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    discountval = models.DecimalField(db_column='DiscountVal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    discounttype = models.CharField(db_column='DiscountType', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbBilling_copy610'


class Tbbooking(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50)  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', primary_key=True, max_length=50)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=50)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    recdfrom = models.CharField(db_column='RecdFrom', max_length=10)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub', max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='EntryTime')  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=10)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=10)  # Field name made lowercase.
    oda = models.CharField(db_column='ODA', max_length=10)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=250)  # Field name made lowercase.
    invoicevalue = models.BigIntegerField(db_column='InvoiceValue')  # Field name made lowercase.
    riskcoveredby = models.CharField(db_column='RiskCoveredBy', max_length=10)  # Field name made lowercase.
    topay = models.BigIntegerField(db_column='Topay')  # Field name made lowercase.
    cod = models.BigIntegerField(db_column='COD')  # Field name made lowercase.
    contents = models.CharField(db_column='Contents', max_length=50)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=10)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='PCS')  # Field name made lowercase.
    actweight = models.DecimalField(db_column='ActWeight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    volweight = models.DecimalField(db_column='VolWeight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ewaybillno = models.CharField(db_column='EwayBillNo', max_length=50)  # Field name made lowercase.
    transportid = models.CharField(db_column='TransportId', max_length=50)  # Field name made lowercase.
    recname = models.CharField(db_column='RecName', max_length=100)  # Field name made lowercase.
    recadd = models.CharField(db_column='RecAdd', max_length=100)  # Field name made lowercase.
    recphone = models.CharField(db_column='RecPhone', max_length=100)  # Field name made lowercase.
    recmail = models.CharField(db_column='RecMail', max_length=100)  # Field name made lowercase.
    cliname = models.CharField(db_column='CliName', max_length=100)  # Field name made lowercase.
    cliphone = models.CharField(db_column='CliPhone', max_length=100)  # Field name made lowercase.
    climail = models.CharField(db_column='CliMail', max_length=100)  # Field name made lowercase.
    cliadd = models.CharField(db_column='CliAdd', max_length=100)  # Field name made lowercase.
    clipin = models.CharField(db_column='CliPin', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbBooking'


class ChildBooking(models.Model):
    masterawbno = models.CharField(db_column='MasterAwbNo', primary_key=True, max_length=50)  # Field name made lowercase.
    childawb = models.CharField(db_column='ChildAwb', max_length=50)  # Field name made lowercase.
    actweight = models.DecimalField(db_column='ActWeight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    submitteduser = models.CharField(db_column='SubmittedUser', max_length=50)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbBookingChild'
        unique_together = (('masterawbno', 'childawb'),)


class Tbbookingweb(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', primary_key=True, max_length=50)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=10)  # Field name made lowercase.
    clientcode = models.CharField(db_column='ClientCode', max_length=10)  # Field name made lowercase.
    couriercode = models.CharField(db_column='CourierCode', max_length=10)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=100)  # Field name made lowercase.
    topay = models.CharField(db_column='Topay', max_length=10)  # Field name made lowercase.
    cod = models.DecimalField(db_column='COD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    riskcoveredby = models.CharField(db_column='RiskCoveredBy', max_length=10)  # Field name made lowercase.
    recname = models.CharField(db_column='RecName', max_length=100)  # Field name made lowercase.
    recaddr1 = models.CharField(db_column='RecAddr1', max_length=100)  # Field name made lowercase.
    recaddr2 = models.CharField(db_column='RecAddr2', max_length=100)  # Field name made lowercase.
    recphone = models.CharField(db_column='RecPhone', max_length=100)  # Field name made lowercase.
    recmail = models.CharField(db_column='RecMail', max_length=100)  # Field name made lowercase.
    recpin = models.CharField(db_column='RecPin', max_length=6)  # Field name made lowercase.
    recdestination = models.CharField(db_column='RecDestination', max_length=50)  # Field name made lowercase.
    recstate = models.CharField(db_column='RecState', max_length=2)  # Field name made lowercase.
    oda = models.CharField(db_column='ODA', max_length=10)  # Field name made lowercase.
    ewaybillno = models.CharField(db_column='EwayBillNo', max_length=50)  # Field name made lowercase.
    invoicevalue = models.DecimalField(db_column='InvoiceValue', max_digits=19, decimal_places=4)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=50)  # Field name made lowercase.
    productdesc = models.CharField(db_column='ProductDesc', max_length=50)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=10)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=10)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='PCS')  # Field name made lowercase.
    actweight = models.DecimalField(db_column='ActWeight', max_digits=5, decimal_places=2)  # Field name made lowercase.
    referenceid = models.CharField(db_column='ReferenceId', max_length=50)  # Field name made lowercase.
    dimensions = models.CharField(db_column='Dimensions', max_length=15)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=5, decimal_places=2)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=5, decimal_places=2)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=5, decimal_places=2)  # Field name made lowercase.
    submitteduser = models.CharField(db_column='SubmittedUser', max_length=50)  # Field name made lowercase.
    recdfrom = models.CharField(db_column='RecdFrom', max_length=10)  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub', max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='EntryTime')  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    cliname = models.CharField(db_column='CliName', max_length=100)  # Field name made lowercase.
    cliphone = models.CharField(db_column='CliPhone', max_length=100)  # Field name made lowercase.
    climail = models.CharField(db_column='CliMail', max_length=100)  # Field name made lowercase.
    cliadd = models.CharField(db_column='CliAdd', max_length=100)  # Field name made lowercase.
    clipin = models.CharField(db_column='CliPin', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbBookingWeb'


class Tbdelivery(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50)  # Field name made lowercase.
    recdby = models.CharField(db_column='RecdBy', max_length=50)  # Field name made lowercase.
    statusdate = models.DateTimeField(db_column='StatusDate')  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub', max_length=10)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    drsno = models.CharField(db_column='DRSNo', max_length=50)  # Field name made lowercase.
    entrysource = models.CharField(db_column='EntrySource', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbDelivery'


class Tbinscan(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='EntryTime')  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub', max_length=10)  # Field name made lowercase.
    fromhub = models.CharField(db_column='FromHub', max_length=10)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='Pcs')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    sealno = models.CharField(db_column='SealNo', max_length=50)  # Field name made lowercase.
    entrysource = models.CharField(db_column='EntrySource', max_length=10)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbInscan'


class Tbmanifest(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    mfno = models.CharField(db_column='MFNo', max_length=50)  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
    slno = models.IntegerField(db_column='SlNo')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='EntryTime')  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub', max_length=10)  # Field name made lowercase.
    tohub = models.CharField(db_column='ToHub', max_length=10)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='Pcs')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    sealno = models.CharField(db_column='SealNo', max_length=50)  # Field name made lowercase.
    entrysource = models.CharField(db_column='EntrySource', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbManifest'


class Tbofd(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    mfno = models.CharField(db_column='MFNo', max_length=50)  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
    slno = models.IntegerField(db_column='SlNo')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='EntryTime')  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub', max_length=10)  # Field name made lowercase.
    tohub = models.CharField(db_column='ToHub', max_length=10)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='Pcs')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=100)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    consignee = models.CharField(db_column='Consignee', max_length=100)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    entrysource = models.CharField(db_column='EntrySource', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbOFD'
