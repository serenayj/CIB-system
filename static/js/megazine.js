$(document).ready(function () {
	var ins1_name = $("#meg1").val();
	var ins2_name = $("#meg2").val();

	$("#inst1").click(function(){
		alert("gooo!!");
		var ins1_url = "<iframe src='//users.instush.com/bee-gallery-v2/?cols=3&rows=3&size=medium&border=10&round=false&space=4&sl=true&bg=transparent&brd=true&pin=true&hc=e72476&ltc=3f3f3f&lpc=ffffff&fc=ffffff&user_id=230246924&username=serenaetjacq&sid=-1&susername=-1&tag="+ins1_name+"&stype=tag&t=999999md0DVXyNTNE9bimrerVImq3p7EUyjBpPxJK1WC1iNl0ykxKQqlV2JdT481bUNoNBcLdiM6TsoZY' allowtransparency='true' frameborder='0' scrolling='no'  style='display:block;width:482px;height:482px;border:none;overflow:visible;' ></iframe>";

		$("#tabs-1").prepend(ins1_url);
		alert("gooo00000!!");

	});

	$("#inst2").click(function(){

		var ins2_url = "<iframe src='//users.instush.com/bee-gallery-v2/?cols=3&rows=3&size=medium&border=10&round=false&space=4&sl=true&bg=transparent&brd=true&pin=true&hc=e72476&ltc=3f3f3f&lpc=ffffff&fc=ffffff&user_id=230246924&username=serenaetjacq&sid=-1&susername=-1&tag="+ins2_name+"&stype=tag&t=999999md0DVXyNTNE9bimrerVImq3p7EUyjBpPxJK1WC1iNl0ykxKQqlV2JdT481bUNoNBcLdiM6TsoZY' allowtransparency='true' frameborder='0' scrolling='no'  style='display:block;width:482px;height:482px;border:none;overflow:visible;' ></iframe>";

		$("#tabs-2").append(ins2_url);

	});


});