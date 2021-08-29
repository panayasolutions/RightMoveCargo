import json
from os import WEXITED
from pathlib import Path
import requests

from django.http import request

from rightmovecargo.rmcapi.models import BookingWeb, ChildBooking, CityMapping, Client, Courier, Destination, PinCode, Tbbilling
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
        f.close()
        fullurl = url+params;
        returnValue = list();
        returnValue.append(fullurl);
        returnValue.append(auth);
        return returnValue;


    def get_response(self,courier,authfor,urltype):
        f = open(auth_path,)
        data = json.load(f);
        response = data[courier]['uris'][urltype]['response']
        f.close();
        return response;


    def get_pin_code(self,courier,oparams):
        pinCodes = list();
        if courier == constant.TRACKON:
            return pinCodes;
        elif courier== constant.PROFESSIONAL:
            return pinCodes;
        elif courier == constant.DTDC:
            return pinCodes;
        elif courier == constant.DELHIVERY:
            authfor = "RIGHTMOVEFRANCHISE";
            url = self.get_url(courier,authfor,'pin',oparams)[0];
            response = requests.get(url)
            geodata = response.json()
            pinCodes = self.get_delivery_pincode(courier,authfor,geodata);
            print(pinCodes);
        else:
            courier = constant.DELHIVERY;
            authfor = "RIGHTMOVEFRANCHISE";
            url = self.get_url(courier,authfor,'pin',oparams)[0];
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
            url = self.get_url(courier,authfor,'eway_nos',oparams)[0];
            response = requests.get(url)
            eway_codes = response.json()
        else:
            courier = constant.DELHIVERY;
            authfor = self.get_client_by_booking(pincode,doctype,weight,mode)[2];
            url = self.get_url(courier,authfor,'eway_nos',oparams)[0];
            response = requests.get(url)
            eway_codes = response.json()
        return eway_codes;

    def get_track(self,courier,authfor,oparams):
        return self.get_url(self,courier,authfor,'track',oparams)[0]


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
        # print(geodata);
        json_response = self.get_response(courier,authfor,'pin');
        pinCodes = list();
        # a = PinCode(1111);
        # print(a);
        # return pinCodes;
        for pin in geodata['delivery_codes']:
            #print(pincode);
            pincode = pin['postal_code'];
            pinObj = PinCode(pincode["pin"]);
            dest = Destination(destinationname = pincode["district"]);
            courier = Courier.objects.get(branchcode=courier);
            pinObj.pincode = pincode["pin"];
            pinObj.courier = courier;
            pinObj.oda = pincode["is_oda"];
            pinObj.topay = pincode["pre_paid"];
            pinObj.entrydatetime = None
            pinObj.pickup = pincode["pickup"];
            dest.statecode = pincode["state_code"]
            pinObj.destinationcode = dest  
            pinCodes.append(pinObj)
        return pinCodes;


    def test(self):
        booking = BookingWeb.objects.get(awbNo='5727310066172');
        self.create_booking(booking);
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
            url = self.get_url(courier,courier_client[2],'order',[]);
            data = self.create_delivery_payload(booking,url[1]['Pickup']);
            data = json.dumps(data);
            
            # url = self.get_url(courier,courier_client[2],'order',['json',data]);
            headers = {'Authorization': "Token "+url[1]['token']}
            payload = {'data':data,'format':'json'}
            session = requests.Session()
            response = session.post(url[0],headers=headers,data=payload)
            # my_json = response.content.decode('utf8').replace("'", '"')
            my_json = json.loads(response.content)
            print(my_json);
            return self.genrateError(my_json)
            # print(self.genrateError(my_json));
            # print(data);
            # print(courier_client);
            
            # print(courier_client[2])
            # print(url[1]['Pickup'])
            #response = requests.get(url)
            # eway_codes = response.json();
            # print(eway_codes);

    def create_delivery_payload(self,booking,wearhouse):
        data = {};
        pickup_location = {};
        pickup_location["name"] =  wearhouse#
        shipments = [];
        child_queryset = ChildBooking.objects.filter(masterawbno=booking.awbNo);
        client = Client.objects.get(userid=booking.client);
        shipments.append(self.create_payload_v1(booking,"",client,True)); 
        for childBooking in child_queryset:
            shipment = self.create_payload_v1(booking,childBooking,client,False);
            shipments.append(shipment); 

        data["pickup_location"] = pickup_location;
        data["shipments"] = shipments;
        return data;


    def create_payload(self,booking,childBooking,client,isMaster):
        shipment = {};
        shipment["mps_amount"] = ""; #//Sum of all package amount for cod. Will be zero incase of prepaid//
        shipment["seller_inv"] = "";
        shipment["shipment_type"] = ""; #//Mandatory for b2c mps or blank//  
        shipment["consignee_gst_tin"] = "";
        shipment["order_date"] = ""; #// current date and time
        shipment["total_amount"] = "" ;  #// 
        shipment["country"] = "India";  #//
        shipment["client_gst_tin"] = "";
        shipment["hsn_code"] = ""; 
        shipment["order"] = booking.invoiceNumber; #invoice number
        shipment["mps_children"] = booking.prodPiece; #// sum of master and child package//
        shipment["cod_amount"] = str(booking.codAmt);
       
        shipment["pin"] = booking.recpin; #// Client pin code
        shipment["add"] = booking.recaddr1 + " "+booking.recaddr2;  #// Client Address 1
        shipment["state"] = booking.recstate;        #// Client state
        shipment["seller_gst_tin"]  = client.gstin;     #// mt gstin client 
        shipment["name"] = booking.recname;         #//client branchname
        shipment["products_desc"] = booking.prodDesc; # prod desc
        shipment["master_id"] = booking.awbNo;#//this will master pakage and need to pass with every package//
        shipment["city"] = booking.recdestination; #// rec cityname
        shipment["phone"] = booking.recphone;     #// rec mobile 
        shipment["payment_mode"] = booking.toFreight;     #// # COD OR PREPAID
        shipment["weight"] = str(booking.prodWeight); #only for master max 20,000g rest 0
        shipment["waybill"] = booking.awbNo; #// first package will always be master package//
        if isMaster == False:
            shipment["weight"] = 0; #only for master max 20,000g rest 0
            shipment["waybill"] = childBooking.subAwbNo; #// first package will always be master package//
        return shipment;

