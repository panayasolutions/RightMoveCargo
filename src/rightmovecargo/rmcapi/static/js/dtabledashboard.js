$(document).ready(function(){
    $('#ordertable').DataTable({
        "pagingType":"simple_numbers",
        "ordering":false,
        "scrollX":true,
        "columnDefs":[{"orderable":false, 'className':'select-checkbox', 'targets':0}],
        "select": {"style":'multi', "selector": 'td:first-child'},
    });
        //$('.dataTables_length').addClass('bs-select');


});
function printlabel(awb, courier){
	//console.log($('tr.selected').length);
	var itemselcount = $('tr.selected').length;
	if (itemselcount ==0){
		//console.log('inside single print');
    	$.getJSON('/PrintLabel/' +awb+'/'+courier, {}, function(data, status){
            console.log('data'+data+'data'+status);
        	var retdata = data.split(';');
        	if(status == "success" && retdata[0]!='' ){
            	checkprint(retdata[0],retdata[1]);
        	}else{
            	$('#printmsg').text("Error occured during label generation:")
        	}
    	});
    }else{
    	//console.log('Multip page print')
    	var items = $('tr.selected td:nth-child(2), tr.selected td:nth-child(5)').text().split(' ');
    	$.getJSON('/PrintMulti/' +items, {}, function(data, status){
    		//console.log('data'+data+'data'+status);
    		var retdata = data.split(';');
    		if(status == "success" && retdata[0]!='' ){
            	checkprint(retdata[0],retdata[1]);
        	}else{
            	$('#printmsg').text("Error occured during label generation:")
        	}
    	});
    }

}
function checkprint(printop, filename){
    //console.log(printop+filename);
    if(printop == 'Y'){
        //var iframe = document.getElementById('printiframe');
        var oldframe = document.getElementsByTagName("IFRAME")[0]
        if(oldframe != undefined){
        document.body.removeChild(oldframe);}
        var iframe = document.createElement('IFRAME');
        iframe.src = filename;
        iframe.style.display = 'none';
        document.body.appendChild(iframe);
		var useragent=navigator.userAgent.toLowerCase();
		//console.log(useragent);
        if(useragent.indexOf("android") > -1){
			var aelem = document.createElement('a');
			aelem.setAttribute('href',filename);
			aelem.setAttribute('download',"label");
			aelem.style.display= 'none';
			document.body.appendChild(aelem);
			aelem.click();
			document.body.removeChild(aelem);
        }
        else{
		  try{
			 setTimeout(function(){ iframe.contentWindow.print(); }, 1000);
		  }catch(e){alert(e);}
        }
    }
}

$('#checkall').on('click', function(){
	//console.log('chkbox value'+$('#checkall').prop('checked'))
	if($('#checkall').prop('checked')){
		$('tbody tr').addClass('selected');
	}
	else{
		$('tbody tr').removeClass('selected');
	}
});
