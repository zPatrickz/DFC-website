// JavaScript Document
$(document).ready(function(e) {
	//browser=checkbrowser();
	cact('div1');
	cact('div2');
	cact('div3');
	cact('div1');
	cact('div2');
	cact('div3');
	$('#act_1').hover(function(){
		$('#operation_div').show();
	},
	function(){
		setTimeout(function(){
			$('#operation_div').hide();
		},200);
	});
});

