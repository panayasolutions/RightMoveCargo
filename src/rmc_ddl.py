# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Awbseries(models.Model):
    couriercode = models.CharField(db_column='CourierCode', primary_key=True, max_length=10)  # Field name made lowercase.
    awbtype = models.CharField(db_column='AWBType', max_length=1)  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=10)  # Field name made lowercase.
    awbstart = models.CharField(db_column='AWBStart', max_length=50)  # Field name made lowercase.
    awbend = models.CharField(db_column='AWBEnd', max_length=50)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=3)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=1)  # Field name made lowercase.
    lastusedawb = models.CharField(db_column='LastUsedAWB', max_length=50)  # Field name made lowercase.
    lastupdateduserid = models.CharField(db_column='LastUpdatedUserId', max_length=50)  # Field name made lowercase.
    lastupdatedtimestamp = models.DateTimeField(db_column='LastUpdatedTimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AWBSeries'
        unique_together = (('couriercode', 'weight'),)


class Tbbilling181220(models.Model):
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
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
        db_table = 'TBBILLING181220'


class DCode(models.Model):
    pin = models.FloatField(blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    statecode = models.CharField(max_length=255, blank=True, null=True)
    oda = models.CharField(db_column='ODA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_code'


class Datapostalpin(models.Model):
    areaname = models.CharField(db_column='AreaName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pincode = models.FloatField(db_column='PinCode', blank=True, null=True)  # Field name made lowercase.
    divisionname = models.CharField(db_column='DivisionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regionname = models.CharField(db_column='RegionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    circlename = models.CharField(db_column='CircleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    districtname = models.CharField(db_column='DistrictName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entryid = models.AutoField(db_column='EntryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataPostalPin'


class Dc(models.Model):
    pin = models.FloatField(blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    statecode = models.CharField(max_length=255, blank=True, null=True)
    oda = models.CharField(db_column='ODA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dc'


class Hisbilling(models.Model):
    history = models.CharField(db_column='History', max_length=100)  # Field name made lowercase.
    entryid = models.BigIntegerField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=50)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    originzone = models.CharField(db_column='OriginZone', max_length=10)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=10)  # Field name made lowercase.
    courier = models.CharField(db_column='Courier', max_length=10)  # Field name made lowercase.
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
    consignee = models.CharField(db_column='Consignee', max_length=100)  # Field name made lowercase.
    fuelchg = models.DecimalField(db_column='FuelChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fuelamt = models.DecimalField(db_column='FuelAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    devpchg = models.DecimalField(db_column='DevpChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    devpamt = models.DecimalField(db_column='DevpAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    gramount = models.DecimalField(db_column='GRAmount', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hisBilling'


class Hisbooking(models.Model):
    history = models.CharField(db_column='History', max_length=100)  # Field name made lowercase.
    entryid = models.BigIntegerField(db_column='EntryId')  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50)  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
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
        db_table = 'hisBooking'


class Hisdelivery(models.Model):
    history = models.CharField(db_column='History', max_length=50)  # Field name made lowercase.
    entryid = models.BigIntegerField(db_column='EntryId')  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100)  # Field name made lowercase.
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
        db_table = 'hisDelivery'


class Hisinscan(models.Model):
    history = models.CharField(db_column='History', max_length=100)  # Field name made lowercase.
    entryid = models.BigIntegerField(db_column='EntryId')  # Field name made lowercase.
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
        db_table = 'hisInscan'


class Hismanifest(models.Model):
    history = models.CharField(db_column='History', max_length=50)  # Field name made lowercase.
    entryid = models.BigIntegerField(db_column='EntryId', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'hisManifest'


class Hisofd(models.Model):
    history = models.CharField(db_column='History', max_length=100)  # Field name made lowercase.
    entryid = models.BigIntegerField(db_column='EntryId')  # Field name made lowercase.
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
        db_table = 'hisOFD'


class Mtbranch(models.Model):
    branchcode = models.CharField(db_column='BranchCode', primary_key=True, max_length=10)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=100)  # Field name made lowercase.
    branchtype = models.CharField(db_column='BranchType', max_length=50)  # Field name made lowercase.
    branchincharge = models.CharField(db_column='BranchInCharge', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=6)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=100)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=100)  # Field name made lowercase.
    idproof = models.CharField(db_column='IdProof', max_length=100)  # Field name made lowercase.
    addproof = models.CharField(db_column='AddProof', max_length=100)  # Field name made lowercase.
    panno = models.CharField(db_column='PanNo', max_length=100)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=3)  # Field name made lowercase.
    activedate = models.DateTimeField(db_column='ActiveDate')  # Field name made lowercase.
    servicearea = models.CharField(db_column='ServiceArea', max_length=10)  # Field name made lowercase.
    inpermission = models.CharField(db_column='InPermission', max_length=10)  # Field name made lowercase.
    outpermission = models.CharField(db_column='OutPermission', max_length=10)  # Field name made lowercase.
    rategroup = models.CharField(db_column='RateGroup', max_length=10)  # Field name made lowercase.
    applytax = models.CharField(db_column='ApplyTax', max_length=3)  # Field name made lowercase.
    ratetype = models.CharField(db_column='RateType', max_length=10)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIn', max_length=50)  # Field name made lowercase.
    creditlimit = models.BigIntegerField(db_column='CreditLimit')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    enterdatetime = models.DateTimeField(db_column='EnterDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    hubcode = models.CharField(db_column='HubCode', max_length=10)  # Field name made lowercase.
    couriertype = models.CharField(db_column='CourierType', max_length=10)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtBranch'


class Mtcitymapping(models.Model):
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', primary_key=True, max_length=10)  # Field name made lowercase.
    zonedox = models.CharField(db_column='ZoneDox', max_length=5)  # Field name made lowercase.
    zonenondox = models.CharField(db_column='ZoneNonDox', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtCityMapping'
        unique_together = (('destination', 'company'),)


class Mtcompany(models.Model):
    companycode = models.CharField(db_column='CompanyCode', max_length=10)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMailId', max_length=50)  # Field name made lowercase.
    cinno = models.CharField(db_column='CINNo', max_length=50)  # Field name made lowercase.
    panno = models.CharField(db_column='PANNo', max_length=50)  # Field name made lowercase.
    gstno = models.CharField(db_column='GSTNo', max_length=50)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    courier = models.CharField(db_column='Courier', max_length=10)  # Field name made lowercase.
    couriertype = models.CharField(db_column='CourierType', max_length=10)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=5)  # Field name made lowercase.
    activedate = models.DateTimeField(db_column='ActiveDate')  # Field name made lowercase.
    term1 = models.CharField(db_column='Term1', max_length=100)  # Field name made lowercase.
    term2 = models.CharField(db_column='Term2', max_length=100)  # Field name made lowercase.
    term3 = models.CharField(db_column='Term3', max_length=100)  # Field name made lowercase.
    term4 = models.CharField(db_column='Term4', max_length=100)  # Field name made lowercase.
    term5 = models.CharField(db_column='Term5', max_length=100)  # Field name made lowercase.
    term6 = models.CharField(db_column='Term6', max_length=100)  # Field name made lowercase.
    term7 = models.CharField(db_column='Term7', max_length=100)  # Field name made lowercase.
    term8 = models.CharField(db_column='Term8', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtCompany'


class Mtconsignee(models.Model):
    conscode = models.CharField(db_column='ConsCode', primary_key=True, max_length=10)  # Field name made lowercase.
    consname = models.CharField(db_column='ConsName', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=6)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=100)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=100)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=3)  # Field name made lowercase.
    activedate = models.DateTimeField(db_column='ActiveDate')  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=10)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    enterdatetime = models.DateTimeField(db_column='EnterDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100)  # Field name made lowercase.
    branchincharge = models.CharField(db_column='BranchInCharge', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtConsignee'


class Mtcourier(models.Model):
    branchcode = models.CharField(db_column='BranchCode', primary_key=True, max_length=10)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100)  # Field name made lowercase.
    branchincharge = models.CharField(db_column='BranchInCharge', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=6)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=100)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=100)  # Field name made lowercase.
    idproof = models.CharField(db_column='IdProof', max_length=100)  # Field name made lowercase.
    addproof = models.CharField(db_column='AddProof', max_length=100)  # Field name made lowercase.
    panno = models.CharField(db_column='PanNo', max_length=100)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=3)  # Field name made lowercase.
    activedate = models.DateTimeField(db_column='ActiveDate')  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIn', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    enterdatetime = models.DateTimeField(db_column='EnterDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100)  # Field name made lowercase.
    website = models.CharField(db_column='WebSite', max_length=100)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtCourier'


