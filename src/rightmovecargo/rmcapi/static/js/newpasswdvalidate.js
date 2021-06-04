$('#passConfirm').focusout(function(){
	if($('#passNew').val() === $('#passConfirm').val()){
		return true;
	}
	else{
		$('#msgtxt').text("Passwords do not match");
		$('#passNew').val("");
		$('#passConfirm').val("");
		return false;
	}
});
$('#passNew').focusout(function(){
	console.log("I amm here");
	var str = String($('#passNew').val());
	if (str.length < 10){
		$('#msgtxt').text("Password didnt follow the rules please check and modify");
	}
	else{
		fspchr = str.search(/[$*#!@%]/);
		fnumeric = str.search(/\d/);
		falpha = str.search(/[a-z]|[A-Z]/);
		console.log("fspchr:"+String(fspchr)+"fnumeric:"+String(fnumeric)+"falpha"+String(falpha));
		if(fspchr == -1 || fnumeric == -1 || falpha == -1){
			$('#msgtxt').text("Password didnt follow the rules please check and modify");
			return false;
		}
		else{
			return true;
		}
	}
});