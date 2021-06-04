function typeaheadfc(cfilename){

    var cnames = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: cfilename
      });

      cnames.clearPrefetchCache();
      cnames.initialize();
      $('#cliname .typeahead').typeahead('destroy');
      $('#cliname .typeahead').typeahead({
        items:5, 
        minLength:2
        },
        {
        name:'Cnames',
        source:cnames
      }).on('typeahead:selected',function(obj, datam){
            //console.log(datam);
            var pos = datam.lastIndexOf(" ");
            $('#cnamesel').val(datam);
            var pos1 = datam.lastIndexOf('(');
            var pos2 = datam.lastIndexOf(')');
            var cocode = datam.substring(pos1+1, pos2);
            //console.log(cocode);
            typeaheadcadd(cocode);
      });
}

function typeaheadfp(pfilename){
      var pincodes = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch:pfilename 
      });

      pincodes.clearPrefetchCache();
      pincodes.initialize();

      var flag = 0;
      var datas;
      $('#pincode .typeahead').typeahead('destroy');
      $('#pincode').off('keyup');
      $('#pincode .typeahead').typeahead({
            items:5, 
            minLength:1,
            highlight: true,
        },
        {
            name:'pincodes',
            source:pincodes
        }).on('typeahead:selected',function(obj, datam){
            var pos = datam.lastIndexOf(" ")
            $('#istate').val(datam.substring(pos+1,datam.length));
            $('#pinsel').val('selected');
        }).on('keyup', function(obj, datam){
            var $pelem = $('#vpincode');
            var datav = $('#ipincode').val();
         //console.log('datav'+datav)
            if($('.tt-suggestion').length === 0){
                $pelem.text(datav+" Pincode/Destination not in service area, please enter valid data");
                $pelem.css('display','block');
                $('#ipincode').val("");
                $('#istate').val("");
            }
            else{
                $pelem.text("");
                $pelem.css('display','none');
            }
        }).on('typeahead:closed', function(obj, data){
            var $pelem = $('#vpincode');
            if($('#ipincode').val().length < 6 || $('#pinsel').val() != 'selected'){
                //console.log("I am inside--chk details")
                $pelem.text("Pincode/Destination not valid");
                $pelem.css('display','block');
                $('#ipincode').val("");
                $('#istate').val("");
            }
            else{
                $pelem.text("");
                $pelem.css('display','none');
            }

        });
}

function trackAWB(){
    //console.log($('#itrackawb').val())
    if($('#itrackawb').val() == ""){
        $('#trackmsg').text("AWB Number is Required"); 
        return false; 
    }
    else return true;
}

function chkTracking(retcode){
    if (retcode == "SUCCESS"){
        $('#trksuccess').css('display','block')
        $('#trkerror').css('display','none')
    }
    else{
        $('#trksuccess').css('display','none')
        $('#trkerror').css('display','block')
    }
}
$("input[name='cCourier']").on('change',function(){
        //console.log("I am here");
      cmpny= cmap[$("input[name='cCourier']:checked").val()];
      //console.log(cmpny);
      cfilename = '../static/typeahead/cnames'+cmpny+'.json';
      pfilename = '../static/typeahead/pincodes'+cmpny+'.json';
      //console.log(cfilename);
      //console.log(pfilename);
      $('#cocode').val(cmpny);
      typeaheadfp(pfilename);
	  if (cname.trim() != ''){
            //console.log('inside:'+cname.trim());
            if(cmpny == 'RMC' || cmpny == 'UNI'){
                  $('#ccliname').val(cname.trim()+'('+cmpny.charAt(0)+cid.toUpperCase()+')');
                  $('#cnamesel').val(cname.trim()+'('+cmpny.charAt(0)+cid.toUpperCase()+')');
            }else{
                  $('#ccliname').val(cname.trim()+'('+cid.toUpperCase()+')');
                  $('#cnamesel').val(cname.trim()+'('+cid.toUpperCase()+')');
            }
            $('#ccliname').prop('readonly',true);
      }else{
            typeaheadfc(cfilename);
      }
        setdefaults($("input[name='cCourier']:checked").val());
});
function setdefaults(couriercode){
        //console.log(couriercode);
      if(couriercode == 'DELC'){
        $('#nondel').css('display','none');
        $('#ipincode').removeAttr('required');
        $('#dpincode').prop('required', true);
        $('#delv').css('display','block');
        $('#freightpay').attr('disabled',true);
        $('#pcs').val('1');
        $('#pcs').prop('readonly',true);
        $('#qty').val('1');
        $('#qty').prop('readonly',true);
        $('.dimen').prop('required',true);
        $('#awbno').prop('readonly',true);
        $('#optmnl').attr('disabled', true);
        $('#optauto').prop('readonly',true);
        $('#optauto').attr('checked',true);
        $('#llen').text('Length*');
        $('#lwidth').text('Width*');
        $('#lheight').text('Height*');
      }else{
        $('#nondel').css('display','block');
        $('#ipincode').prop('required',true);
        $('#dpincode').removeAttr('required');
        $('#delv').css('display','none');
        $('#freightpay').attr('disabled',false);
        $('#pcs').val('');
        $('#pcs').removeAttr('readonly');
        $('#qty').val('');
        $('#qty').removeAttr('readonly');
        $('.dimen').removeAttr('required');
        $('#awbno').prop('readonly',true);
        $('#optmnl').attr('disabled', true);
        $('#optauto').prop('readonly',true);
        $('#optauto').attr('checked',true); 
        $('#llen').text('Length');
        $('#lwidth').text('Width');
        $('#lheight').text('Height');
        if (cname.trim() != ''){
            if (cid.toUpperCase() == 'GIT' || cid.toUpperCase() == 'SUKH'){
                //console.log("script"+cid);
                $('#optmnl').attr('enabled',true);
                $('#awbno').attr('enabled',true);
                $('#optauto').attr('disabled',true);
                $('#optmnl').attr('checked',true);
            }else{
                $('#optmnl').attr('disabled',true);
                $('#awbno').attr('disabled',true);
                $('#optauto').prop('readonly',true);
                $('#optauto').attr('checked',true); 
            }
        }
    }
}
$('#dpincode').focusout(function (e){
    //console.log($('#dpincode').val().length);
    if($('#dpincode').val().length == 6){
        e.preventDefault();
        $.getJSON('/pininq/' + $('#dpincode').val(), {}, function(data, status){
        //console.log('data'+data+'data'+status)
        var pindata = data.split(';')
        if(status == "success" && pindata[0] !='' ){
            $('#dpincode').val(pindata[0] + " "+ pindata[1]);
            $('#dstate').val(pindata[2]);
            $('#dppincode').text('');
        }else{
            $('#dppincode').text('Pincode not in service area');
            $('#dstate').val('');
            $('#dpincode').val('');
        }
    });
    }else{
        $('#dppincode').text('Please enter pincode');
    }
    return false;
});
$('#dpincode').keydown(function(){
    if($('#dpincode').val().length === 0){
      $('#clickpin').attr('disabled',false);
    }
});
$('#bcCourier').on('change',function(){
      cmpny= cmap[$('#cCourier').val()];
      //console.log(cmpny);
      cfilename = '../static/typeahead/cnames'+cmpny+'.json';
      //console.log(cfilename);
      $('#cocode').val(cmpny);
      typeaheadfc(cfilename);
}); 
