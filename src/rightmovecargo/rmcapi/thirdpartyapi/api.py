import json
from os import WEXITED
from pathlib import Path
import requests

from django.http import request

from rightmovecargo.rmcapi.models import CityMapping, Courier, Destination, PinCode
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
            authfor = self.get_client_by_booking(pincode,doctype,weight,mode);
            url = self.get_url(courier,authfor,'eway_nos',oparams);
            response = requests.get(url)
            eway_codes = response.json()
        else:
            courier = constant.DELHIVERY;
            authfor = self.get_client_by_booking(pincode,doctype,weight,mode);
            url = self.get_url(courier,authfor,'eway_nos',oparams);
            response = requests.get(url)
            eway_codes = response.json()
        return eway_codes;

    def get_track(self,courier,authfor,oparams):
        return self.get_url(self,courier,authfor,'track',oparams)


    def get_client_by_booking(self,pincode,doctype,weight,mode):
        weight = float(weight)*1000 # weight in grams
        destination = PinCode.objects.all().filter(pincode=pincode).first().destinationcode;
        zone = CityMapping.objects.all().filter(destination=destination.destinationcode).first();
        if(doctype == constant.DOX):
            if(mode == constant.SURFACE):
                if(0<= weight and weight<250):
                    return "DOCRIGHTMOVEFRANCHISE";
                elif (250<= weight and weight<1000):
                    return "RIGHTMOVEFRANCHISE";
                elif (1000<= weight):
                    return "RIGHTMOVEFRANCHISE";
            elif(mode == constant.AIR):
                if(0<= weight and weight<250):
                    return "DOCRIGHTMOVEFRANCHISE";
                elif (250<= weight):
                    return "RIGHTMOVEFRANCHISE";
        elif(doctype == constant.NONDOX):
            if(mode == constant.AIR):
                if(0<= weight and weight<250):
                    return "DOCRIGHTMOVEFRANCHISE";
                elif (250<= weight):
                    return "RIGHTMOVEFRANCHISE";
            elif(mode == constant.SURFACE):
                if(zone.zonenondox == constant.NORTH):
                    if(0<= weight and weight<250):
                        return "DOCRIGHTMOVEFRANCHISE";
                    elif (250<= weight):
                        return "RIGHTMOVEFRANCHISE";
                elif(zone.zonenondox == constant.NORTHEAST or zone.zonenondox == constant.RNORTHEAST ):
                    if(0<= weight and weight<250):
                        return "DOCRIGHTMOVEFRANCHISE";
                    elif (250<= weight and weight<2000):
                        return "RIGHTMOVEFRANCHISE";
                    elif (2000<= weight and weight < 20000):
                        return "RIGHTMOVELOGISTICSLW";
                    elif (20000<= weight):
                        return "RIGHTMOVEFRANCHISE";
                else:
                    if(0<= weight and weight<250):
                        return "DOCRIGHTMOVEFRANCHISE";
                    elif (250<= weight and weight<2000):
                        return "RIGHTMOVEFRANCHISE";
                    elif (2000<= weight and  weight < 20000):
                        return "RIGHTMOVELOGISTICSLW";
                    elif (20000<= weight):
                        return "RIGHTMOVEFRANCHISE";
                        



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



# rightmovefe = 57173
# docright = 102515
# logic = 101644