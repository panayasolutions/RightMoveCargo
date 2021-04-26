from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    class Meta:
        managed = True
        db_table = 'tbBookingWeb'
    id = models.CharField(auto_created=True,primary_key=True, max_length=30,db_column='EntryId',blank=True,unique=True)  # Field name made lowercase.
    awbno = models.CharField(db_column='AwbNo', blank=True, null=True,max_length=50)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo',blank=True, null=True, max_length=50)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode',blank=True, null=True, max_length=10)  # Field name made lowercase.
    clientcode = models.CharField(db_column='ClientCode', blank=True, null=True,max_length=10)  # Field name made lowercase.
    couriercode = models.CharField(db_column='CourierCode',blank=True, null=True, max_length=10)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', blank=True, null=True,max_length=100)  # Field name made lowercase.
    topay = models.CharField(db_column='Topay',blank=True, null=True, max_length=10)  # Field name made lowercase.
    cod = models.CharField(db_column='COD',blank=True, null=True, max_length=15)  # Field name made lowercase.
    riskcoveredby = models.CharField(db_column='RiskCoveredBy',blank=True, null=True, max_length=10)  # Field name made lowercase.
    recname = models.CharField(db_column='RecName',blank=True, null=True, max_length=100)  # Field name made lowercase.
    recaddr1 = models.CharField(db_column='RecAddr1',blank=True, null=True, max_length=100)  # Field name made lowercase.
    recaddr2 = models.CharField(db_column='RecAddr2',blank=True, null=True, max_length=100)  # Field name made lowercase.
    recphone = models.CharField(db_column='RecPhone',blank=True, null=True, max_length=100)  # Field name made lowercase.
    recmail = models.CharField(db_column='RecMail',blank=True, null=True, max_length=100)  # Field name made lowercase.
    recpin = models.CharField(db_column='RecPin',blank=True, null=True, max_length=6)  # Field name made lowercase.
    recdestination = models.CharField(db_column='RecDestination',blank=True, null=True, max_length=50)  # Field name made lowercase.
    recstate = models.CharField(db_column='RecState',blank=True, null=True, max_length=2)  # Field name made lowercase.
    oda = models.CharField(db_column='ODA',blank=True, null=True, max_length=10)  # Field name made lowercase.
    ewaybillno = models.CharField(db_column='EwayBillNo',blank=True, null=True, max_length=50)  # Field name made lowercase.
    invoicevalue = models.CharField(db_column='InvoiceValue',blank=True, null=True, max_length=12)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber',blank=True, null=True, max_length=50)  # Field name made lowercase.
    productdesc = models.CharField(db_column='ProductDesc',blank=True, null=True, max_length=50)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode',blank=True, null=True, max_length=10)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType',blank=True, null=True, max_length=10)  # Field name made lowercase.
    pcs = models.IntegerField(db_column='PCS',blank=True, null=True)  # Field name made lowercase.
    actweight = models.DecimalField(db_column='ActWeight',default=0.00, max_digits=5, decimal_places=2)  # Field name made lowercase.
    referenceid = models.CharField(db_column='ReferenceId',blank=True, null=True, max_length=50)  # Field name made lowercase.
    dimensions = models.CharField(db_column='Dimensions',blank=True, null=True, max_length=15)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty',blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length',blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height',blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width',blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase.
    submitteduser = models.CharField(db_column='SubmittedUser',blank=True, null=True, max_length=50)  # Field name made lowercase.
    recdfrom = models.CharField(db_column='RecdFrom',blank=True, null=True, max_length=10)  # Field name made lowercase.
    byhub = models.CharField(db_column='ByHub',blank=True, null=True, max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType',blank=True, null=True, max_length=10)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate',blank=True, null=True)  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='EntryTime',blank=True, null=True)  # Field name made lowercase.
    entrydatetime = models.DateTimeField(db_column='EntryDateTime',blank=True, null=True)  # Field name made lowercase.
    enterby = models.CharField(db_column='EnterBy', blank=True, null=True,max_length=10)  # Field name made lowercase.
    cliname = models.CharField(db_column='CliName', blank=True, null=True,max_length=100)  # Field name made lowercase.
    cliphone = models.CharField(db_column='CliPhone',blank=True, null=True, max_length=100)  # Field name made lowercase.
    climail = models.CharField(db_column='CliMail',blank=True, null=True, max_length=100)  # Field name made lowercase.
    cliadd = models.CharField(db_column='CliAdd',blank=True, null=True, max_length=100)  # Field name made lowercase.
    clipin = models.CharField(db_column='CliPin',blank=True, null=True, max_length=6)  # Field name made lowercase.