# rightmovefe = 57173
# docright = 102515
# logic = 101644



    def create_payload_v1(self,booking,childBooking,client,isMaster):
        returnClient = Client.objects.get(userid="ACE");
        shipment = {};
        # Consignee details
        shipment["add"]=booking.recaddr1 + ","+booking.recaddr2;
        shipment["address_type"]="home office";
        shipment["phone"]=booking.recphone;
        shipment["name"]=booking.recname;
        shipment["pin"]=booking.recpin;
        shipment["city"]=booking.recdestination;
        shipment["state"]=booking.recstate;
        shipment["country"]="India";
        # Consignee details

        # Return details
        shipment["return_name"]=returnClient.username; # MtCompnay = TCPL Return details username
        shipment["return_pin"]=returnClient.pin; # MtCompnay = TCPL Return details
        shipment["return_add"]=returnClient.address1+","+returnClient.address2; # MtCompnay = TCPL Return details
        shipment["return_state"]=returnClient.statename; # MtCompnay = TCPL Return details
        shipment["return_city"]=returnClient.address3; # MtCompnay = TCPL Return details
        shipment["return_phone"]=returnClient.phone;  # MtCompnay = TCPL Return details  
        shipment["return_country"]="India";
        shipment["extra_parameters"]={};
        # Return details

        # client details
        shipment["seller_gst_tin"]=client.gstin; #client gstin
        shipment["seller_tin"]=client.gstin;  #client gstin
        shipment["seller_cst"]=client.gstin   # client gstin
        shipment["seller_name"]=client.username  #client  username
        shipment["seller_add"]=client.address1+","+client.address2;  #client  address1 + address2
        # client details
        
        #Constant Details
        shipment["consignee_gst_tin"]="";
        shipment["consignee_gst_amount"]="";
        shipment["integrated_gst_amount"]="";
        shipment["client_gst_tin"]="";
        shipment["hsn_code"]="";
        shipment["gst_cess_amount"]="";
        shipment["tax_value"]="";
        shipment["seller_gst_amount"]="";
        shipment["od_distance"]="";
        shipment["sales_tax_form_ack_no"]="";
        shipment["fragile_shipment"]="false";     #(Optional;If content is fragile; Key Value must be true else false)
        shipment["document_type"]="EWaybill"; # "EWaybill"
        shipment["dangerous_good"]="False";
        shipment["consignee_tin"]="0";
        shipment["supply_sub_type"]="";
        shipment["plastic_packaging"]="";
        shipment["document_date"]="";
        shipment["taxable_amount"]="";
        shipment["quantity"]="0"
        
        #Constant Details

        #Simple booking table details 
        shipment["document_number"]=booking.EWayNo #"for ewaybill-document_number,only mandatory in case of ewbn", #booking EWaybill number
        shipment["order"]=client.userid+"_"+booking.invoiceNumber; #BranchCode from  mtCustomer + invoice number 
        shipment["ewbn"]=booking.EWayNo; #"if ewbn is there no need to send additional keys for generating ewaybill only if the total package amount is greater than or equal to 50k", #Ewabill number
        shipment["seller_inv"]=booking.invoiceNumber; #invoice number from booking 
        shipment["products_desc"]=booking.prodDesc; #booking prod desc
        shipment["order_date"]=str(booking.entrydatetime); #booking date BookingWeb
        shipment["total_amount"]=str(booking.invoiceValue); #invoice value
        shipment["waybill"]=booking.awbNo; # AWb No
        shipment["master_id"] = booking.awbNo;#//this will master pakage and need to pass with every package//
         #Simple booking table details 
        
        

        commodity_value = str(booking.invoiceValue);
         # if topay or COD or topay + COD then COD 
            # otherwise Prepaid 
        payment_mode = "COD";
        # if cod then cod amount 
        # if topay then Tbbilling total amount after GST
        # if topay + plus cod = cod from webbooking and topay from Tbbilling 
        # if prepaid = then 0
        cod_amount = booking.codAmt;
        shipment_type = "";
        if booking.prodPiece > 1:
            shipment_type = "MPS"


        if booking.toFreight == "PAID":
            payment_mode = "Prepaid";
            cod_amount = 0;

        shipment["cod_amount"]=cod_amount;  
        shipment["payment_mode"]=payment_mode; #"Prepaid/COD/Pickup/REPL", 
        shipment["shipment_type"] = shipment_type; #//Mandatory for b2c mps or blank// 
        
        
        shipment["cod_amount"]=cod_amount;  
        shipment["payment_mode"]=payment_mode; #"Prepaid/COD/Pickup/REPL", 
        shipment["shipment_type"] = shipment_type; #//Mandatory for b2c mps or blank// 
        shipment["mps_amount"] = cod_amount;
        shipment["mps_children"] = booking.prodPiece;

        shipment["category_of_goods"]=""; # if prod desc have medicine then pass essential 
        shipment["commodity_value"]=commodity_value; #invoice value in case  topay and cod then topay+cod in MSP not single package invoice value
        
        shipment["weight"]=str(booking.prodWeight);
        shipment["waybill"] = booking.awbNo; #// first package will always be master package//
        shipment["shipment_height"]=str(booking.height); # if there in booking then use other wise no need
        shipment["shipment_width"]=str(booking.width); # if there in booking then use other wise no need
        shipment["shipment_length"]=str(booking.length); # if there in booking then use other wise no need
        
        if isMaster == False:
            shipment["weight"] = 0; #only for master max 20,000g rest 0
            shipment["waybill"] = childBooking.subAwbNo; #// first package will always be master package//
            shipment["shipment_height"]=str(childBooking.height); # if there in booking then use other wise no need
            shipment["shipment_width"]=str(childBooking.width); # if there in booking then use other wise no need
            shipment["shipment_length"]=str(childBooking.length); # if there in booking then use other wise no need
        
        # if MPS
            # if cod then cod amount 
            # if topay then Tbbilling total amount after GST
            # if topay + plus cod = cod from webbooking and topay from Tbbilling 
            # if prepaid = then 0
            # shipment["mps_amount"] = cod_amount;
            # shipment["mps_children"] = booking.prodPiece;

        return shipment;


        # disbale ewabill if invocie value < 50000

    def genrateError(self,jsonResponse):
        stringError = "";
        seprator = "";
        if jsonResponse["success"] != True:
            stringError = "Delivery Portal : ";
            for package in jsonResponse["packages"]:
                for remark in package["remarks"]:
                    stringError = stringError+seprator + remark;
                    seprator = ",";
        return stringError;
        