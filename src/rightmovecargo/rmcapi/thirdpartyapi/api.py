import json
from os import WEXITED
from pathlib import Path
import requests

from django.http import request

from rightmovecargo.rmcapi.models import ChildBooking, CityMapping, Client, Courier, Destination, PinCode
from rightmovecargo.rmcapi.constants import constant

# from rightmovecargo.rmcapi.thirdpartyapi import api;
# api.get_url('TCPL','TCPL','track',["AWBNo"])
# api.get_url('DELC','RIGHTMOVELOGISTICSLW','pin',[])
# from rightmovecargo.rmcapi.thirdpartyapi import api
# api = api.API()
# api.get_client_by_booking('110091','DOX','0','SURFACE')

rmc_path=Path(__file__).parent.parent;
rmc_path = str(rmc_path);
thirdpartyapi_path=rmc_path+"/thirdpartyapi";
auth_path=thirdpartyapi_path+"/oauth.json";

class API:

    def get_url(self,courier,authfor,urltype,oparams):
        # print(auth_path);
        f = open(auth_path,)
        data = json.load(f);
        auth = data[courier]['auth'][authfor]
        uri = data[courier]['uris'][urltype]
        url = auth['baseurl']+uri['uri'];
        authindex = uri['authindex'];
        params = "";
        seprator = "?";
        counter = 0;
        paramcounter = 0;
        for param in uri['params']:
            value = "";
            if(counter!=0):
                seprator = "&";
            if(authindex>=counter):
                value = auth[param];
            else:
                if(len(oparams)==paramcounter):
                    break;
                if(oparams[paramcounter] == None):
                    value = '';
                else:
                    value = oparams[paramcounter] 
                paramcounter = paramcounter+1;       
            params = params +seprator+param+"="+value
            counter = counter + 1;
        fullurl = url+params;

        f.close()
        return fullurl;


    def get_response(self,courier,authfor,urltype):
        f = open(auth_path,)
        data = json.load(f);
        response = data[courier]['uris'][urltype]['response']
        f.close();
        return response;


    def get_pin_code(self,courier,oparams):
        pinCodes = list();
        if courier == constant.TRACKON:
            pinCodes = list()
        elif courier== constant.PROFESSIONAL:
            pinCodes = list()
        elif courier == constant.DTDC:
            pinCodes = list()
        elif courier == constant.DELHIVERY:
            authfor = "RIGHTMOVEFRANCHISE";
            url = self.get_url(courier,authfor,'pin',oparams);
            response = requests.get(url)
            geodata = response.json()
            pinCodes = self.get_delivery_pincode(courier,authfor,geodata);
        else:
            courier = constant.DELHIVERY;
            authfor = "RIGHTMOVEFRANCHISE";
            url = self.get_url(courier,authfor,'pin',oparams);
            response = requests.get(url)
            geodata = response.json()
            pinCodes = self.get_delivery_pincode(courier,authfor,geodata);
        return pinCodes;


    def get_fetch_eway_code(self,courier,oparams,pincode,doctype,weight,mode):
        eway_codes = "";
        if courier == constant.TRACKON:
            eway_codes = ""
        elif courier== constant.PROFESSIONAL:
            eway_codes = ""
        elif courier == constant.DTDC:
            eway_codes = ""
        elif courier == constant.DELHIVERY:
            authfor = self.get_client_by_booking(pincode,doctype,weight,mode)[2];
            url = self.get_url(courier,authfor,'eway_nos',oparams);
            response = requests.get(url)
            eway_codes = response.json()
        else:
            courier = constant.DELHIVERY;
            authfor = self.get_client_by_booking(pincode,doctype,weight,mode)[2];
            url = self.get_url(courier,authfor,'eway_nos',oparams);
            response = requests.get(url)
            eway_codes = response.json()
        return eway_codes;

    def get_track(self,courier,authfor,oparams):
        return self.get_url(self,courier,authfor,'track',oparams)


    def get_client_by_booking(self,pincode,doctype,weight,mode):
        returnValue = list();
        weight = float(weight)*1000 # weight in grams
        low_weight = 0.8*weight  # 20% low weight send
        
        destination = PinCode.objects.all().filter(pincode=pincode).first().destinationcode;
        zone = CityMapping.objects.all().filter(destination=destination.destinationcode).first();
        if(doctype == constant.DOX):
            if(mode == constant.SURFACE):
                if(0<= weight and weight<250):
                    returnValue.append(low_weight);
                    returnValue.append("EXPRESS");
                    returnValue.append("DOCRIGHTMOVEFRANCHISE");
                    return returnValue;
                elif (250<= weight and weight<1000):
                    returnValue.append(low_weight);
                    returnValue.append("EXPRESS");
                    returnValue.append("RIGHTMOVEFRANCHISE");
                    return returnValue;
                elif (1000<= weight):
                    returnValue.append(low_weight);
                    returnValue.append("SURFACE");
                    returnValue.append("RIGHTMOVEFRANCHISE");
                    return returnValue;
            elif(mode == constant.AIR):
                if(0<= weight and weight<250):
                    returnValue.append(low_weight);
                    returnValue.append("EXPRESS");
                    returnValue.append("DOCRIGHTMOVEFRANCHISE");
                    return  returnValue;
                elif (250<= weight):
                    returnValue.append(low_weight);
                    returnValue.append("EXPRESS");
                    returnValue.append("RIGHTMOVEFRANCHISE");
                    return returnValue;
        elif(doctype == constant.NONDOX):
            if(mode == constant.AIR):
                if(0<= weight and weight<250):
                    returnValue.append(low_weight);
                    returnValue.append("EXPRESS");
                    returnValue.append("DOCRIGHTMOVEFRANCHISE");
                    return returnValue;
                elif (250<= weight):
                    returnValue.append(low_weight);
                    returnValue.append("EXPRESS");
                    returnValue.append("RIGHTMOVEFRANCHISE");
                    return returnValue;
            elif(mode == constant.SURFACE):
                if(zone.zonenondox == constant.NORTH):
                    if(0<= weight and weight<250):
                        returnValue.append(low_weight);
                        returnValue.append("EXPRESS");
                        returnValue.append("DOCRIGHTMOVEFRANCHISE");
                        return returnValue;
                    elif (250<= weight):
                        returnValue.append(low_weight);
                        returnValue.append("EXPRESS");
                        returnValue.append("RIGHTMOVEFRANCHISE");
                        return returnValue;
                elif(zone.zonenondox == constant.NORTHEAST or zone.zonenondox == constant.RNORTHEAST ):
                    if(0<= weight and weight<250):
                        returnValue.append(low_weight);
                        returnValue.append("EXPRESS");
                        returnValue.append("DOCRIGHTMOVEFRANCHISE");
                        return returnValue;
                    elif (250<= weight and weight<2000):
                        returnValue.append(low_weight);
                        returnValue.append("SURFACE");
                        returnValue.append("RIGHTMOVEFRANCHISE");
                        return returnValue;
                    elif (2000<= weight and weight < 20000):
                        returnValue.append(low_weight);
                        returnValue.append("SURFACE");
                        returnValue.append("RIGHTMOVELOGISTICSLW");
                        return returnValue;
                    elif (20000<= weight):
                        returnValue.append(low_weight);
                        returnValue.append("SURFACE");
                        returnValue.append("RIGHTMOVEFRANCHISE");
                        return returnValue;
                else:
                    if(0<= weight and weight<250):
                        returnValue.append(low_weight);
                        returnValue.append("EXPRESS");
                        returnValue.append("DOCRIGHTMOVEFRANCHISE");
                        return returnValue;
                    elif (250<= weight and weight<2000):
                        returnValue.append(low_weight);
                        returnValue.append("SURFACE");
                        returnValue.append("RIGHTMOVEFRANCHISE");
                        return returnValue;
                    elif (2000<= weight and  weight < 20000):
                        returnValue.append(low_weight);
                        returnValue.append("SURFACE");
                        returnValue.append("RIGHTMOVELOGISTICSLW");
                        return returnValue;
                    elif (20000<= weight):
                        returnValue.append(low_weight);
                        returnValue.append("SURFACE");
                        returnValue.append("RIGHTMOVEFRANCHISE");
                        return returnValue;
                        

    def get_delivery_pincode(self,courier,authfor,geodata):
        json_response = self.get_response(courier,authfor,'pin');
        pinCodes = list();
        for pincode in geodata['delivery_codes']:
            pinObj = PinCode();
            dest = Destination();
            courier = Courier.objects.get(branchcode=courier);
            pincode = pincode['postal_code'];
            pinObj.pincode = pincode["pin"];
            pinObj.courier = courier;
            # pinObj.branchcode = pincode[];
            pinObj.oda = pincode["is_oda"];
            pinObj.topay = pincode["pre_paid"];
            pinObj.entrydatetime = None
            # pinObj.compnay = pincode[];
            pinObj.pickup = pincode["pickup"];
            dest.destinationname = pincode["district"]
            dest.statecode = pincode["state_code"]
            pinObj.destinationcode = dest
            # print(pinObj);
            pinCodes.append(pinObj)
        return pinCodes;



    def create_booking(self,booking):
        courier = booking.courier;
        courier_client = self.get_client_by_booking(booking.recpin,booking.prodIty,booking.prodWeight,booking.prodMod);
        # json_response = self.get_response(booking.courier,courier_client[2],'order');
        if courier == constant.TRACKON:
            eway_codes = ""
        elif courier== constant.PROFESSIONAL:
            eway_codes = ""
        elif courier == constant.DTDC:
            eway_codes = ""
        elif courier == constant.DELHIVERY:
            data = self.create_delivery_payload(booking);
            data = json.dumps(data);
            print(data);
            url = self.get_url(courier,courier_client[2],'order',['json',data]);
            print(url)

            response = requests.get(url)
            eway_codes = response.json()

    def create_delivery_payload(self,booking):
        data = {};
        pickup_location = {};
        pickup_location["name"] = "" #
        shipments = [];
        shipments.append(self.create_payload(booking,True)); 
        child_queryset = ChildBooking.objects.filter(masterawbno=booking.awbNo);
        client = Client.objects.get(userid=booking.client);
        for childBooking in child_queryset:
            shipment = self.create_payload(booking,childBooking,client,False);
            shipments.append(shipment); 

        data["pickup_location"] = pickup_location;
        data["shipments"] = shipments;
        return data;


    def create_payload(self,booking,childBooking,client,isMaster):
        shipment = {};
        shipment["mps_amount"] = ""; #//Sum of all package amount for cod. Will be zero incase of prepaid//
        shipment["seller_inv"] = "";
        shipment["shipment_type"] = "MPS"; #//Mandatory for b2c mps//  
        shipment["consignee_gst_tin"] = "";
        shipment["order_date"] = ""; #// current date and time
        shipment["total_amount"] = "" ;  #// 
        shipment["country"] = "India";  #//
        shipment["client_gst_tin"] = "";
        shipment["hsn_code"] = ""; 

        shipment["order"] = booking.invoiceNumber; #invoice number
        shipment["mps_children"] = booking.prodPiece; #// sum of master and child package//
        shipment["cod_amount"] = booking.codAmt;
        shipment["pin"] = client.pin; #// Client pin code
        shipment["add"] = client.address1;  #// Client Address 1
        shipment["state"] = client.statename;        #// Client state
        shipment["seller_gst_tin"]  = client.gstin;     #// mt gstin client 
        shipment["name"] = client.username;         #//client branchname
        shipment["products_desc"] = booking.prodDesc; # prod desc
        shipment["master_id"] = booking.awbNo;#//this will master pakage and need to pass with every package//
        shipment["city"] = booking.recdestination; #// rec cityname
        shipment["phone"] = booking.recphone;     #// rec mobile 
        shipment["payment_mode"] = booking.toFreight;     #// # COD OR PREPAID
        shipment["weight"] = booking.prodWeight; #only for master max 20,000g rest 0
        shipment["waybill"] = booking.awbNo; #// first package will always be master package//
        if isMaster == True:
            shipment["weight"] = 0; #only for master max 20,000g rest 0
            shipment["waybill"] = childBooking.subAwbNo; #// first package will always be master package//
        return shipment;

# rightmovefe = 57173
# docright = 102515
# logic = 101644