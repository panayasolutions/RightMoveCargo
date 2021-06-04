function validate(){
    var elem = document.getElementById("freightcod");
    if (elem.checked){
        document.getElementById("nodis").style.display = "block";
    }
    else{
        document.getElementById("nodis").style.display = "none";
    }

    var awboption = document.getElementById("optmnl")
    if(awboption.checked){
        document.getElementById("awbno").disabled = false;
    }
    else{
        document.getElementById("awbno").disabled = true;
    }
}
function checkamt(){
    if(Number($('#invamt').val()) > 50000){
        $("#ewaybill").prop('required', true);
        $("#ewaylbl").text('Eway Bill No*');
    }
    else{
        $("#ewaylbl").text('Eway Bill No');
        $("#ewaybill").removeAttr('required');
    }

}
function defaultref(){
  //console.log("I am here");
  if($('#dtypendox').prop('selected')){
    $('#refid').val($('#invno').val());
    $('#refid').prop('readonly',true);
    $('#invamtlbl').text('Amount*');
    $('#invnolbl').text('Invoice No*');
    $('#invamt').prop('required',true);
    $('#invno').prop('required',true);
  }
  else{
    $('#refid').val('');
    $('#refid').removeAttr('readonly');
    $('#invamtlbl').text('Amount');
    $('#invnolbl').text('Invoice No');
    $('#invamt').removeAttr('required');
    $('#invno').removeAttr('required');
  }
}
$('#invno').focusout(function(){
    if($('#dtypendox').prop('selected')){
      $('#refid').prop('readonly',true);
      $('#refid').val($('#invno').val());  
    }
});
function loadimageandcolors(cCourier){
    //var cCourier = document.getElementsByName('cCourier');
    var imgtag = document.getElementById('logimage');
    document.getElementById("nodis").style.display = "none";
    imgtag.style.display = "block";
    //alert(classelem.className)
    switch(cCourier){
    case 'TCPL':
        imgtag.src = "../static/images/trackon.svg";
        break;
    case 'RM':
        imgtag.src = "../static/images/logo.png";
        break;
    case 'DELC':
        imgtag.src = "../static/images/delhivery.jpg";
        break;
    case 'PRO':
        imgtag.src = "../static/images/proff.png";
        break;
    case 'DHL':
        imgtag.src = "../static/images/proff.png";
        break;
    case 'DTDC':
        imgtag.src = "../static/images/dtdc.jpeg";
        break;
    default:
        imgtag.style.display = "none";
    }

}
$('#ovraddr').change(function(){
    if($('#ovraddr').prop('checked')){
        $('#coname').val('');
        $('#mphone').val('');
        $('#emailid').val('');
        $('#addline1').val('');
        $('#addline2').val('');
        $('#ipincode').val('');
        $('#dpincode').val('');
        $('#istate').val('');
        $('#dstate').val('');
        $('#ovraddr').removeAttr('checked');
        $('#pinsel').val('');
        $('#divovraddr').css('display','none');
    }
});
$('form').submit(function(){   
    //console.log('inside form chk')       
    var $pelem = $('#vpincode');
    var $pcelem = $('#pcname');
    if((($('#ipincode').val().length < 6 || $('#pinsel').val() != 'selected')) && $("input[name='cCourier']").val()=='TCPL'){
       //console.log("I am inside--chk details")
       $pelem.text("Pincode/Destination not valid");
       $pelem.css('display','block');
       $('#ipincode').val("");
       $('#istate').val("");
       return false;
    }
    else{
       $pelem.text("");
       $pelem.css('display','none');
       console.log($('#cnamesel').val());
       if ($('#cnamesel').val() == '' || $('#cnamesel').val() == undefined){
            $pcelem.text('Invalid client please choose existing');
            $pcelem.css('display','block');
            return false;
       }else{
            $pcelem.text('');
            $pcelem.css('display','block');
            $('#sbutton').prop('disabled', true);
       }
       
    }
});


function typeaheadcadd(cocode){
    var addresses;

    $.getJSON('/consAddress/' + cocode , {}, function(data, status){
        console.log('data'+data+'data'+status);

        var caddrs = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.nonword,
        queryTokenizer: Bloodhound.tokenizers.nonword,
        local: data
        });

        $('#caddress .typeahead').typeahead('destroy');
        $('#caddress .typeahead').typeahead(
          {
          items:5,
          minLength:2
          },
          {
          name:'caddress',
          source: caddrs
          }
        ).on('typeahead:selected',function(obj, datam){
          console.log(datam);
          if( datam != null && datam.length > 0){
            var arr = datam.split(';');
              console.log(arr[0]);
              $('#coname').val(arr[0]);
              $('#mphone').val(arr[6]);
              $('#emailid').val(arr[7]);
              $('#addline1').val(arr[1]);
              $('#addline2').val(arr[2]);
              if($("input[name='cCourier']:checked").val() == 'DELC'){
                $('#dpincode').val(arr[3]+' '+arr[4]);
                $('#dstate').val(arr[5]);
                $('#pinsel').val('selected');
              }else{
                $('#ipincode').val(arr[4]+' '+arr[3]+' '+arr[5]);
                $('#istate').val(arr[5]);
                $('#pinsel').val('selected');
              }

          }

        });
    });

}


/*                if (data.Name != undefined){
                    $('#coname').val(data.Name);
                    $('#mphone').val(data.Mobile);
                    $('#emailid').val(data.EmailId);
                    $('#addline1').val(data.Addr1);
                    $('#addline2').val(data.Addr2);
                    $('#ipincode').val(data.Pin + ' '+data.City);
                    $('#dpincode').val(data.Pin + ' '+data.City);
                    $('#istate').val(data.State);
                    $('#dstate').val(data.State);
                    $('#pinsel').val('selected');
                    $('#divovraddr').css('display','block');
                }
                else{
                    $('#coname').val('');
                    $('#mphone').val('');
                    $('#emailid').val('');
                    $('#addline1').val('');
                    $('#addline2').val('');
                    $('#ipincode').val('');
                    $('#dpincode').val('');
                    $('#istate').val('');
                    $('#dstate').val('');
                    $('#pinsel').val('');
                    $('#divovraddr').css('display','none');
                }
                console.log(data.Name+data.Addr1+data.Addr2+data.City+data.Pin+data.State+data.Mobile+data.EmailId)
            });

}
*/