class Mtcustomer(models.Model):
    branchcode = models.CharField(db_column='BranchCode', primary_key=True, max_length=10)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100)  # Field name made lowercase.
    branchincharge = models.CharField(db_column='BranchInCharge', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=6)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=100)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=100)  # Field name made lowercase.
    idproof = models.CharField(db_column='IdProof', max_length=100)  # Field name made lowercase.
    addproof = models.CharField(db_column='AddProof', max_length=100)  # Field name made lowercase.
    panno = models.CharField(db_column='PanNo', max_length=100)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=3)  # Field name made lowercase.
    activedate = models.DateTimeField(db_column='ActiveDate')  # Field name made lowercase.
    applytax = models.CharField(db_column='ApplyTax', max_length=3)  # Field name made lowercase.
    couriertype = models.CharField(db_column='CourierType', max_length=50)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIn', max_length=50)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    creditlimit = models.BigIntegerField(db_column='CreditLimit')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    enterdatetime = models.DateTimeField(db_column='EnterDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    servicearea = models.CharField(db_column='ServiceArea', max_length=50)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100)  # Field name made lowercase.
    ratetype = models.CharField(db_column='RateType', max_length=10)  # Field name made lowercase.
    othertext = models.CharField(db_column='OtherText', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtCustomer'


class Mtdestination(models.Model):
    destinationcode = models.CharField(db_column='DestinationCode', primary_key=True, max_length=10)  # Field name made lowercase.
    destinationname = models.CharField(db_column='DestinationName', max_length=50)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=5)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.
    oda = models.CharField(db_column='ODA', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtDestination'


class Mtfuelchg(models.Model):
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=10)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    fueldox = models.DecimalField(db_column='FuelDox', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fuelnondox = models.DecimalField(db_column='FuelNondox', max_digits=19, decimal_places=4)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.
    docchg = models.DecimalField(db_column='DocChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    courier = models.CharField(db_column='Courier', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtFuelChg'


class Mtglobalchg(models.Model):
    igst = models.DecimalField(db_column='IGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sgst = models.DecimalField(db_column='SGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cgst = models.DecimalField(db_column='CGST', max_digits=19, decimal_places=4)  # Field name made lowercase.
    gsttype = models.CharField(db_column='GSTType', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtGlobalChg'


class Mtissue(models.Model):
    issueno = models.BigIntegerField(db_column='IssueNo')  # Field name made lowercase.
    issuedate = models.DateTimeField(db_column='IssueDate')  # Field name made lowercase.
    issuefromhub = models.CharField(db_column='IssueFromHub', max_length=10)  # Field name made lowercase.
    issuetohub = models.CharField(db_column='IssueToHub', max_length=10)  # Field name made lowercase.
    awbnofrom = models.CharField(db_column='AwbNoFrom', max_length=50)  # Field name made lowercase.
    awbnoto = models.CharField(db_column='AwbNoTo', max_length=50)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=5)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=5)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtIssue'


class Mtitem(models.Model):
    itemcode = models.CharField(db_column='ItemCode', max_length=10)  # Field name made lowercase.
    itemdesp = models.CharField(db_column='ItemDesp', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    applycharges = models.CharField(db_column='ApplyCharges', max_length=5)  # Field name made lowercase.
    fuelchg = models.DecimalField(db_column='FuelChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otherchg = models.DecimalField(db_column='OtherChg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtItem'


class Mtncrrate(models.Model):
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=10)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.
    wtfrom = models.DecimalField(db_column='WtFrom', max_digits=19, decimal_places=4)  # Field name made lowercase.
    wtto = models.DecimalField(db_column='WtTo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ratezone = models.CharField(db_column='RateZone', max_length=5)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=10)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=10)  # Field name made lowercase.
    divide = models.DecimalField(db_column='Divide', max_digits=19, decimal_places=4)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    addwt = models.DecimalField(db_column='AddWt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    addrt = models.DecimalField(db_column='AddRt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    ratefor = models.CharField(db_column='RateFor', max_length=10)  # Field name made lowercase.
    entryid = models.BigAutoField(db_column='EntryId')  # Field name made lowercase.
    courier = models.CharField(db_column='Courier', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtNCRRate'


class Mtoriginzone(models.Model):
    zonecode = models.CharField(db_column='ZoneCode', max_length=5)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtOriginZone'


class Mtpin(models.Model):
    pincode = models.CharField(db_column='PinCode', primary_key=True, max_length=6)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=10)  # Field name made lowercase.
    destinationcode = models.CharField(db_column='DestinationCode', max_length=10)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtPin'


class Mtratezone(models.Model):
    zonecode = models.CharField(db_column='ZoneCode', max_length=5)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=50)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtRateZone'


class Mtstate(models.Model):
    statecode = models.CharField(db_column='StateCode', primary_key=True, max_length=5)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=50)  # Field name made lowercase.
    zonecode = models.CharField(db_column='ZoneCode', max_length=5)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtState'


class Mtstatus(models.Model):
    remarks = models.CharField(db_column='Remarks', primary_key=True, max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtStatus'
        unique_together = (('remarks', 'status'),)


class Mttopayrate(models.Model):
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    amtfrom = models.DecimalField(db_column='AmtFrom', max_digits=19, decimal_places=4)  # Field name made lowercase.
    amtto = models.DecimalField(db_column='AmtTo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtTopayRate'


class Mtuserrevenue(models.Model):
    userid = models.CharField(db_column='UserId', primary_key=True, max_length=10)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='UserPassword', max_length=100)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=10)  # Field name made lowercase.
    userrights = models.CharField(db_column='UserRights', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    editby = models.CharField(db_column='EditBy', max_length=10)  # Field name made lowercase.
    editdatetime = models.DateTimeField(db_column='EditDateTime')  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=5)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=255)  # Field name made lowercase.
    resettoken = models.CharField(db_column='ResetToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resettimestamp = models.DateTimeField(db_column='ResetTimeStamp', blank=True, null=True)  # Field name made lowercase.
    iv = models.CharField(db_column='IV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invalidcount = models.IntegerField(db_column='InvalidCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtUserRevenue'


class Mtvalue(models.Model):
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=10)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    per = models.DecimalField(db_column='Per', max_digits=19, decimal_places=4)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDatetime')  # Field name made lowercase.
    courier = models.CharField(db_column='Courier', max_length=10)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=10)  # Field name made lowercase.
    client = models.CharField(db_column='Client', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtValue'


class Mtzone(models.Model):
    zonecode = models.CharField(db_column='ZoneCode', max_length=5)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=50)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', max_length=10)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtZone'


class Nd(models.Model):
    destinationcode = models.FloatField(db_column='DestinationCode', blank=True, null=True)  # Field name made lowercase.
    destinationname = models.CharField(db_column='DestinationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=255)  # Field name made lowercase.
    f5 = models.DateTimeField(db_column='F5')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nd'


class Nd1(models.Model):
    destinationcode = models.FloatField(db_column='DestinationCode', blank=True, null=True)  # Field name made lowercase.
    destinationname = models.CharField(db_column='DestinationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f5 = models.DateTimeField(db_column='F5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nd1'


class Tbbillreg(models.Model):
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
        db_table = 'tbBillReg'


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


class Tbbookingchild(models.Model):
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
